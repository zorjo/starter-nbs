# %% [markdown]
# Connected to Python 3.11.8

# %%
zeps

# %%
import requests

cookies = {
    'deviceId': 's%3A218f9800-2306-45b5-8c80-2519af3f682f.NBslBuD1ybpRPHN%2BC7aOCCoEj168QwxWmKlopCyCC7Y',
    'versionCode': '1200',
    'platform': 'web',
    'subplatform': 'dweb',
    'statusBarHeight': '0',
    'bottomOffset': '0',
    'genieTrackOn': 'false',
    'ally-on': 'false',
    'isNative': 'false',
    'strId': '',
    'openIMHP': 'false',
    'webBottomBarHeight': '0',
    'tid': 's%3A9ce06a13-dd7f-480b-8dd7-f3253702d476.6vuw5gU02WfZyoRG7RDaUfw3TwF%2Bh9CNhPCdmosfvl0',
    'sid': 's%3Afia1fd01-e77f-483d-accf-f06adff39070.G44qC55GXjEI79RFPyUYb1w7zbds2rH5%2BfG%2B74qFvgo',
    '__SW': 'du_lhMAH7JoYF7eE5a8CT0ChjAKNKRET',
    '_guest_tid': 'f17e3d45-19a7-4e7b-9cd7-8f08de655722',
    '_device_id': '151ff188-cee7-8750-55b0-9b45f149d508',
    '_sid': 'fia3b9aa-4729-4019-9ae1-925e167b7602',
    'fontsLoaded': '1',
    'lat': 's%3A21.190754149457742.tJEnSmZeHxCsUvyJFUoAtKta8E5O2yK3sxcBKOdlFyY',
    'lng': 's%3A72.84203356309146.aJAwGxxRVL9k0IMQ8DXmIrncu0wzojvEVayYZdtlj4w',
    'address': 's%3A.4Wx2Am9WLolnmzVcU32g6YaFDw0QbIBFRj2nkO7P25s',
    'addressId': 's%3A.4Wx2Am9WLolnmzVcU32g6YaFDw0QbIBFRj2nkO7P25s',
    'LocSrc': 's%3AswgyUL.Dzm1rLPIhJmB3Tl2Xs6141hVZS0ofGP7LGmLXgQOA7Y',
    'userLocation': '%7B%22address%22%3A%22%22%2C%22lat%22%3A21.190754149457742%2C%22lng%22%3A72.84203356309146%2C%22id%22%3A%22%22%2C%22annotation%22%3A%22%22%2C%22name%22%3A%22%22%7D',
    'imOrderAttribution': '{%22entryId%22:%22TAXONOMY-Cleaning%20Essentials%22%2C%22entryName%22:%22store-menu-items-instamart%22}',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'deviceId=s%3A218f9800-2306-45b5-8c80-2519af3f682f.NBslBuD1ybpRPHN%2BC7aOCCoEj168QwxWmKlopCyCC7Y; versionCode=1200; platform=web; subplatform=dweb; statusBarHeight=0; bottomOffset=0; genieTrackOn=false; ally-on=false; isNative=false; strId=; openIMHP=false; webBottomBarHeight=0; tid=s%3A9ce06a13-dd7f-480b-8dd7-f3253702d476.6vuw5gU02WfZyoRG7RDaUfw3TwF%2Bh9CNhPCdmosfvl0; sid=s%3Afia1fd01-e77f-483d-accf-f06adff39070.G44qC55GXjEI79RFPyUYb1w7zbds2rH5%2BfG%2B74qFvgo; __SW=du_lhMAH7JoYF7eE5a8CT0ChjAKNKRET; _guest_tid=f17e3d45-19a7-4e7b-9cd7-8f08de655722; _device_id=151ff188-cee7-8750-55b0-9b45f149d508; _sid=fia3b9aa-4729-4019-9ae1-925e167b7602; fontsLoaded=1; lat=s%3A21.190754149457742.tJEnSmZeHxCsUvyJFUoAtKta8E5O2yK3sxcBKOdlFyY; lng=s%3A72.84203356309146.aJAwGxxRVL9k0IMQ8DXmIrncu0wzojvEVayYZdtlj4w; address=s%3A.4Wx2Am9WLolnmzVcU32g6YaFDw0QbIBFRj2nkO7P25s; addressId=s%3A.4Wx2Am9WLolnmzVcU32g6YaFDw0QbIBFRj2nkO7P25s; LocSrc=s%3AswgyUL.Dzm1rLPIhJmB3Tl2Xs6141hVZS0ofGP7LGmLXgQOA7Y; userLocation=%7B%22address%22%3A%22%22%2C%22lat%22%3A21.190754149457742%2C%22lng%22%3A72.84203356309146%2C%22id%22%3A%22%22%2C%22annotation%22%3A%22%22%2C%22name%22%3A%22%22%7D; imOrderAttribution={%22entryId%22:%22TAXONOMY-Cleaning%20Essentials%22%2C%22entryName%22:%22store-menu-items-instamart%22}',
    'matcher': 'df89g8e9ac9dbf8fg8g99b8',
    'origin': 'https://www.swiggy.com',
    'priority': 'u=1, i',
    'referer': 'https://www.swiggy.com/instamart/search?categoryName=Cleaning+Essentials&custom_back=true&filterId=63a1b0c81b37c809f929c020&query=Scotch+Brite&storeId=1387706&taxonomyType=All+Listing',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

params = {
    'pageNumber': '0',
    'searchResultsOffset': '0',
    'limit': '40',
    'query': 'Scotch Brite',
    'ageConsent': 'false',
    'layoutId': '3990',
    'pageType': 'INSTAMART_AUTO_SUGGEST_PAGE',
    'isPreSearchTag': 'false',
    'highConfidencePageNo': '0',
    'lowConfidencePageNo': '0',
    'voiceSearchTrackingId': '',
    'storeId': '1387706',
}

json_data = {
    'facets': {},
    'sortAttribute': '',
}

sw = requests.post(
    'https://www.swiggy.com/api/instamart/search',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)

import requests

cookies = {
    'gr_1_deviceId': 'f9e5183c-add2-4fce-b651-99f45c303a24',
    '__cfruid': '7f85240dccc08a13bc5c2fc06ee8c7b08da9badf-1723528950',
    '_cfuvid': 'uBcPR2rBmIdGt.RoyF98AyQBdjeqb2ik6o67IpjAEg4-1723528950937-0.0.1.1-604800000',
    'gr_1_lat': '28.4652382',
    'gr_1_lon': '77.0615957',
    'gr_1_locality': '1849',
    'gr_1_landmark': 'undefined',
    '__cf_bm': '5KDu5vj4jCLZNqz7hXwha9B2xDqQI3aSQNv3RJpm7sE-1723530362-1.0.1.1-_G__v0dFw0ySRgQ_OnRygJ5dq.1fmO6AkbfSmuXLvkQ0GLwOO2MIdt2lMA8XgWzT8uT4Q_a8PdUcFRjYbiRbLg',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'app_client': 'consumer_web',
    'app_version': '52434332',
    'auth_key': 'c761ec3633c22afad934fb17a66385c1c06c5472b4898b866b7306186d0bb477',
    'content-type': 'application/json',
    # 'cookie': 'gr_1_deviceId=f9e5183c-add2-4fce-b651-99f45c303a24; __cfruid=7f85240dccc08a13bc5c2fc06ee8c7b08da9badf-1723528950; _cfuvid=uBcPR2rBmIdGt.RoyF98AyQBdjeqb2ik6o67IpjAEg4-1723528950937-0.0.1.1-604800000; gr_1_lat=28.4652382; gr_1_lon=77.0615957; gr_1_locality=1849; gr_1_landmark=undefined; __cf_bm=5KDu5vj4jCLZNqz7hXwha9B2xDqQI3aSQNv3RJpm7sE-1723530362-1.0.1.1-_G__v0dFw0ySRgQ_OnRygJ5dq.1fmO6AkbfSmuXLvkQ0GLwOO2MIdt2lMA8XgWzT8uT4Q_a8PdUcFRjYbiRbLg',
    'device_id': 'f9e5183c-add2-4fce-b651-99f45c303a24',
    'lat': '28.4652382',
    'lon': '77.0615957',
    'priority': 'u=1, i',
    'referer': 'https://blinkit.com/brand/scotch-brite/5045',
    'rn_bundle_version': '1009003012',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'session_uuid': '04fba0d4-133a-4bea-a942-ef092f27203d',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'web_app_version': '1008010016',
}

blk = requests.get('https://blinkit.com/v2/listing?filters={%22brand_id%22:%20[5045]}', cookies=cookies, headers=headers)
#blinkit and swiggy zepto bbnow 
import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'appversion': '11.8.3-WEB',
    'compatible_components': 'CONVENIENCE_FEE,RAIN_FEE,EXTERNAL_COUPONS,STANDSTILL,BUNDLE,MULTI_SELLER_ENABLED,PIP_V1,ROLLUPS,SCHEDULED_DELIVERY,SAMPLING_ENABLED,ETA_NORMAL_WITH_149_DELIVERY,ETA_NORMAL_WITH_199_DELIVERY,HOMEPAGE_V2,NEW_ETA_BANNER,VERTICAL_FEED_PRODUCT_GRID,AUTOSUGGESTION_PAGE_ENABLED,AUTOSUGGESTION_PIP,AUTOSUGGESTION_AD_PIP,BOTTOM_NAV_FULL_ICON,COUPON_WIDGET_CART_REVAMP,DELIVERY_UPSELLING_WIDGET,NEW_ROLLUPS_ENABLED,RERANKING_QCL_RELATED_PRODUCTS,PLP_ON_SEARCH,PAAN_BANNER_WIDGETIZED,ROLLUPS_UOM,DYNAMIC_FILTERS,PHARMA_ENABLED,NEW_FEE_STRUCTURE,NEW_BILL_INFO,RE_PROMISE_ETA_ORDER_SCREEN_ENABLED,MANUALLY_APPLIED_DELIVERY_FEE_RECEIVABLE,MARKETPLACE_REPLACEMENT,ZEPTO_PASS,ZEPTO_PASS:1,ZEPTO_PASS:2,ZEPTO_PASS_RENEWAL',
    'content-type': 'application/json',
    'deviceid': '4263125861026457',
    'origin': 'https://www.zeptonow.com',
    'platform': 'WEB',
    'priority': 'u=1, i',
    'referer': 'https://www.zeptonow.com/',
    'requestid': '8702663244638380',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sessionid': '8831510182529992',
    'store_etas': '{261b9c45-eb5b-4398-be1c-909ccde6f629:10}',
    'store_id': '261b9c45-eb5b-4398-be1c-909ccde6f629',
    'store_ids': '261b9c45-eb5b-4398-be1c-909ccde6f629',
    'storeetas': '{261b9c45-eb5b-4398-be1c-909ccde6f629:10}',
    'storeid': '261b9c45-eb5b-4398-be1c-909ccde6f629',
    'storeids': '261b9c45-eb5b-4398-be1c-909ccde6f629',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-without-bearer': 'true',
}

