import streamlit as st
import os
import sys


# list of urls
image_info_list = [
    {
        "url": 'https://assets.adidas.com/images/w_600,f_auto,q_auto/435ebc4133ec458e85b6ad3500e3a5ec_9366/Short_Sleeve_Graphic_Tee_White_GV5159_01_laydown.jpg',
        "description": "Shirt 1",
        "product": "Short Sleeve",
        "price": "25"
    },
    {
        "url": 'https://assets.adidas.com/images/w_600,f_auto,q_auto/435ebc4133ec458e85b6ad3500e3a5ec_9366/Short_Sleeve_Graphic_Tee_White_GV5159_01_laydown.jpg',
        "description": "Shirt 1",
        "product": "Short Sleeve",
        "price": "25"
    },
    {
        "url": 'https://assets.adidas.com/images/w_600,f_auto,q_auto/435ebc4133ec458e85b6ad3500e3a5ec_9366/Short_Sleeve_Graphic_Tee_White_GV5159_01_laydown.jpg',
        "description": "Shirt 1",
        "product": "Short Sleeve",
        "price": "25"
    },
    {
        "url": 'https://assets.adidas.com/images/w_600,f_auto,q_auto/435ebc4133ec458e85b6ad3500e3a5ec_9366/Short_Sleeve_Graphic_Tee_White_GV5159_01_laydown.jpg',
        "description": "Shirt 1",
        "product": "Short Sleeve",
        "price": "25"
    },
    {
        "url": 'https://assets.adidas.com/images/w_600,f_auto,q_auto/435ebc4133ec458e85b6ad3500e3a5ec_9366/Short_Sleeve_Graphic_Tee_White_GV5159_01_laydown.jpg',
        "description": "Shirt 1",
        "product": "Short Sleeve",
        "price": "25"
    }
]


st.set_page_config(layout="wide")

# # Apply custom CSS for the flip effect
# st.markdown(css_string, unsafe_allow_html=True)


def display_product_info(image_info_list):
    for i in range(0, len(image_info_list), 4):
        col1, col2, col3, col4 = st.columns(4)

        col1.image(image_info_list[i]["url"], use_column_width=True, width=200)
        col1.subheader(image_info_list[i]["product"])
        col1.text("Price: $" + image_info_list[i]["price"])
        col1.text(image_info_list[i]["description"])

        if i+1 < len(image_info_list):
            col2.image(image_info_list[i+1]["url"], use_column_width=True, width=200)
            col2.subheader(image_info_list[i+1]["product"])
            col2.text("Price: $" + image_info_list[i+1]["price"])
            col2.text(image_info_list[i+1]["description"])

        if i+2 < len(image_info_list):
            col3.image(image_info_list[i+2]["url"], use_column_width=True, width=200)
            col3.subheader(image_info_list[i+2]["product"])
            col3.text("Price: $" + image_info_list[i+2]["price"])
            col3.text(image_info_list[i+2]["description"])

        if i+3 < len(image_info_list):
            col4.image(image_info_list[i+3]["url"], use_column_width=True, width=200)
            col4.subheader(image_info_list[i+3]["product"])
            col4.text("Price: $" + image_info_list[i+3]["price"])
            col4.text(image_info_list[i+3]["description"])

def main():
    # Custom CSS styling for navigation bar
    with open("../src/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.write('<div class="navbar"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Adidas_Logo.svg/2560px-Adidas_Logo.svg.png"></div>', unsafe_allow_html=True)

    st.title("Product Display App")
    user_input = st.text_input("What can I help you look for?", "")
    display_product_info(image_info_list)

if __name__ == "__main__":
    main()
