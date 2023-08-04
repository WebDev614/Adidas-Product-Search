import streamlit as st

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