json_data = {
    'query': 'scotch',
    'pageNumber': 0,
    'intentId': 'fc3f5a24-d7de-47bd-a3f1-feb2a5209cc8',
    'mode': 'AUTOSUGGEST',
}

zp = requests.post('https://user-search.zepto.co.in/api/v3/search', headers=headers, json=json_data)

import requests

cookies = {
    '_bb_locSrc': 'default',
    '_bb_hid': '1723',
    '_bb_vid': '"MTI1NTI0OTI1NTM="',
    '_bb_tc': '0',
    '_client_version': '2789',
    '_bb_rdt': '"MzEwNDcwMTYwMg==.0"',
    '_bb_rd': '6',
    '_sp_van_encom_hid': '1722',
    '_sp_bike_hid': '1720',
    'sessionid': 'jennhyzk7qr8qsdr4v5s23o441oa8fub',
    'csrftoken': 'ek2YxxEh6ltRLwy5WuNsLsmXnbHJCBG3FMp8SNDihAPmLvg9UPWUP4PO1T6PMJix',
    'jarvis-id': '66d7b15e-8446-485f-9490-df3f32309689',
    'x-entry-context-id': '100',
    'x-entry-context': 'bb-b2c',
    'x-channel': 'web',
    '_bb_bb2.0': '1',
    'is_global': '0',
    '_is_bb1.0_supported': '0',
    'is_integrated_sa': '0',
    'bb2_enabled': 'true',
    '_is_tobacco_enabled': '0',
    '_bb_cid': '14',
    '_bb_lat_long': '"MjIuNTA4NDQ5N3w4OC4zMzAwMDQxOTk5OTk5OQ=="',
    '_bb_aid': '"Mjk2MTgwNTUxMg=="',
    '_bb_addressinfo': 'MjIuNTA4NDQ5N3w4OC4zMzAwMDQxOTk5OTk5OXxTYWhhcHVyfDcwMDAzOHxLb2xrYXRhfDF8ZmFsc2V8dHJ1ZXx0cnVlfEJpZ2Jhc2tldGVlcg==',
    '_bb_pin_code': '700038',
    '_bb_cda_sa_info': 'djIuY2RhX3NhLjEwMC4xMDg5NCwxMDg5NQ==',
    'ts': '2024-08-13%2008:50:44.208',
    'csurftoken': 'sTHsQQ.MTI1NTI0OTI1NTM=.1723531478045.LFkz62OA24kwcW/HTRNaGAEnrEURb/f+v4unRnQOK1I=',
    '_bb_sa_ids': '10894,10895',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': '_bb_locSrc=default; _bb_hid=1723; _bb_vid="MTI1NTI0OTI1NTM="; _bb_tc=0; _client_version=2789; _bb_rdt="MzEwNDcwMTYwMg==.0"; _bb_rd=6; _sp_van_encom_hid=1722; _sp_bike_hid=1720; sessionid=jennhyzk7qr8qsdr4v5s23o441oa8fub; csrftoken=ek2YxxEh6ltRLwy5WuNsLsmXnbHJCBG3FMp8SNDihAPmLvg9UPWUP4PO1T6PMJix; jarvis-id=66d7b15e-8446-485f-9490-df3f32309689; x-entry-context-id=100; x-entry-context=bb-b2c; x-channel=web; _bb_bb2.0=1; is_global=0; _is_bb1.0_supported=0; is_integrated_sa=0; bb2_enabled=true; _is_tobacco_enabled=0; _bb_cid=14; _bb_lat_long="MjIuNTA4NDQ5N3w4OC4zMzAwMDQxOTk5OTk5OQ=="; _bb_aid="Mjk2MTgwNTUxMg=="; _bb_addressinfo=MjIuNTA4NDQ5N3w4OC4zMzAwMDQxOTk5OTk5OXxTYWhhcHVyfDcwMDAzOHxLb2xrYXRhfDF8ZmFsc2V8dHJ1ZXx0cnVlfEJpZ2Jhc2tldGVlcg==; _bb_pin_code=700038; _bb_cda_sa_info=djIuY2RhX3NhLjEwMC4xMDg5NCwxMDg5NQ==; ts=2024-08-13%2008:50:44.208; csurftoken=sTHsQQ.MTI1NTI0OTI1NTM=.1723531478045.LFkz62OA24kwcW/HTRNaGAEnrEURb/f+v4unRnQOK1I=; _bb_sa_ids=10894,10895',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjgzNzMwNCIsImFwIjoiMTgzNDk4NzAwMiIsImlkIjoiNjcyYjI4M2FiN2I4MDBkOSIsInRyIjoiMWI3N2UyNmRkMzY5MDdjOTc3MzJhMWI1ODc4MWMyNjQiLCJ0aSI6MTcyMzUzMTQ4ODcwMH19',
    'priority': 'u=1, i',
    'referer': 'https://www.bigbasket.com/pb/scotch-brite/?nc=scotch-brite&page=1',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-1b77e26dd36907c97732a1b58781c264-672b283ab7b800d9-01',
    'tracestate': '837304@nr=0-1-837304-1834987002-672b283ab7b800d9----1723531488700',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-channel': 'BB-WEB',
    'x-tracker': '673b547f-55ce-43e8-889c-9d2a0db8730c',
}

