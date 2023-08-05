import streamlit as st

def display_product_info(product_info_list):

    for i in range(0, len(product_info_list), 4):
        col1, col2, col3, col4 = st.columns(4)

        col1.markdown(f'<a href="{product_info_list[i]["url"]}" target="_blank"><img src="{product_info_list[i]["image_url"]}" alt="Clickable Image" style="width:550px;"></a>', unsafe_allow_html=True)
        col1.subheader(product_info_list[i]["product"])
        col1.write("Price: $" + product_info_list[i]["price"])
        col1.write(product_info_list[i]["description"])

        if i+1 < len(product_info_list):
            col2.markdown(f'<a href="{product_info_list[i+1]["url"]}" target="_blank"><img src="{product_info_list[i+1]["image_url"]}" alt="Clickable Image" style="width:550px;"></a>', unsafe_allow_html=True)
            col2.subheader(product_info_list[i+1]["product"])
            col2.write("Price: $" + product_info_list[i+1]["price"])
            col2.write(product_info_list[i+1]["description"])

        if i+2 < len(product_info_list):
            col3.markdown(f'<a href="{product_info_list[i+2]["url"]}" target="_blank"><img src="{product_info_list[i+2]["image_url"]}" alt="Clickable Image" style="width:550px;"></a>', unsafe_allow_html=True)
            col3.subheader(product_info_list[i+2]["product"])
            col3.write("Price: $" + product_info_list[i+2]["price"])
            col3.write(product_info_list[i+2]["description"])

        if i+3 < len(product_info_list):
            col4.markdown(f'<a href="{product_info_list[i+3]["url"]}" target="_blank"><img src="{product_info_list[i+3]["image_url"]}" alt="Clickable Image" style="width:550px;"></a>', unsafe_allow_html=True)
            col4.subheader(product_info_list[i+3]["product"])
            col4.write("Price: $" + product_info_list[i+3]["price"])
            col4.write(product_info_list[i+3]["description"])
