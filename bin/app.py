import streamlit as st
import os
import sys
import pandas as pd

current_path = os.path.dirname(os.path.abspath(__file__))
parent_folder_path = os.path.abspath(os.path.join(current_path, os.pardir))
sys.path.append(parent_folder_path)

from src.qa_chain import create_qa_chain
from src.display_product_info import display_product_info
from src.create_product_info import create_info

from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Adidas Product Search", layout="wide")


def main():
    vectordb_path = "vectordb"

    # load vector database
    embeddings = OpenAIEmbeddings()
    vector_db = FAISS.load_local(vectordb_path, embeddings)

    # Custom CSS styling for navigation bar
    with open("src/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.write('<div class="navbar"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Adidas_Logo.svg/2560px-Adidas_Logo.svg.png"></div>', unsafe_allow_html=True)

    st.title("Adidas Product Search")
    user_input = st.text_input("What can I help you look for?", "")
    qa_chain = create_qa_chain(vector_db)
    response = qa_chain.run(user_input)
    if response:
        st.write(response.split("\n")[0].split(".")[1])

        product_info_list = create_info(response)
        display_product_info(product_info_list)
    else:
        st.write("Could not find any matches. Try searching for something else")

if __name__ == "__main__":
    main()