params = {
    'type': 'pb',
    'slug': 'scotch-brite',
    'page': '1',
}

bb = requests.get('https://www.bigbasket.com/listing-svc/v2/products', params=params, cookies=cookies, headers=headers)

# %% [markdown]
# No kernel connected

# %% [markdown]
# No kernel connected

# %% [markdown]
# No kernel connected

# %% [markdown]
# Connected to miniforge3 (Python 3.10.14)

# %%
import curl_cffi

# %% [markdown]
# Connected to Python 3.11.8

# %%
import curl_cffi

# %%
from curl_cffi import requests

# %%
import requests

cookies = {
    'T': 'cltwbqz3e00fb0igmxi62engy-BR1710728785706',
    'K-ACTION': 'null',
    'rt': 'null',
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
    'ud': '8.H-ln8QiRdJI2Sd_6H6Ww6mCGs5k2lJvvabgQRdssG5321-ouTQpXVTW2mrutYyTq_DhAZJ3sEEWPSuCCDJppX5qR55Z7qESpLWDD4WgI0rqWyfVt7rkfrGOt0xHAAgatGj1RXlXfHj0XWYrYUa0rqOcsqGEkpMhxf-ckWx3AYv0RCFzcLeHFYY8rF7z2n-_6TvX7FbPDSXmKUiskpBu5qRe_SSdgVOJT-W0KdB3ucIaLq-tbJE-RoR-7vifQo5LIRNKpzJ6C9bFkzaCfonRNw-byQ92IGaLd871fs1H4yFmSwnG5_96WE476VhusuZuD',
    'Network-Type': '4g',
    'vh': '743',
    'vw': '1535',
    'dpr': '1.25',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3MjY5ODk3MDksImlhdCI6MTcyNTI2MTcwOSwiaXNzIjoia2V2bGFyIiwianRpIjoiODE3NGI1NjQtODg4OS00YmM4LWE3NTItOGM3MDUzNjA1N2FkIiwidHlwZSI6IkFUIiwiZElkIjoiY2x0d2JxejNlMDBmYjBpZ214aTYyZW5neS1CUjE3MTA3Mjg3ODU3MDYiLCJrZXZJZCI6IlZJMTMwQ0VCMTI2MkNCNDNFRTlGODg1OUMzMURDQ0RGQzMiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.pShvfWh3lv3Njz_o5lcsYX_dBo3qOM2QKXHMWyBffc8',
    'SN': 'VI130CEB1262CB43EE9F8859C31DCCDFC3.TOK88CA875348444489BAEF8CF2F36FBED3.1725734430.LO',
    'vd': 'VI130CEB1262CB43EE9F8859C31DCCDFC3-1722174934057-20.1725734430.1725733024.159733711',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19974%7CMCMID%7C43798188536455097640562161626710135828%7CMCAID%7CNONE%7CMCOPTOUT-1725741641s%7CNONE',
    'S': 'd1t10BHg/Tz8SPz8/KD8/Jz8/Pzk/qvzzPhTtU4/7AtDZX6noqNt9FMAQNvgZM9OIVbfcknjBCNDzRUni0yTwyp5gww==',
    's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Agrocery%25253Ahousehold-care%25253Apr%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'T=cltwbqz3e00fb0igmxi62engy-BR1710728785706; K-ACTION=null; rt=null; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; ud=8.H-ln8QiRdJI2Sd_6H6Ww6mCGs5k2lJvvabgQRdssG5321-ouTQpXVTW2mrutYyTq_DhAZJ3sEEWPSuCCDJppX5qR55Z7qESpLWDD4WgI0rqWyfVt7rkfrGOt0xHAAgatGj1RXlXfHj0XWYrYUa0rqOcsqGEkpMhxf-ckWx3AYv0RCFzcLeHFYY8rF7z2n-_6TvX7FbPDSXmKUiskpBu5qRe_SSdgVOJT-W0KdB3ucIaLq-tbJE-RoR-7vifQo5LIRNKpzJ6C9bFkzaCfonRNw-byQ92IGaLd871fs1H4yFmSwnG5_96WE476VhusuZuD; Network-Type=4g; vh=743; vw=1535; dpr=1.25; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3MjY5ODk3MDksImlhdCI6MTcyNTI2MTcwOSwiaXNzIjoia2V2bGFyIiwianRpIjoiODE3NGI1NjQtODg4OS00YmM4LWE3NTItOGM3MDUzNjA1N2FkIiwidHlwZSI6IkFUIiwiZElkIjoiY2x0d2JxejNlMDBmYjBpZ214aTYyZW5neS1CUjE3MTA3Mjg3ODU3MDYiLCJrZXZJZCI6IlZJMTMwQ0VCMTI2MkNCNDNFRTlGODg1OUMzMURDQ0RGQzMiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.pShvfWh3lv3Njz_o5lcsYX_dBo3qOM2QKXHMWyBffc8; SN=VI130CEB1262CB43EE9F8859C31DCCDFC3.TOK88CA875348444489BAEF8CF2F36FBED3.1725734430.LO; vd=VI130CEB1262CB43EE9F8859C31DCCDFC3-1722174934057-20.1725734430.1725733024.159733711; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19974%7CMCMID%7C43798188536455097640562161626710135828%7CMCAID%7CNONE%7CMCOPTOUT-1725741641s%7CNONE; S=d1t10BHg/Tz8SPz8/KD8/Jz8/Pzk/qvzzPhTtU4/7AtDZX6noqNt9FMAQNvgZM9OIVbfcknjBCNDzRUni0yTwyp5gww==; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Agrocery%25253Ahousehold-care%25253Apr%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV',
    'Origin': 'https://www.flipkart.com',
    'Referer': 'https://www.flipkart.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'X-User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 FKUA/website/42/website/Desktop',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'pageUri': '/grocery/household-care/pr?sid=73z%2Ccwl&marketplace=GROCERY&businessZone=bz_chn_01&fm=neo%2Fmerchandising&ppt=browse&ppn=browse&p%5B%5D=facets.brand%255B%255D%3DScotch-Brite&sort=price_asc',
    'pageContext': {
        'fetchSeoData': True,
        'paginatedFetch': True,
        'pageNumber': 1,
    },
    'requestContext': {
        'type': 'BROWSE_PAGE',
        'ssid': 'rk53wpddds0000001725734433004',
        'sqid': 'agh93yobdc0000001725734462400',
    },
}

