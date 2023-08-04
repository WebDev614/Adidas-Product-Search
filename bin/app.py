import streamlit as st
import os
import sys
import re
import pandas as pd

current_path = os.path.dirname(os.path.abspath(__file__))
parent_folder_path = os.path.abspath(os.path.join(current_path, os.pardir))
sys.path.append(parent_folder_path)

from src.qa_chain import create_qa_chain

from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

os.getenv("OPENAI_API_KEY")

st.set_page_config(layout="wide")

def create_column_dict():

    df = pd.read_csv("data/adidas_usa.csv")


    default_url = "https://assets.adidas.com/images/w_600,f_auto,q_auto/139affb83f16488cb899aafd00b3e2b9_9366/Beach_Shorts_Black_FJ5089_01_laydown.jpg"

    image_urls = df["images"].str.split("~").apply(lambda x: [img for img in x if img.endswith("laydown.jpg")])
    image_urls = image_urls.apply(lambda x: x[0] if x else default_url)
    image_dict = {df['name'][i]: image_urls[i] for i in range(len(df))}


    description_dict = {df['name'][i]: df["description"][i] for i in range(len(df))}
    price_dict = {df['name'][i]: df["selling_price"][i] for i in range(len(df))}
    url_dict = {df['name'][i]: df["url"][i] for i in range(len(df))}
    
    
    return image_dict, description_dict, price_dict, url_dict


def product_info(response):
 
    product_info = []

    image_dict, description_dict, price_dict, url_dict = create_column_dict()


    product_names = []
    for key in image_dict:
        if key in response:
            product_names.append(key)


    for name in product_names:
        product_info.append({
            "image_url": image_dict[name],
            "product": name,
            "price": str(price_dict[name]),
            "description": description_dict[name],
            "url": url_dict[name]
        })

    return product_info



def display_product_info(product_info_list):
    for i in range(0, len(product_info_list), 4):
        col1, col2, col3, col4 = st.columns(4)

        col1.image(product_info_list[i]["image_url"], use_column_width=True, width=200)
        col1.subheader(product_info_list[i]["product"])
        col1.text("Price: $" + product_info_list[i]["price"])
        col1.text(product_info_list[i]["description"])

        if i+1 < len(product_info_list):
            col2.image(product_info_list[i+1]["image_url"], use_column_width=True, width=200)
            col2.subheader(product_info_list[i+1]["product"])
            col2.text("Price: $" + product_info_list[i+1]["price"])
            col2.text(product_info_list[i+1]["description"])

        if i+2 < len(product_info_list):
            col3.image(product_info_list[i+2]["image_url"], use_column_width=True, width=200)
            col3.subheader(product_info_list[i+2]["product"])
            col3.text("Price: $" + product_info_list[i+2]["price"])
            col3.text(product_info_list[i+2]["description"])

        if i+3 < len(product_info_list):
            col4.image(product_info_list[i+3]["image_url"], use_column_width=True, width=200)
            col4.subheader(product_info_list[i+3]["product"])
            col4.text("Price: $" + product_info_list[i+3]["price"])
            col4.text(product_info_list[i+3]["description"])

def main():

    vectordb_path = "vectordb"

    # load vector database
    embeddings = OpenAIEmbeddings()
    vector_db = FAISS.load_local(vectordb_path, embeddings)


    # Custom CSS styling for navigation bar
    with open("src/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.write('<div class="navbar"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Adidas_Logo.svg/2560px-Adidas_Logo.svg.png"></div>', unsafe_allow_html=True)

    st.title("Product Display App")
    user_input = st.text_input("What can I help you look for?", "")
    qa_chain = create_qa_chain(vector_db)
    response = qa_chain.run(user_input)
    st.write(response.split("\n")[0].split(".")[1])

    product_info_list = product_info(response)

    display_product_info(product_info_list)

if __name__ == "__main__":
    main()
