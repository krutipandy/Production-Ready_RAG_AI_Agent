from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

class QdrantStorage:
    def __init__(self, url="http://localhost:6333", collection="docs", dim=3072): #dim number of values inside the vector, turn docs into vectors
        self.client=QdrantClient(url=url, timeout=30) #if we dont connect db in 30 sec it will crash the app
        self.collection=collection #create new collection in vector db inside qdrant storage, there is already collection in init if we dont then we can create from here
        if not self.client.collection_exists(self.collection):
            self.client.create_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(size=dim, distance=Distance.COSINE), #calculating diff points from vectordb, compare vectors against eachother using distance formula, vector words near to each other are similar
            )
            
    def upsert(self, ids, vectors, payloads): #we are going to pass series of ids which is bunch of vectors which is vectorized version of dim 3072, payloads are data that is human readable in which is vectorized
        points=[PointStruct(id=ids[i], vector=vectors[i]) for i in range(len(ids))] #create point structure in order to insert this into our vector database
        self.client.upsert(self.collection, points=points)
        
    def search(self, query_vector, top_k: int=5): #top_k means going to get 5 results we can increase number but it is very fast, search our vectordb its going to get relevent results based on query vector
        results=self.client.search(
            collection_name=self.collection,
            query_vector=query_vector,
            with_payloads=True,
            limit=top_k
        )
        contexts=[] #I need to get all the context or information
        sources=set() #I need to get the sources to the documents basically we pulled info from
        
        for r in results: #pull out all sources and context from results
            payload=getattr(r, "payload", None) or {}
            text=payload.get("text", "")
            source=payload.get("source", "")
            if text:
                contexts.append(text)
                sources.add(source)
                
        return {"contexts": contexts, "sources": list(sources)} #sources are converted into list and going to return sources
        #we are going to lose context is associate with  associated story with which source
        #so if u wanted to we could change it back and then we would have kind of the related data based on indices