response = requests.post('https://2.rome.api.flipkart.com/api/4/page/fetch', headers=headers, json=json_data)


# %%
response

# %%
import requests

cookies = {
    'T': 'cltwbqz3e00fb0igmxi62engy-BR1710728785706',
    'K-ACTION': 'null',
    'rt': 'null',
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
    'ud': '8.H-ln8QiRdJI2Sd_6H6Ww6mCGs5k2lJvvabgQRdssG5321-ouTQpXVTW2mrutYyTq_DhAZJ3sEEWPSuCCDJppX5qR55Z7qESpLWDD4WgI0rqWyfVt7rkfrGOt0xHAAgatGj1RXlXfHj0XWYrYUa0rqOcsqGEkpMhxf-ckWx3AYv0RCFzcLeHFYY8rF7z2n-_6TvX7FbPDSXmKUiskpBu5qRe_SSdgVOJT-W0KdB3ucIaLq-tbJE-RoR-7vifQo5LIRNKpzJ6C9bFkzaCfonRNw-byQ92IGaLd871fs1H4yFmSwnG5_96WE476VhusuZuD',
    'Network-Type': '4g',
    'vh': '743',
    'vw': '1535',
    'dpr': '1.25',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3MjY5ODk3MDksImlhdCI6MTcyNTI2MTcwOSwiaXNzIjoia2V2bGFyIiwianRpIjoiODE3NGI1NjQtODg4OS00YmM4LWE3NTItOGM3MDUzNjA1N2FkIiwidHlwZSI6IkFUIiwiZElkIjoiY2x0d2JxejNlMDBmYjBpZ214aTYyZW5neS1CUjE3MTA3Mjg3ODU3MDYiLCJrZXZJZCI6IlZJMTMwQ0VCMTI2MkNCNDNFRTlGODg1OUMzMURDQ0RGQzMiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.pShvfWh3lv3Njz_o5lcsYX_dBo3qOM2QKXHMWyBffc8',
    'SN': 'VI130CEB1262CB43EE9F8859C31DCCDFC3.TOK88CA875348444489BAEF8CF2F36FBED3.1725734430.LO',
    'vd': 'VI130CEB1262CB43EE9F8859C31DCCDFC3-1722174934057-20.1725734430.1725733024.159733711',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19974%7CMCMID%7C43798188536455097640562161626710135828%7CMCAID%7CNONE%7CMCOPTOUT-1725741641s%7CNONE',
    'S': 'd1t10BHg/Tz8SPz8/KD8/Jz8/Pzk/qvzzPhTtU4/7AtDZX6noqNt9FMAQNvgZM9OIVbfcknjBCNDzRUni0yTwyp5gww==',
    's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Agrocery%25253Ahousehold-care%25253Apr%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'T=cltwbqz3e00fb0igmxi62engy-BR1710728785706; K-ACTION=null; rt=null; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; ud=8.H-ln8QiRdJI2Sd_6H6Ww6mCGs5k2lJvvabgQRdssG5321-ouTQpXVTW2mrutYyTq_DhAZJ3sEEWPSuCCDJppX5qR55Z7qESpLWDD4WgI0rqWyfVt7rkfrGOt0xHAAgatGj1RXlXfHj0XWYrYUa0rqOcsqGEkpMhxf-ckWx3AYv0RCFzcLeHFYY8rF7z2n-_6TvX7FbPDSXmKUiskpBu5qRe_SSdgVOJT-W0KdB3ucIaLq-tbJE-RoR-7vifQo5LIRNKpzJ6C9bFkzaCfonRNw-byQ92IGaLd871fs1H4yFmSwnG5_96WE476VhusuZuD; Network-Type=4g; vh=743; vw=1535; dpr=1.25; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3MjY5ODk3MDksImlhdCI6MTcyNTI2MTcwOSwiaXNzIjoia2V2bGFyIiwianRpIjoiODE3NGI1NjQtODg4OS00YmM4LWE3NTItOGM3MDUzNjA1N2FkIiwidHlwZSI6IkFUIiwiZElkIjoiY2x0d2JxejNlMDBmYjBpZ214aTYyZW5neS1CUjE3MTA3Mjg3ODU3MDYiLCJrZXZJZCI6IlZJMTMwQ0VCMTI2MkNCNDNFRTlGODg1OUMzMURDQ0RGQzMiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.pShvfWh3lv3Njz_o5lcsYX_dBo3qOM2QKXHMWyBffc8; SN=VI130CEB1262CB43EE9F8859C31DCCDFC3.TOK88CA875348444489BAEF8CF2F36FBED3.1725734430.LO; vd=VI130CEB1262CB43EE9F8859C31DCCDFC3-1722174934057-20.1725734430.1725733024.159733711; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19974%7CMCMID%7C43798188536455097640562161626710135828%7CMCAID%7CNONE%7CMCOPTOUT-1725741641s%7CNONE; S=d1t10BHg/Tz8SPz8/KD8/Jz8/Pzk/qvzzPhTtU4/7AtDZX6noqNt9FMAQNvgZM9OIVbfcknjBCNDzRUni0yTwyp5gww==; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Agrocery%25253Ahousehold-care%25253Apr%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV',
    'Origin': 'https://www.flipkart.com',
    'Referer': 'https://www.flipkart.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'X-User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 FKUA/website/42/website/Desktop',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'pageUri': '/grocery/household-care/pr?sid=73z%2Ccwl&marketplace=GROCERY&businessZone=bz_chn_01&fm=neo%2Fmerchandising&ppt=browse&ppn=browse&p%5B%5D=facets.brand%255B%255D%3DScotch-Brite&sort=price_asc',
    'pageContext': {
        'fetchSeoData': True,
        'paginatedFetch': True,
        'pageNumber': 1,
    },
    'requestContext': {
        'type': 'BROWSE_PAGE',
        'ssid': 'rk53wpddds0000001725734433004',
        'sqid': 'agh93yobdc0000001725734462400',
    },
}

