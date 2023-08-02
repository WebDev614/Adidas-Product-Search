import streamlit as st
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
parent_folder_path = os.path.abspath(os.path.join(current_path, os.pardir))
sys.path.append(parent_folder_path)

from src.custom_css import css_string
from src.custom_html import html_string

def display_images(image_info_list, images_per_row=4, image_width=300):
    num_images = len(image_info_list)
    num_rows = (num_images + images_per_row - 1) // images_per_row

    for row in range(num_rows):
        start_index = row * images_per_row
        end_index = min((row + 1) * images_per_row, num_images)
        columns = st.columns(end_index - start_index)

        for i in range(start_index, end_index):
            image_info = image_info_list[i]
            with columns[i - start_index]:
                st.markdown(
                    html_string.format(url=image_info['url'], image_width=image_width, description=image_info['description']),
                    unsafe_allow_html=True
                )


# list of urls
image_info_list = [{
    "url": 'https://assets.adidas.com/images/w_600,f_auto,q_auto/435ebc4133ec458e85b6ad3500e3a5ec_9366/Short_Sleeve_Graphic_Tee_White_GV5159_01_laydown.jpg',
    "description": "shirt 1"
},
{
    "url": 'https://assets.adidas.com/images/w_600,f_auto,q_auto/986bd0fce531401c9c9cad12010a8df6_9366/Graphic_Tee_White_GU3637_01_laydown.jpg',
    "description": "shirt 2"
},
{
    "url": 'https://assets.adidas.com/images/w_600,f_auto,q_auto/b3abdc62d2594c2b97a5ad1200d1b8a4_9366/Long_Sleeve_Graphic_Tee_White_GU1468_01_laydown.jpg',
    "description": "shirt 3"
},
{
    "url": 'https://assets.adidas.com/images/w_600,f_auto,q_auto/435ebc4133ec458e85b6ad3500e3a5ec_9366/Short_Sleeve_Graphic_Tee_White_GV5159_01_laydown.jpg',
    "description": "shirt 4"
},
{
    "url": 'https://assets.adidas.com/images/w_600,f_auto,q_auto/b3abdc62d2594c2b97a5ad1200d1b8a4_9366/Long_Sleeve_Graphic_Tee_White_GU1468_01_laydown.jpg',
    "description": "shirt 5"
},
{
    "url": 'https://assets.adidas.com/images/w_600,f_auto,q_auto/435ebc4133ec458e85b6ad3500e3a5ec_9366/Short_Sleeve_Graphic_Tee_White_GV5159_01_laydown.jpg',
    "description": "shirt 6"
},
{
    "url": 'https://assets.adidas.com/images/w_600,f_auto,q_auto/b3abdc62d2594c2b97a5ad1200d1b8a4_9366/Long_Sleeve_Graphic_Tee_White_GU1468_01_laydown.jpg',
    "description": "shirt 7"
},
{
    "url": 'https://assets.adidas.com/images/w_600,f_auto,q_auto/435ebc4133ec458e85b6ad3500e3a5ec_9366/Short_Sleeve_Graphic_Tee_White_GV5159_01_laydown.jpg',
    "description": "shirt 8"
}

]

st.set_page_config(layout="wide")

# Apply custom CSS for the flip effect
st.markdown(css_string, unsafe_allow_html=True)



st.title("Display Images from URLs")
display_images(image_info_list)