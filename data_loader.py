#i am going to use my index to load in pdf documents and to embed them 
#we made vector db which allows to upload essentially vectors and search for vectors but i still need to create vectors

from openai import OpenAI
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv
from fastapi import response


client = OpenAI()
#breakdown the file into chunck and then embed those smaller pieces
#use lama index to read in our pdf, split all the sentences in that pdf into chuncks
#chunck->embed-store in vectordb
EMBED_MODEL="text-embedding-3-large"
EMBED_DIM=3072 #should be same as in vector_db.py file

splitter=SentenceSplitter(chunk_size=1000, chunk_overlap=200) #chunck_overlap is how much of the end one chunck is included in the beginning of another chunk, we need to put chunk so that relevent content doesnt skip
#represents character not words

def load_and_chunk_pdf(path: str):
    docs=PDFReader().load_data(file=path)
    texts=[d.text for d in docs if getattr(d, "text", None)]#pull out the texts, going to get all texts content for every single document inside our documents
    chuncks=[]
    for t in texts:
        chuncks.extend(splitter.split_text(t))
    return chuncks

def embed_texts(texts: list[str]) -> list[list[float]]:#texts are in the form of string, vectors are going to be in float
   reponse=client.embeddings.create(
       model=EMBED_MODEL,
       input=texts,
   )  
   return [item.embedding for item in response.data]