response = requests.post('https://2.rome.api.flipkart.com/api/4/page/fetch',cookies=cookies, headers=headers, json=json_data)


# %%
response

# %%
response.json()

# %%
pattern = "widget.data.products.productInfo.value"

# %%
import jq 
products=jq.all(jq_pattern, json_data)

# %%
import jq 
products=jq.all(pattern, json_data)

# %%
pattern = ".RESPONSE.slotswidget.data.products.productInfo.value"

# %%
import jq 
products=jq.all(pattern, json_data)

# %%
products

# %%
pattern = ".RESPONSE.slots.widget.data.products.productInfo.value"

# %%
products=jq.all(pattern, json_data)

# %%
products

# %%
pattern = ".RESPONSE.slots[].widget.data.products[].productInfo.value"

# %%
products=jq.all(pattern, json_data)

# %%
pattern = ".RESPONSE.slots[].widget.data.products[]?.productInfo?.value"

# %%
products=jq.all(pattern, json_data)

# %%
pattern = ".RESPONSE.slots[].widget.data?.products[]?.productInfo?.value"
jq.all(pattern, json_data)

# %%
pattern = ".RESPONSE.slots[].widget?.data?.products[]?.productInfo?.value"
jq.all(pattern, json_data)

# %%
pattern = ".RESPONSE.slots[].widget?.data?.products[]?.productInfo?.value?"
jq.all(pattern, json_data)

