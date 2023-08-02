import streamlit as st

def display_images_in_row(image_urls):
    # Define the number of columns based on the number of images
    num_columns = len(image_urls)

    # Create columns to display images in a row
    columns = st.beta_columns(num_columns)

    # Display each image in a separate column
    for i, url in enumerate(image_urls):
        with columns[i]:
            st.image(url)


# list of urls
image_urls = ['https://assets.adidas.com/images/w_600,f_auto,q_auto/435ebc4133ec458e85b6ad3500e3a5ec_9366/Short_Sleeve_Graphic_Tee_White_GV5159_01_laydown.jpg',
'https://assets.adidas.com/images/w_600,f_auto,q_auto/986bd0fce531401c9c9cad12010a8df6_9366/Graphic_Tee_White_GU3637_01_laydown.jpg',
'https://assets.adidas.com/images/w_600,f_auto,q_auto/b3abdc62d2594c2b97a5ad1200d1b8a4_9366/Long_Sleeve_Graphic_Tee_White_GU1468_01_laydown.jpg',
]

st.title("Display Images from URLs")
display_images_from_urls(image_urls)