
headers2 = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'accept': 'application/json',
    'Referer': 'https://www.ajio.com/b/campus-sutra?query=%3Anewn%3Abrand%3ACampus%20Sutra%3Aoccasion%3ACasual%3Al1l3nestedcategory%3AMen%20-%20Shirts%3Al1l3nestedcategory%3AWomen%20-%20Shirts%3Agenderfilter%3AMen%3Arating%3A4%20star%20%26%20above&classifier=intent&gridColumns=5&segmentIds=',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}
proxies={
        "http": "http://pomijfhn-rotate:unu8s737a7gi@p.webshare.io:80/",
        "https": "http://pomijfhn-rotate:unu8s737a7gi@p.webshare.io:80/"
    }
from curl_cffi import requests
import pandas as pd
data = requests.get('https://www.ajio.com/api/p/466637319_blue', headers=headers2,proxies=proxies)

product_info=data.json()
def extract_size_info(variant):
    return {
        'size': variant['variantOptionQualifiers'][3]['value'],
        'balance_stock': variant['stock']['stockLevel'],
        'Stock_Status': variant['stock']['stockLevelStatus']
    }

# Extract common product information
platform="Ajio"
SKU=product_info['request']['optionCode']
brand = product_info['brandName']
name = product_info['name']
category = product_info['brickName']
selling_price = product_info['price']['value']
mrp = product_info['wasPriceData']['value']
rating = product_info['ratingsResponse']['aggregateRating']['averageRating']
number_of_ratings = product_info['ratingsResponse']['aggregateRating']['numUserRatings']


size_info = [extract_size_info(variant) for variant in product_info['variantOptions']]

product_data = []
for size_variant in size_info:
    product_data.append({
        'Platform': platform,
        'Brand': brand,
        'Name': name,
        'Category': category,
        'SKU': SKU,
        'Selling Price': selling_price,
        'MRP': mrp,
        'size': size_variant['size'],
        'rating': rating,
        'number_of_ratings': number_of_ratings,
        'balance_stock': size_variant['balance_stock'],
        'Stock_Status': size_variant['Stock_Status']
    })

df2 = pd.DataFrame(product_data)


print(df2)


df2.to_clipboard()

from bs4 import BeautifulSoup
import json

data = requests.get('https://www.myntra.com/trousers/campus+sutra/campus-sutra-men-comfort-loose-fit-easy-wash-trousers/30464012/buy', headers=headers2,proxies=proxies)
html_content=data.text
# Assuming the HTML content is stored in a variable called 'html_content'
soup = BeautifulSoup(html_content, 'html.parser')

# Find the script tag containing the product information
script_tag = soup.find('script', text=lambda t: t and 'window.__myx =' in t)

# Extract the JSON data
json_text = script_tag.string.split('window.__myx = ', 1)[1]
data = json.loads(json_text)

# Extract the required information
product_data = data['pdpData']

# Create a list to store the data for each size
rows = []

for size in product_data['sizes']:
    row = {
        'Platform': 'Myntra',
        'Brand': product_data['brand']['name'],
        'Name': product_data['name'],
        'Category': product_data['analytics']['articleType'],
        'SKU': product_data['id'],
        'Selling Price': product_data['price']['discounted'],
        'MRP': product_data['price']['mrp'],
        'Size': size['label'],
        'Rating': product_data['ratings']['averageRating'],
        'Number of Ratings': product_data['ratings']['totalCount'],
        'Balance Stock': size['sizeSellerData'][0]['availableCount'] if size['sizeSellerData'] else 0,
        'Stock Status': 'In Stock' if size['available'] else 'Out of Stock'
    }
    rows.append(row)

# Create a DataFrame
df = pd.DataFrame(rows)

print(df)
