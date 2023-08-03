from langchain.vectorstores import FAISS
from langchain.document_loaders import CSVLoader
from langchain.embeddings import OpenAIEmbeddings



data_path = "../data/adidas_usa.csv"
db_path = "../vectordb"

# create vector database

def create_vector_db():
    loader = CSVLoader(file_path = data_path)
    
    docs = loader.load()

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(db_path)

if __name__ == "__main__":
    create_vector_db()

