from typing import Union
from fastapi import FastAPI

from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_milvus import Milvus
from docling.document_converter import DocumentConverter

# Configuration
EMBED_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"

app = FastAPI()

file_path = "C:\\Users\\USER\\Documents\\hackathon\\British National Formulary (BNF85) March to September 2023.pdf"
loader = PyPDFLoader(
    file_path,
    mode="page",
    extraction_mode="layout"
)

#docs = loader.load()

model_kwargs = {'device': 'cuda:0'}

# Création des embeddings
embedding = HuggingFaceEmbeddings(
    model_name=EMBED_MODEL_ID,
    model_kwargs=model_kwargs
)

# Configuration de Milvus
#vector_store_saved = Milvus.from_documents(
#    docs,
#    embedding,
#    collection_name="hackathon",
#    connection_args={"uri": "http://localhost:19530"},
#)
vector_store_saved = Milvus(
    embedding,
    collection_name="hackathon",
    connection_args={"uri": "http://localhost:19530"},
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/query")
def query(q: Union[str, None] = None):
    if q is None:
        return {"result": []}
    res = vector_store_saved.search(
        query=q,
        search_type="similarity",
    )

    return {"result": [hit.page_content for hit in res]}