# %%
pattern = "."
jq.all(pattern, json_data)

# %%
pattern = "."
o=jq.all(pattern, json_data)

# %%
o

# %%
json_data

# %%
pattern = ".RESPONSE.slots[].widget?.data?.products[]?.productInfo?.value"
jq.all(pattern, response.text)

# %%
pattern = ".RESPONSE.slots[].widget?.data?.products[]?.productInfo?.value"
jq.all(pattern, response.json())

# %%
pattern = ".products[]?.productInfo?.value"
jq.all(pattern, response.json())

# %%
pattern = "..products[]?.productInfo?.value"
jq.all(pattern, response.json())

# %%
pattern = ".RESPONSE.slots[].widget?.data?.products[]?.productInfo?.value"
o=jq.all(pattern, response.json())

# %%
o[0]

# %%
pattern = "..|.data?.products[]?.productInfo?.value"
jq.all(pattern, response.json())

# %%
pattern = ".. | .data.products[]?.productInfo?.value"
jq.all(pattern, response.json())

# %%
pattern = ".. | .data.products[].productInfo.value"
jq.all(pattern, response.json())

# %%
pattern = ".. | .data.products[]?.productInfo?.value"
jq.all(pattern, response.json())

# %%
pattern = ".. | .widget.data.products[]?.productInfo?.value"
jq.all(pattern, response.json())

