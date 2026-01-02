import pydantic

class RAGChunkAndSrc(pydantic.BaseModel):
    chunks: list[str]
    source_id: str = None
    
class RAGUpsertResult(pydantic.BaseModel): #the result after we upsert document
    ingested: int
    
class RAGSearchResult(pydantic.BaseModel):#searching for some text
    contexts: list[str]
    sources: list[str]
    
class RAGQueryResult(): #query that user is actually sending
    answer: str
    sources: list[str]
    num_contexts: int