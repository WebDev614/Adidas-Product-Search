# column_dict.py
import pandas as pd

def create_column_dict(file_path="./data/adidas_usa.csv"):
    df = pd.read_csv(file_path)

    default_url = "https://st4.depositphotos.com/14953852/22772/v/450/depositphotos_227725020-stock-illustration-image-available-icon-flat-vector.jpg"

    image_urls = df["images"].str.split("~").apply(lambda x: [img for img in x if img.endswith("laydown.jpg")])
    image_urls = image_urls.apply(lambda x: x[0] if x else default_url)
    image_dict = {df['name'][i]: image_urls[i] for i in range(len(df))}

    description_dict = {df['name'][i]: df["description"][i] for i in range(len(df))}
    price_dict = {df['name'][i]: df["selling_price"][i] for i in range(len(df))}
    url_dict = {df['name'][i]: df["url"][i] for i in range(len(df))}

    return image_dict, description_dict, price_dict, url_dict
