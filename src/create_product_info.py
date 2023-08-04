from src.column_dict import create_column_dict


def create_info(response):

    image_dict, description_dict, price_dict, url_dict = create_column_dict()

    product_info = []
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