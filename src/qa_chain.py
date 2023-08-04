from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI


def create_qa_chain(db):
    """
    This function creates a question and answering chain

    Inputs:
        db - vector database
    Outputs:
        RetrievalQA - The configured question-answering chain
    
    """
    llm = ChatOpenAI(temperature = 0.0)
    qa_stuff = RetrievalQA.from_chain_type(
        llm = llm,
        chain_type = "stuff",
        retriever = db.as_retriever()
    )
    return qa_stuff