import streamlit as st

def display_images_from_urls(image_urls, images_per_row=4, image_width=350):
    num_images = len(image_urls)
    num_rows = (num_images + images_per_row - 1) // images_per_row

    for row in range(num_rows):
        start_index = row * images_per_row
        end_index = min((row + 1) * images_per_row, num_images)
        columns = st.columns(end_index - start_index)

        for i in range(start_index, end_index):
            with columns[i - start_index]:
                st.image(image_urls[i], width=image_width)


# list of urls
image_urls = ['https://assets.adidas.com/images/w_600,f_auto,q_auto/435ebc4133ec458e85b6ad3500e3a5ec_9366/Short_Sleeve_Graphic_Tee_White_GV5159_01_laydown.jpg',
'https://assets.adidas.com/images/w_600,f_auto,q_auto/986bd0fce531401c9c9cad12010a8df6_9366/Graphic_Tee_White_GU3637_01_laydown.jpg',
'https://assets.adidas.com/images/w_600,f_auto,q_auto/b3abdc62d2594c2b97a5ad1200d1b8a4_9366/Long_Sleeve_Graphic_Tee_White_GU1468_01_laydown.jpg',
'https://assets.adidas.com/images/w_600,f_auto,q_auto/435ebc4133ec458e85b6ad3500e3a5ec_9366/Short_Sleeve_Graphic_Tee_White_GV5159_01_laydown.jpg',
'https://assets.adidas.com/images/w_600,f_auto,q_auto/986bd0fce531401c9c9cad12010a8df6_9366/Graphic_Tee_White_GU3637_01_laydown.jpg',
'https://assets.adidas.com/images/w_600,f_auto,q_auto/b3abdc62d2594c2b97a5ad1200d1b8a4_9366/Long_Sleeve_Graphic_Tee_White_GU1468_01_laydown.jpg',
'https://assets.adidas.com/images/w_600,f_auto,q_auto/435ebc4133ec458e85b6ad3500e3a5ec_9366/Short_Sleeve_Graphic_Tee_White_GV5159_01_laydown.jpg',
'https://assets.adidas.com/images/w_600,f_auto,q_auto/986bd0fce531401c9c9cad12010a8df6_9366/Graphic_Tee_White_GU3637_01_laydown.jpg',
]

st.set_page_config(layout="wide")


st.title("Display Images from URLs")
display_images_from_urls(image_urls)