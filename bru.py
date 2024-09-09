import requests
from config import (
    swiggy_cookies, swiggy_headers, swiggy_params,swiggy_json_data,
    blinkit_cookies, blinkit_headers,
    zepto_headers, zepto_json_data,
    bbnow_cookies, bbnow_headers, bbnow_params
)

response = requests.post(
    'https://www.swiggy.com/api/instamart/search',
    params=swiggy_params,
    cookies=swiggy_cookies,
    headers=swiggy_headers,
    json=swiggy_json_data,
)

response = requests.get('https://blinkit.com/v2/listing?filters={%22brand_id%22:%20[5045]}', cookies=blinkit_cookies, headers=blinkit_headers)

response = requests.post('https://user-search.zepto.co.in/api/v3/search', headers=zepto_headers, json=zepto_json_data)


bb = requests.get('https://www.bigbasket.com/listing-svc/v2/products', params=bbnow_params, cookies=bbnow_cookies, headers=bbnow_headers)