# %%
pattern = ".. | .slots[].widget?.data?.products[]?.productInfo?.value"
jq.all(pattern, response.json())

# %%
response.text

# %%
print(response.text)

# %%
pattern = ".. | .slots[]"
jq.all(pattern, response.json())

# %%
pattern = ".. | .slots[]?"
jq.all(pattern, response.json())

# %%
o

# %%
o[0]
    

# %%
s[0].json()

# %%
o[0].json()

# %%
o[0]

# %%
o[0]['type']

# %%
import json
with open('ofutput.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

# %%
import json
with open('ofutput.json', 'w') as json_file:
    json.dump(o[0], json_file, indent=4)

# %% [markdown]
# Connected to Python 3.11.8

# %% [markdown]
# No kernel connected

# %% [markdown]
# Connected to Python 3.11.8

# %%
ok

# %%
from curl_cffi import requests

# %%
from datetime import date
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
import csv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
os.chdir('C:/Users/ASUS/Downloads/Win_665004_chrome-win/chrome-win')
current_date = str(date.today())
current_time = str(datetime.now().time())


# %%
import json
import pandas as pd

# Read the JSON file
with open('../../463298317_black.json', 'r') as file:
    data = json.load(file)


# %%
product_info = json.loads(data)

# %%
data

# %%
print("hasattr")

# %%
options1=webdriver.ChromeOptions()
options1.binary_location="./chrome.exe";
options1.add_argument("--no-sandbox")


# %%
driver=webdriver.Chrome(options=options1)
driver.maximize_window()


# %%
driver.get('https://myntra.com')


# %%
driver.get('https://www.myntra.com/trousers/campus+sutra/campus-sutra-men-comfort-loose-fit-easy-wash-trousers/30464012/buy')


# %%
ux=driver.page_source

# %%
driver.get('https://www.myntra.com/swimwear/haute+sauce+by++campus+sutra/haute-sauce-by--campus-sutra-women-pink-solid-swimsuit/20686098/buy')


# %%
uy=driver.page_source

# %%
driver.close()

# %%
print(data['brickName'])

# %%
print(','.join([x['scDisplaySize'] for x in c if x['stock']['stockLevelStatus']=="outOfStock"]))

# %%
print(','.join([x['scDisplaySize'] for x in data if x['stock']['stockLevelStatus']=="outOfStock"]))

# %%
print(','.join([x['scDisplaySize'] for x in data['variantOptions'] if x['stock']['stockLevelStatus']=="outOfStock"]))

# %%
print(','.join([x['scDisplaySize'] for x in data['variantOptions'] if x['stock']['stockLevelStatus']=="inStock"]))

# %%
print(','.join([x['scDisplaySize'] for x in data['variantOptions'] ))

# %%
print(','.join(x['scDisplaySize'] for x in data['variantOptions'] ))

# %%
print(data['ratingsResponse']['aggregateRating']['numUserRatings'])

# %%
product_info=data
def extract_size_info(variant):
    return {
        'size': variant['variantOptionQualifiers'][3]['value'],
        'balance_stock': variant['stock']['stockLevel'],
        'Stock_Status': variant['stock']['stockLevelStatus']
    }

# Extract common product information
brand = product_info['brandName']
name = product_info['name']
category = product_info['brickName']
selling_price = product_info['price']['value']
mrp = product_info['wasPriceData']['value']
rating = product_info['ratingsResponse']['aggregateRating']['averageRating']
number_of_ratings = product_info['ratingsResponse']['aggregateRating']['numUserRatings']

# Extract size-specific information
size_info = [extract_size_info(variant) for variant in product_info['variantOptions']]

# Create a list of dictionaries for each size variant
product_data = []
for size_variant in size_info:
    product_data.append({
        'Brand': brand,
        'Name': name,
        'Category': category,
        'Selling Price': selling_price,
        'MRP': mrp,
        'size': size_variant['size'],
        'rating': rating,
        'number_of_ratings': number_of_ratings,
        'balance_stock': size_variant['balance_stock'],
        'Stock_Status': size_variant['Stock_Status']
    })

# Create a pandas DataFrame
df = pd.DataFrame(product_data)

# Display the DataFrame
print(df)


# %%
df.head()

# %%
len(df)

# %%
df.to_clipboard()

# %%
product_info=data
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

# Extract size-specific information
size_info = [extract_size_info(variant) for variant in product_info['variantOptions']]

# Create a list of dictionaries for each size variant
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

# Create a pandas DataFrame
df = pd.DataFrame(product_data)

# Display the DataFrame
print(df)


# %%
import json
import pandas as pd

# Read the JSON file
with open('../../466637319_blue.json', 'r') as file:
    data = json.load(file)


# %%
product_info = json.loads(data)

# %%
product_info=data

# %%
product_info=data
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

# Extract size-specific information
size_info = [extract_size_info(variant) for variant in product_info['variantOptions']]

# Create a list of dictionaries for each size variant
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

# Create a pandas DataFrame
df = pd.DataFrame(product_data)

# Display the DataFrame
print(df)


# %%
df.to_clipboard()


#%%
from curl_cffi import requests  
data = requests.get('https://www.ajio.com/api/p/466637319_blue', headers=headers2)

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
#%%
data = requests.get('https://www.myntra.com/trousers/campus+sutra/campus-sutra-men-comfort-loose-fit-easy-wash-trousers/30464012/buy', headers=headers2)
#%%
from bs4 import BeautifulSoup
import json
import pandas as pd

# Assuming the HTML content is stored in a variable called 'html_content'
soup = BeautifulSoup(html_content, 'html.parser')

# Find the script tag containing the product information
script_tag = soup.find('script', string=lambda text: text and 'window.__myx' in text)

# Extract the JSON data from the script tag
json_data = script_tag.string.split('window.__myx = ')[1].strip(';')

# Parse the JSON data
data = json.loads(json_data)

# Extract the required information
product_data = data['pdpData']

features = {
    'title': product_data['name'],
    'in_stock': any(size['available'] for size in product_data['sizes']),
    'url': f"https://www.myntra.com/{product_data['landingPageUrl']}",
    'mrp': product_data['mrp'],
    'offer_price': product_data['price']['discounted'],
    'category': product_data['analytics']['subCategory'],
    'subcategory': product_data['analytics']['articleType'],
    'supercategory': product_data['analytics']['masterCategory'],
    'id': product_data['id']
}

# Create a DataFrame
result = pd.DataFrame([features])

print(result)
#%%

from bs4 import BeautifulSoup
import json
import pandas as pd
data = requests.get('https://www.myntra.com/trousers/campus+sutra/campus-sutra-men-comfort-loose-fit-easy-wash-trousers/30464012/buy', headers=headers2)
html_content=data.text
# Assuming the HTML content is stored in a variable called 'html_content'
soup = BeautifulSoup(html_content, 'html.parser')

# Find the script tag containing the product information
script_tag = soup.find('script', text=lambda t: t and 'window.__myx' in t)

# Extract the JSON data
json_text = script_tag.string.split('window.__myx = ', 1)[1].rsplit(';', 1)[0]
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
