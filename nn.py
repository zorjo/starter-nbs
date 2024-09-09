#%%
import requests

headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.google-analytics.com/analytics.js', headers=headers)


cookies = {
    'at': 'ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWWpNeFkySm1NelF0TkdOaFpTMHhNV1ZtTFRreVlqZ3RNV1ZsTmpjd1pXTTVabUk1SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzTXpjM01ERTROamdzSW1semN5STZJa2xFUlVFaWZRLjcyUTBZczRVNFdjT09zaEhuQnNlRWRTb3pHS01oR2c3VDhHSEwyUkpiaFk=',
    '_d_id': '4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb',
    'mynt-eupv': '1',
    'x-mynt-pca': 'nH9mxtXUPchmnWDGbhXl9jaw-c5Vja_ovNGyjLbpRsDQIkl7OflPowdK8z8pxlicfpTpLHNuswY89SAkZ0oVceg_fRX_GCoVljGV-NLrKDUCeGRNSpaf2XMnYzvBI24aQdwXtGc0zx9tzATRW3LlN5Xa3EcQmrjYx43Q1R_Vq_62sBgai-E%3D',
    'bm_so': 'E109E85282B2EDF1E26153975A59FFAE6442F951FCDF85BE3175DFB4A8619B05~YAAQjInTFxWXr+6QAQAAo+S4DwAdc9vA9ij+VOThLf5JjS+2IBvz3pawfnK2IGki5GdnWZSQsV3yw+HzZHRTU3HJYmEurWPNcsyJksBpzqx3457t8JX3fMu6OxWXA2mXues2Wwk1YluQ3wEKAw5EQ0Gb9dR12AS8lmuCLc27fEO3+bexdUiAX7r4nX8IBbpC/5INTge4ATgv3Ice6RdaSEyNtWZEi2Z8fxeJHV+3c8oegRxZrRoRBm7qDofm04Yrb7gfva9XsDrl2KdpaJBfeqdq+ZIyis5yVp/zFi7lgS7WANCyJtyeIEOmAwQx5G+rNtDVeWxd+3vO2jehD2zUqd7vAcViY1QqeTzepwEYtOhmvJ/UDV1xa8j7q0RXEiixSp/E6PaQPdKHEJR5y9pXrcAwpDJ3THXu6gMwGPkydnP+OqGeas+GmEj4XgdtaRv4XMEv95ceiG00EEmNSM0PYiRYbs3lcZ8Ib8KBdpWp6Umj+kqybg+YX2SK/YelbJegMzc2lMP7KP7FC3D+zRkEzorndI1DsnF+xaSK4n7iVtDw7h/40F7uurWe9Ghu0BVyByc9fvlm6CVo5oNdBy5/Zho=',
    'bm_s': 'YAAQjInTF1GXr+6QAQAArum4DwEmTXiC/UubYUGVeSPuoiawy6zYxDOj6JWJqHzFv7povcf4HGVn/8vP8IqyBNpmdWfYBlX4NWKyLaT6z4fj5Vg2EnXcgMFxxsu16JbKW+6G80UKk4M1wlgN8140UND2Eq7/C+BwJdMgsmj3xW2yYx2HNoOBhiFRyMGxkNIYh6rhkj9oiGpY0KHVYA3Yd348IMcKPrwhiDhYs5WaRyecbvu69jP67grpKRKMGbhfjd3zvz+8nrvjC3nVpId+QHtwjL0zvxS0KpKRttrS2Fva8w5LELnC8uO8eIwFQDqGc4z5EdPfldJJ0T+lfCn7bho8FSqJzA==',
    'mynt-ulc-api': 'pincode%3A700028',
    '_abck': 'FA360452C255EDEFEF91C657BB89268A~0~YAAQMTXZFzx3ev6QAQAAZ5EWEgxHmf788Nrszbjhk4pmzdsCg+nlkFRyIrUOZrPQ/ZsTcxV0Kh3tAlsj/PnmZIXTtq+nwgKqkWBOfvF5eTel7vA6vtW7/vdFR1zwGqrBJLUhALDtJofrJOjVJr/sB+cSYBJ9zpQT+5qjH0Rr525Fxgvtn4qf1EI6KPIZXzKAVbGPgsAUHaAIyHON/IG39v5E/NMAFEtvbUjOQHip+qC4lc94j3Z308VtRu8VWxnZLbtifDyrzqRNI1zYGi1Of9xgupExd265LO3fnPgEBL1JYrWogfwmBKLPaKvO2rJIRdFXvM6RY8pPfSDmj1iIOLjfp6CL+2QiOHauH8M8w5WDn6QjmKDaOaGD3kbjxScMQxFCbQBldDa7Wy76MbvfYe02iPRy5ZLN~-1~-1~-1',
    '_xsrf': 'EwrqylFLgZ3GKp1TLkoO3w5dAXPZkifN',
    'mynt-loc-src': 'expiry%3A1722586796342%7Csource%3AIP',
    '_mxab_': 'config.bucket%3Dregular%3BConvenience_fee_logged_out_user%3Denabled%3Bhpmweb.mycoupons.revamp%3DRevamp_ver1%3Bcoupon.cart.channelAware%3DchannelAware_Enabled%3Bdesktop.pla%3Denabled',
    '_pv': 'default',
    'dp': 'd',
    'utm_track_v1': '%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1722594941%2C%22trackend%22%3A1722595001%7D',
    'lt_timeout': '1',
    'lt_session': '1',
    'utrid': 'CwpbF3xgQFV2SWdWSAlAMCMzOTUzMjAwODYzJDI%3D.7b80dcf6c1f08d6e88c563dfc5e1f04e',
    'ak_bmsc': 'BF2EDE66000C6058D5751985832A7489~000000000000000000000000000000~YAAQnonTF4YV/QWRAQAAZ9uoEhi5FSb9qYX0FMl1P6dwxEYr1vtIKJtpAkP6L3k9mjt8+xsPfdCb2TzO1C4JVGCPRm4RJwb9s93fQFoRDNHnwrcgq8bV/RrrELq9HyEPNLTByAPuoKJ7iWwGBl4MzEc8Fgdm8qnA4zH81ZP5fRNgiY/zWIF8h7mCJ0Pp4iDV5JceoMBoJZw/V88AJlUG4IFxYcokaTNdirEeZISzJXADtxrve1az7R/F7r2lMrX2X2w7ECKHR+ox1mpEECPtRiu2T1D+xt4nPCGjSRqKEis4vJMrWZsegR6i0oKzwbpaBuVA7OHMS7/Q5exXJhUyrua6XY0OpwzbzMcJqKkXUSRL65RGk9dhJeJZ5qoD+SZp9FIXxOA2HNFuz70=',
    'bm_sz': '8A68F248AAC0E85AA8CBA64AEB42542F~YAAQnonTF4gV/QWRAQAAZ9uoEhhzYCajhFTVMfYG2xdwa3UFFUeB941H6k70xIp79KP5PuM+vjY9ZBgPFVUneKmHLbs8gNLHzi6efot2P4A0sKa9mxwkqtjip9pA33geC5q73nQjtlkL3J/Rngodxlg/SaotGa4JAqkHAhlAeyqiGcCaIsXm8VvWrd90qopsqMsGzknflipTGfhCyCJfyvnOXseQnkCY7MxCp0no5/iwwkf3H05tLVT2eL2LbflyxGiSSx5Dv5T3Xe7c7UV2o8vW1lX69iAlH33mlcDvBgBWJFyQHdDh1d3DDykXItWhfvc2PYGppYnnV807K/lQelRJSlckowHp+g4MG1omssiJ57szPQsaWxpjeRPSHY57OBEyRGIU71gW/D5r98DwPXGZnss5t50VJT0=~4469045~4403522',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'at=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWWpNeFkySm1NelF0TkdOaFpTMHhNV1ZtTFRreVlqZ3RNV1ZsTmpjd1pXTTVabUk1SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzTXpjM01ERTROamdzSW1semN5STZJa2xFUlVFaWZRLjcyUTBZczRVNFdjT09zaEhuQnNlRWRTb3pHS01oR2c3VDhHSEwyUkpiaFk=; _d_id=4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb; mynt-eupv=1; x-mynt-pca=nH9mxtXUPchmnWDGbhXl9jaw-c5Vja_ovNGyjLbpRsDQIkl7OflPowdK8z8pxlicfpTpLHNuswY89SAkZ0oVceg_fRX_GCoVljGV-NLrKDUCeGRNSpaf2XMnYzvBI24aQdwXtGc0zx9tzATRW3LlN5Xa3EcQmrjYx43Q1R_Vq_62sBgai-E%3D; bm_so=E109E85282B2EDF1E26153975A59FFAE6442F951FCDF85BE3175DFB4A8619B05~YAAQjInTFxWXr+6QAQAAo+S4DwAdc9vA9ij+VOThLf5JjS+2IBvz3pawfnK2IGki5GdnWZSQsV3yw+HzZHRTU3HJYmEurWPNcsyJksBpzqx3457t8JX3fMu6OxWXA2mXues2Wwk1YluQ3wEKAw5EQ0Gb9dR12AS8lmuCLc27fEO3+bexdUiAX7r4nX8IBbpC/5INTge4ATgv3Ice6RdaSEyNtWZEi2Z8fxeJHV+3c8oegRxZrRoRBm7qDofm04Yrb7gfva9XsDrl2KdpaJBfeqdq+ZIyis5yVp/zFi7lgS7WANCyJtyeIEOmAwQx5G+rNtDVeWxd+3vO2jehD2zUqd7vAcViY1QqeTzepwEYtOhmvJ/UDV1xa8j7q0RXEiixSp/E6PaQPdKHEJR5y9pXrcAwpDJ3THXu6gMwGPkydnP+OqGeas+GmEj4XgdtaRv4XMEv95ceiG00EEmNSM0PYiRYbs3lcZ8Ib8KBdpWp6Umj+kqybg+YX2SK/YelbJegMzc2lMP7KP7FC3D+zRkEzorndI1DsnF+xaSK4n7iVtDw7h/40F7uurWe9Ghu0BVyByc9fvlm6CVo5oNdBy5/Zho=; bm_s=YAAQjInTF1GXr+6QAQAArum4DwEmTXiC/UubYUGVeSPuoiawy6zYxDOj6JWJqHzFv7povcf4HGVn/8vP8IqyBNpmdWfYBlX4NWKyLaT6z4fj5Vg2EnXcgMFxxsu16JbKW+6G80UKk4M1wlgN8140UND2Eq7/C+BwJdMgsmj3xW2yYx2HNoOBhiFRyMGxkNIYh6rhkj9oiGpY0KHVYA3Yd348IMcKPrwhiDhYs5WaRyecbvu69jP67grpKRKMGbhfjd3zvz+8nrvjC3nVpId+QHtwjL0zvxS0KpKRttrS2Fva8w5LELnC8uO8eIwFQDqGc4z5EdPfldJJ0T+lfCn7bho8FSqJzA==; mynt-ulc-api=pincode%3A700028; _abck=FA360452C255EDEFEF91C657BB89268A~0~YAAQMTXZFzx3ev6QAQAAZ5EWEgxHmf788Nrszbjhk4pmzdsCg+nlkFRyIrUOZrPQ/ZsTcxV0Kh3tAlsj/PnmZIXTtq+nwgKqkWBOfvF5eTel7vA6vtW7/vdFR1zwGqrBJLUhALDtJofrJOjVJr/sB+cSYBJ9zpQT+5qjH0Rr525Fxgvtn4qf1EI6KPIZXzKAVbGPgsAUHaAIyHON/IG39v5E/NMAFEtvbUjOQHip+qC4lc94j3Z308VtRu8VWxnZLbtifDyrzqRNI1zYGi1Of9xgupExd265LO3fnPgEBL1JYrWogfwmBKLPaKvO2rJIRdFXvM6RY8pPfSDmj1iIOLjfp6CL+2QiOHauH8M8w5WDn6QjmKDaOaGD3kbjxScMQxFCbQBldDa7Wy76MbvfYe02iPRy5ZLN~-1~-1~-1; _xsrf=EwrqylFLgZ3GKp1TLkoO3w5dAXPZkifN; mynt-loc-src=expiry%3A1722586796342%7Csource%3AIP; _mxab_=config.bucket%3Dregular%3BConvenience_fee_logged_out_user%3Denabled%3Bhpmweb.mycoupons.revamp%3DRevamp_ver1%3Bcoupon.cart.channelAware%3DchannelAware_Enabled%3Bdesktop.pla%3Denabled; _pv=default; dp=d; utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1722594941%2C%22trackend%22%3A1722595001%7D; lt_timeout=1; lt_session=1; utrid=CwpbF3xgQFV2SWdWSAlAMCMzOTUzMjAwODYzJDI%3D.7b80dcf6c1f08d6e88c563dfc5e1f04e; ak_bmsc=BF2EDE66000C6058D5751985832A7489~000000000000000000000000000000~YAAQnonTF4YV/QWRAQAAZ9uoEhi5FSb9qYX0FMl1P6dwxEYr1vtIKJtpAkP6L3k9mjt8+xsPfdCb2TzO1C4JVGCPRm4RJwb9s93fQFoRDNHnwrcgq8bV/RrrELq9HyEPNLTByAPuoKJ7iWwGBl4MzEc8Fgdm8qnA4zH81ZP5fRNgiY/zWIF8h7mCJ0Pp4iDV5JceoMBoJZw/V88AJlUG4IFxYcokaTNdirEeZISzJXADtxrve1az7R/F7r2lMrX2X2w7ECKHR+ox1mpEECPtRiu2T1D+xt4nPCGjSRqKEis4vJMrWZsegR6i0oKzwbpaBuVA7OHMS7/Q5exXJhUyrua6XY0OpwzbzMcJqKkXUSRL65RGk9dhJeJZ5qoD+SZp9FIXxOA2HNFuz70=; bm_sz=8A68F248AAC0E85AA8CBA64AEB42542F~YAAQnonTF4gV/QWRAQAAZ9uoEhhzYCajhFTVMfYG2xdwa3UFFUeB941H6k70xIp79KP5PuM+vjY9ZBgPFVUneKmHLbs8gNLHzi6efot2P4A0sKa9mxwkqtjip9pA33geC5q73nQjtlkL3J/Rngodxlg/SaotGa4JAqkHAhlAeyqiGcCaIsXm8VvWrd90qopsqMsGzknflipTGfhCyCJfyvnOXseQnkCY7MxCp0no5/iwwkf3H05tLVT2eL2LbflyxGiSSx5Dv5T3Xe7c7UV2o8vW1lX69iAlH33mlcDvBgBWJFyQHdDh1d3DDykXItWhfvc2PYGppYnnV807K/lQelRJSlckowHp+g4MG1omssiJ57szPQsaWxpjeRPSHY57OBEyRGIU71gW/D5r98DwPXGZnss5t50VJT0=~4469045~4403522',
    'if-modified-since': 'Mon, 17 Jun 2024 15:55:06 GMT',
    'if-none-match': '"1f69d09e768baf873eebed81b22ee2ffbcc4fac7f176256cef9760efd540bc7b"',
    'priority': 'u=1',
    'referer': 'https://www.myntra.com/campussutra?f=Brand%3ACampus%20Sutra',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://www.myntra.com/7glfrb3jrnIFV0l9oGD1v5vL/uXmarmbc4NXGD5G3/EHwtRzUrGAU/VSE2HU/o_RyQ',
    cookies=cookies,
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.myntra.com/campussutra?f=Brand%3ACampus%20Sutra',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.myntra.com/_sec/cp_challenge/sec-4-5.css', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.myntra.com/campussutra?f=Brand%3ACampus%20Sutra',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.myntra.com/_sec/cp_challenge/sec-cpt-4-5.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://s.go-mpulse.net/boomerang/5HGF9-8HWNR-5RKQC-BB2LE-73DQ7', headers=headers)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

params = {
    'secret': 'n60cv4',
}


headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'if-none-match': 'W/"20-0p7d/hKnBoc+Poaa+PpZC+j15qs"',
    'priority': 'u=2',
    'referer': 'https://www.myntra.com/campussutra?f=Brand%3ACampus%20Sutra',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'manifest',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

response = requests.get('https://www.myntra.com/manifest.json', headers=headers)
#%%

cookies = {
    'at': 'ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWWpNeFkySm1NelF0TkdOaFpTMHhNV1ZtTFRreVlqZ3RNV1ZsTmpjd1pXTTVabUk1SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzTXpjM01ERTROamdzSW1semN5STZJa2xFUlVFaWZRLjcyUTBZczRVNFdjT09zaEhuQnNlRWRTb3pHS01oR2c3VDhHSEwyUkpiaFk=',
    '_d_id': '4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb',
    'mynt-eupv': '1',
    'x-mynt-pca': 'nH9mxtXUPchmnWDGbhXl9jaw-c5Vja_ovNGyjLbpRsDQIkl7OflPowdK8z8pxlicfpTpLHNuswY89SAkZ0oVceg_fRX_GCoVljGV-NLrKDUCeGRNSpaf2XMnYzvBI24aQdwXtGc0zx9tzATRW3LlN5Xa3EcQmrjYx43Q1R_Vq_62sBgai-E%3D',
    'bm_so': 'E109E85282B2EDF1E26153975A59FFAE6442F951FCDF85BE3175DFB4A8619B05~YAAQjInTFxWXr+6QAQAAo+S4DwAdc9vA9ij+VOThLf5JjS+2IBvz3pawfnK2IGki5GdnWZSQsV3yw+HzZHRTU3HJYmEurWPNcsyJksBpzqx3457t8JX3fMu6OxWXA2mXues2Wwk1YluQ3wEKAw5EQ0Gb9dR12AS8lmuCLc27fEO3+bexdUiAX7r4nX8IBbpC/5INTge4ATgv3Ice6RdaSEyNtWZEi2Z8fxeJHV+3c8oegRxZrRoRBm7qDofm04Yrb7gfva9XsDrl2KdpaJBfeqdq+ZIyis5yVp/zFi7lgS7WANCyJtyeIEOmAwQx5G+rNtDVeWxd+3vO2jehD2zUqd7vAcViY1QqeTzepwEYtOhmvJ/UDV1xa8j7q0RXEiixSp/E6PaQPdKHEJR5y9pXrcAwpDJ3THXu6gMwGPkydnP+OqGeas+GmEj4XgdtaRv4XMEv95ceiG00EEmNSM0PYiRYbs3lcZ8Ib8KBdpWp6Umj+kqybg+YX2SK/YelbJegMzc2lMP7KP7FC3D+zRkEzorndI1DsnF+xaSK4n7iVtDw7h/40F7uurWe9Ghu0BVyByc9fvlm6CVo5oNdBy5/Zho=',
    'bm_s': 'YAAQjInTF1GXr+6QAQAArum4DwEmTXiC/UubYUGVeSPuoiawy6zYxDOj6JWJqHzFv7povcf4HGVn/8vP8IqyBNpmdWfYBlX4NWKyLaT6z4fj5Vg2EnXcgMFxxsu16JbKW+6G80UKk4M1wlgN8140UND2Eq7/C+BwJdMgsmj3xW2yYx2HNoOBhiFRyMGxkNIYh6rhkj9oiGpY0KHVYA3Yd348IMcKPrwhiDhYs5WaRyecbvu69jP67grpKRKMGbhfjd3zvz+8nrvjC3nVpId+QHtwjL0zvxS0KpKRttrS2Fva8w5LELnC8uO8eIwFQDqGc4z5EdPfldJJ0T+lfCn7bho8FSqJzA==',
    'mynt-ulc-api': 'pincode%3A700028',
    '_abck': 'FA360452C255EDEFEF91C657BB89268A~0~YAAQMTXZFzx3ev6QAQAAZ5EWEgxHmf788Nrszbjhk4pmzdsCg+nlkFRyIrUOZrPQ/ZsTcxV0Kh3tAlsj/PnmZIXTtq+nwgKqkWBOfvF5eTel7vA6vtW7/vdFR1zwGqrBJLUhALDtJofrJOjVJr/sB+cSYBJ9zpQT+5qjH0Rr525Fxgvtn4qf1EI6KPIZXzKAVbGPgsAUHaAIyHON/IG39v5E/NMAFEtvbUjOQHip+qC4lc94j3Z308VtRu8VWxnZLbtifDyrzqRNI1zYGi1Of9xgupExd265LO3fnPgEBL1JYrWogfwmBKLPaKvO2rJIRdFXvM6RY8pPfSDmj1iIOLjfp6CL+2QiOHauH8M8w5WDn6QjmKDaOaGD3kbjxScMQxFCbQBldDa7Wy76MbvfYe02iPRy5ZLN~-1~-1~-1',
    '_xsrf': 'EwrqylFLgZ3GKp1TLkoO3w5dAXPZkifN',
    'mynt-loc-src': 'expiry%3A1722586796342%7Csource%3AIP',
    '_mxab_': 'config.bucket%3Dregular%3BConvenience_fee_logged_out_user%3Denabled%3Bhpmweb.mycoupons.revamp%3DRevamp_ver1%3Bcoupon.cart.channelAware%3DchannelAware_Enabled%3Bdesktop.pla%3Denabled',
    '_pv': 'default',
    'dp': 'd',
    'utm_track_v1': '%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1722594941%2C%22trackend%22%3A1722595001%7D',
    'lt_timeout': '1',
    'lt_session': '1',
    'ak_bmsc': 'BF2EDE66000C6058D5751985832A7489~000000000000000000000000000000~YAAQnonTF4YV/QWRAQAAZ9uoEhi5FSb9qYX0FMl1P6dwxEYr1vtIKJtpAkP6L3k9mjt8+xsPfdCb2TzO1C4JVGCPRm4RJwb9s93fQFoRDNHnwrcgq8bV/RrrELq9HyEPNLTByAPuoKJ7iWwGBl4MzEc8Fgdm8qnA4zH81ZP5fRNgiY/zWIF8h7mCJ0Pp4iDV5JceoMBoJZw/V88AJlUG4IFxYcokaTNdirEeZISzJXADtxrve1az7R/F7r2lMrX2X2w7ECKHR+ox1mpEECPtRiu2T1D+xt4nPCGjSRqKEis4vJMrWZsegR6i0oKzwbpaBuVA7OHMS7/Q5exXJhUyrua6XY0OpwzbzMcJqKkXUSRL65RGk9dhJeJZ5qoD+SZp9FIXxOA2HNFuz70=',
    'bm_sz': '8A68F248AAC0E85AA8CBA64AEB42542F~YAAQnonTF4gV/QWRAQAAZ9uoEhhzYCajhFTVMfYG2xdwa3UFFUeB941H6k70xIp79KP5PuM+vjY9ZBgPFVUneKmHLbs8gNLHzi6efot2P4A0sKa9mxwkqtjip9pA33geC5q73nQjtlkL3J/Rngodxlg/SaotGa4JAqkHAhlAeyqiGcCaIsXm8VvWrd90qopsqMsGzknflipTGfhCyCJfyvnOXseQnkCY7MxCp0no5/iwwkf3H05tLVT2eL2LbflyxGiSSx5Dv5T3Xe7c7UV2o8vW1lX69iAlH33mlcDvBgBWJFyQHdDh1d3DDykXItWhfvc2PYGppYnnV807K/lQelRJSlckowHp+g4MG1omssiJ57szPQsaWxpjeRPSHY57OBEyRGIU71gW/D5r98DwPXGZnss5t50VJT0=~4469045~4403522',
    'utrid': 'aW0JfUUdZxlQFV5SY09AMCM4NTA5NTM5OTgkMg%3D%3D.9a2f4c94150c0d61126fdbe31391799c',
    'bm_mi': 'E1C38B8B15A4FF2ACA93FED9E88819B2~YAAQnonTF7MW/QWRAQAAROGoEhjeEpFIKC/ckJxmhCFrdKEGEM8x+ml649lEhFpa+uqxRlqZ0lJfteKZJtwJ1KU1ilk+wtuGtLcDbP+qXGFbodm1L4/UyIYMB+qnSxAnezRYAZTOEphoIyfNQj6iRT7jfBtDzhQJHQicF2Jexsmh4LpKL/Fd/kJyGjyfTqFN+yp7zOyFCs4eaY+gWiCPe2KjbgZbFaI2/p3BnpKFygGFPYwFwYj5Sde6PJW/3gIEMH4ZK9A4yaVwcipNDoDL2LBsuWnMTmBx9UaGOEN02lRbXv8tqeQ/u9Lo2iq0vIxlPOumtJX6IEWYIOmvzqyImd/R6Tfv0AVv3jK3Qu0TUFDsQg==~1',
    'bm_sv': '562DEBB8644A469B2AF626405AE8728C~YAAQnonTF7QW/QWRAQAAROGoEhiOFpHDo3V5R0xzmd1yBN3x4iIvp5YEHue+3zzDnSUk0rENb2ORma3QV93sEg8xN/itvA8yUkX05lxaTB1Bp/n4wyI/i70hmpo5nWgwRdwt7RWwIOQR3eyPCJmxqFwOF8tMjlAnEO9EszzEMTwrluaXC8OSfQpTDfZs+l88HagnPLxe82+YAYPxpZYGiBzdB9Xgedzj+wbm1ImFYBwnwmrtdK0wCTg7nbSrzU14~1',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    # 'cookie': 'at=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWWpNeFkySm1NelF0TkdOaFpTMHhNV1ZtTFRreVlqZ3RNV1ZsTmpjd1pXTTVabUk1SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzTXpjM01ERTROamdzSW1semN5STZJa2xFUlVFaWZRLjcyUTBZczRVNFdjT09zaEhuQnNlRWRTb3pHS01oR2c3VDhHSEwyUkpiaFk=; _d_id=4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb; mynt-eupv=1; x-mynt-pca=nH9mxtXUPchmnWDGbhXl9jaw-c5Vja_ovNGyjLbpRsDQIkl7OflPowdK8z8pxlicfpTpLHNuswY89SAkZ0oVceg_fRX_GCoVljGV-NLrKDUCeGRNSpaf2XMnYzvBI24aQdwXtGc0zx9tzATRW3LlN5Xa3EcQmrjYx43Q1R_Vq_62sBgai-E%3D; bm_so=E109E85282B2EDF1E26153975A59FFAE6442F951FCDF85BE3175DFB4A8619B05~YAAQjInTFxWXr+6QAQAAo+S4DwAdc9vA9ij+VOThLf5JjS+2IBvz3pawfnK2IGki5GdnWZSQsV3yw+HzZHRTU3HJYmEurWPNcsyJksBpzqx3457t8JX3fMu6OxWXA2mXues2Wwk1YluQ3wEKAw5EQ0Gb9dR12AS8lmuCLc27fEO3+bexdUiAX7r4nX8IBbpC/5INTge4ATgv3Ice6RdaSEyNtWZEi2Z8fxeJHV+3c8oegRxZrRoRBm7qDofm04Yrb7gfva9XsDrl2KdpaJBfeqdq+ZIyis5yVp/zFi7lgS7WANCyJtyeIEOmAwQx5G+rNtDVeWxd+3vO2jehD2zUqd7vAcViY1QqeTzepwEYtOhmvJ/UDV1xa8j7q0RXEiixSp/E6PaQPdKHEJR5y9pXrcAwpDJ3THXu6gMwGPkydnP+OqGeas+GmEj4XgdtaRv4XMEv95ceiG00EEmNSM0PYiRYbs3lcZ8Ib8KBdpWp6Umj+kqybg+YX2SK/YelbJegMzc2lMP7KP7FC3D+zRkEzorndI1DsnF+xaSK4n7iVtDw7h/40F7uurWe9Ghu0BVyByc9fvlm6CVo5oNdBy5/Zho=; bm_s=YAAQjInTF1GXr+6QAQAArum4DwEmTXiC/UubYUGVeSPuoiawy6zYxDOj6JWJqHzFv7povcf4HGVn/8vP8IqyBNpmdWfYBlX4NWKyLaT6z4fj5Vg2EnXcgMFxxsu16JbKW+6G80UKk4M1wlgN8140UND2Eq7/C+BwJdMgsmj3xW2yYx2HNoOBhiFRyMGxkNIYh6rhkj9oiGpY0KHVYA3Yd348IMcKPrwhiDhYs5WaRyecbvu69jP67grpKRKMGbhfjd3zvz+8nrvjC3nVpId+QHtwjL0zvxS0KpKRttrS2Fva8w5LELnC8uO8eIwFQDqGc4z5EdPfldJJ0T+lfCn7bho8FSqJzA==; mynt-ulc-api=pincode%3A700028; _abck=FA360452C255EDEFEF91C657BB89268A~0~YAAQMTXZFzx3ev6QAQAAZ5EWEgxHmf788Nrszbjhk4pmzdsCg+nlkFRyIrUOZrPQ/ZsTcxV0Kh3tAlsj/PnmZIXTtq+nwgKqkWBOfvF5eTel7vA6vtW7/vdFR1zwGqrBJLUhALDtJofrJOjVJr/sB+cSYBJ9zpQT+5qjH0Rr525Fxgvtn4qf1EI6KPIZXzKAVbGPgsAUHaAIyHON/IG39v5E/NMAFEtvbUjOQHip+qC4lc94j3Z308VtRu8VWxnZLbtifDyrzqRNI1zYGi1Of9xgupExd265LO3fnPgEBL1JYrWogfwmBKLPaKvO2rJIRdFXvM6RY8pPfSDmj1iIOLjfp6CL+2QiOHauH8M8w5WDn6QjmKDaOaGD3kbjxScMQxFCbQBldDa7Wy76MbvfYe02iPRy5ZLN~-1~-1~-1; _xsrf=EwrqylFLgZ3GKp1TLkoO3w5dAXPZkifN; mynt-loc-src=expiry%3A1722586796342%7Csource%3AIP; _mxab_=config.bucket%3Dregular%3BConvenience_fee_logged_out_user%3Denabled%3Bhpmweb.mycoupons.revamp%3DRevamp_ver1%3Bcoupon.cart.channelAware%3DchannelAware_Enabled%3Bdesktop.pla%3Denabled; _pv=default; dp=d; utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1722594941%2C%22trackend%22%3A1722595001%7D; lt_timeout=1; lt_session=1; ak_bmsc=BF2EDE66000C6058D5751985832A7489~000000000000000000000000000000~YAAQnonTF4YV/QWRAQAAZ9uoEhi5FSb9qYX0FMl1P6dwxEYr1vtIKJtpAkP6L3k9mjt8+xsPfdCb2TzO1C4JVGCPRm4RJwb9s93fQFoRDNHnwrcgq8bV/RrrELq9HyEPNLTByAPuoKJ7iWwGBl4MzEc8Fgdm8qnA4zH81ZP5fRNgiY/zWIF8h7mCJ0Pp4iDV5JceoMBoJZw/V88AJlUG4IFxYcokaTNdirEeZISzJXADtxrve1az7R/F7r2lMrX2X2w7ECKHR+ox1mpEECPtRiu2T1D+xt4nPCGjSRqKEis4vJMrWZsegR6i0oKzwbpaBuVA7OHMS7/Q5exXJhUyrua6XY0OpwzbzMcJqKkXUSRL65RGk9dhJeJZ5qoD+SZp9FIXxOA2HNFuz70=; bm_sz=8A68F248AAC0E85AA8CBA64AEB42542F~YAAQnonTF4gV/QWRAQAAZ9uoEhhzYCajhFTVMfYG2xdwa3UFFUeB941H6k70xIp79KP5PuM+vjY9ZBgPFVUneKmHLbs8gNLHzi6efot2P4A0sKa9mxwkqtjip9pA33geC5q73nQjtlkL3J/Rngodxlg/SaotGa4JAqkHAhlAeyqiGcCaIsXm8VvWrd90qopsqMsGzknflipTGfhCyCJfyvnOXseQnkCY7MxCp0no5/iwwkf3H05tLVT2eL2LbflyxGiSSx5Dv5T3Xe7c7UV2o8vW1lX69iAlH33mlcDvBgBWJFyQHdDh1d3DDykXItWhfvc2PYGppYnnV807K/lQelRJSlckowHp+g4MG1omssiJ57szPQsaWxpjeRPSHY57OBEyRGIU71gW/D5r98DwPXGZnss5t50VJT0=~4469045~4403522; utrid=aW0JfUUdZxlQFV5SY09AMCM4NTA5NTM5OTgkMg%3D%3D.9a2f4c94150c0d61126fdbe31391799c; bm_mi=E1C38B8B15A4FF2ACA93FED9E88819B2~YAAQnonTF7MW/QWRAQAAROGoEhjeEpFIKC/ckJxmhCFrdKEGEM8x+ml649lEhFpa+uqxRlqZ0lJfteKZJtwJ1KU1ilk+wtuGtLcDbP+qXGFbodm1L4/UyIYMB+qnSxAnezRYAZTOEphoIyfNQj6iRT7jfBtDzhQJHQicF2Jexsmh4LpKL/Fd/kJyGjyfTqFN+yp7zOyFCs4eaY+gWiCPe2KjbgZbFaI2/p3BnpKFygGFPYwFwYj5Sde6PJW/3gIEMH4ZK9A4yaVwcipNDoDL2LBsuWnMTmBx9UaGOEN02lRbXv8tqeQ/u9Lo2iq0vIxlPOumtJX6IEWYIOmvzqyImd/R6Tfv0AVv3jK3Qu0TUFDsQg==~1; bm_sv=562DEBB8644A469B2AF626405AE8728C~YAAQnonTF7QW/QWRAQAAROGoEhiOFpHDo3V5R0xzmd1yBN3x4iIvp5YEHue+3zzDnSUk0rENb2ORma3QV93sEg8xN/itvA8yUkX05lxaTB1Bp/n4wyI/i70hmpo5nWgwRdwt7RWwIOQR3eyPCJmxqFwOF8tMjlAnEO9EszzEMTwrluaXC8OSfQpTDfZs+l88HagnPLxe82+YAYPxpZYGiBzdB9Xgedzj+wbm1ImFYBwnwmrtdK0wCTg7nbSrzU14~1',
    'origin': 'https://www.myntra.com',
    'priority': 'u=1, i',
    'referer': 'https://www.myntra.com/campussutra?f=Brand%3ACampus%20Sutra',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-location-context': 'pincode=700028;source=IP',
    'x-meta-app': 'channel=web',
    'x-myntraweb': 'Yes',
    'x-requested-with': 'browser',
}

params = {
    'f': 'Brand:Campus Sutra',
}

json_data = {}

response = requests.post('https://www.myntra.com/beacon/user-data', params=params, cookies=cookies, headers=headers, json=json_data)


cookies = {
    'at': 'ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWWpNeFkySm1NelF0TkdOaFpTMHhNV1ZtTFRreVlqZ3RNV1ZsTmpjd1pXTTVabUk1SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzTXpjM01ERTROamdzSW1semN5STZJa2xFUlVFaWZRLjcyUTBZczRVNFdjT09zaEhuQnNlRWRTb3pHS01oR2c3VDhHSEwyUkpiaFk=',
    '_d_id': '4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb',
    'mynt-eupv': '1',
    'x-mynt-pca': 'nH9mxtXUPchmnWDGbhXl9jaw-c5Vja_ovNGyjLbpRsDQIkl7OflPowdK8z8pxlicfpTpLHNuswY89SAkZ0oVceg_fRX_GCoVljGV-NLrKDUCeGRNSpaf2XMnYzvBI24aQdwXtGc0zx9tzATRW3LlN5Xa3EcQmrjYx43Q1R_Vq_62sBgai-E%3D',
    'bm_so': 'E109E85282B2EDF1E26153975A59FFAE6442F951FCDF85BE3175DFB4A8619B05~YAAQjInTFxWXr+6QAQAAo+S4DwAdc9vA9ij+VOThLf5JjS+2IBvz3pawfnK2IGki5GdnWZSQsV3yw+HzZHRTU3HJYmEurWPNcsyJksBpzqx3457t8JX3fMu6OxWXA2mXues2Wwk1YluQ3wEKAw5EQ0Gb9dR12AS8lmuCLc27fEO3+bexdUiAX7r4nX8IBbpC/5INTge4ATgv3Ice6RdaSEyNtWZEi2Z8fxeJHV+3c8oegRxZrRoRBm7qDofm04Yrb7gfva9XsDrl2KdpaJBfeqdq+ZIyis5yVp/zFi7lgS7WANCyJtyeIEOmAwQx5G+rNtDVeWxd+3vO2jehD2zUqd7vAcViY1QqeTzepwEYtOhmvJ/UDV1xa8j7q0RXEiixSp/E6PaQPdKHEJR5y9pXrcAwpDJ3THXu6gMwGPkydnP+OqGeas+GmEj4XgdtaRv4XMEv95ceiG00EEmNSM0PYiRYbs3lcZ8Ib8KBdpWp6Umj+kqybg+YX2SK/YelbJegMzc2lMP7KP7FC3D+zRkEzorndI1DsnF+xaSK4n7iVtDw7h/40F7uurWe9Ghu0BVyByc9fvlm6CVo5oNdBy5/Zho=',
    'bm_s': 'YAAQjInTF1GXr+6QAQAArum4DwEmTXiC/UubYUGVeSPuoiawy6zYxDOj6JWJqHzFv7povcf4HGVn/8vP8IqyBNpmdWfYBlX4NWKyLaT6z4fj5Vg2EnXcgMFxxsu16JbKW+6G80UKk4M1wlgN8140UND2Eq7/C+BwJdMgsmj3xW2yYx2HNoOBhiFRyMGxkNIYh6rhkj9oiGpY0KHVYA3Yd348IMcKPrwhiDhYs5WaRyecbvu69jP67grpKRKMGbhfjd3zvz+8nrvjC3nVpId+QHtwjL0zvxS0KpKRttrS2Fva8w5LELnC8uO8eIwFQDqGc4z5EdPfldJJ0T+lfCn7bho8FSqJzA==',
    'mynt-ulc-api': 'pincode%3A700028',
    '_abck': 'FA360452C255EDEFEF91C657BB89268A~0~YAAQMTXZFzx3ev6QAQAAZ5EWEgxHmf788Nrszbjhk4pmzdsCg+nlkFRyIrUOZrPQ/ZsTcxV0Kh3tAlsj/PnmZIXTtq+nwgKqkWBOfvF5eTel7vA6vtW7/vdFR1zwGqrBJLUhALDtJofrJOjVJr/sB+cSYBJ9zpQT+5qjH0Rr525Fxgvtn4qf1EI6KPIZXzKAVbGPgsAUHaAIyHON/IG39v5E/NMAFEtvbUjOQHip+qC4lc94j3Z308VtRu8VWxnZLbtifDyrzqRNI1zYGi1Of9xgupExd265LO3fnPgEBL1JYrWogfwmBKLPaKvO2rJIRdFXvM6RY8pPfSDmj1iIOLjfp6CL+2QiOHauH8M8w5WDn6QjmKDaOaGD3kbjxScMQxFCbQBldDa7Wy76MbvfYe02iPRy5ZLN~-1~-1~-1',
    '_xsrf': 'EwrqylFLgZ3GKp1TLkoO3w5dAXPZkifN',
    'mynt-loc-src': 'expiry%3A1722586796342%7Csource%3AIP',
    '_mxab_': 'config.bucket%3Dregular%3BConvenience_fee_logged_out_user%3Denabled%3Bhpmweb.mycoupons.revamp%3DRevamp_ver1%3Bcoupon.cart.channelAware%3DchannelAware_Enabled%3Bdesktop.pla%3Denabled',
    '_pv': 'default',
    'dp': 'd',
    'utm_track_v1': '%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1722594941%2C%22trackend%22%3A1722595001%7D',
    'lt_timeout': '1',
    'lt_session': '1',
    'ak_bmsc': 'BF2EDE66000C6058D5751985832A7489~000000000000000000000000000000~YAAQnonTF4YV/QWRAQAAZ9uoEhi5FSb9qYX0FMl1P6dwxEYr1vtIKJtpAkP6L3k9mjt8+xsPfdCb2TzO1C4JVGCPRm4RJwb9s93fQFoRDNHnwrcgq8bV/RrrELq9HyEPNLTByAPuoKJ7iWwGBl4MzEc8Fgdm8qnA4zH81ZP5fRNgiY/zWIF8h7mCJ0Pp4iDV5JceoMBoJZw/V88AJlUG4IFxYcokaTNdirEeZISzJXADtxrve1az7R/F7r2lMrX2X2w7ECKHR+ox1mpEECPtRiu2T1D+xt4nPCGjSRqKEis4vJMrWZsegR6i0oKzwbpaBuVA7OHMS7/Q5exXJhUyrua6XY0OpwzbzMcJqKkXUSRL65RGk9dhJeJZ5qoD+SZp9FIXxOA2HNFuz70=',
    'bm_sz': '8A68F248AAC0E85AA8CBA64AEB42542F~YAAQnonTF4gV/QWRAQAAZ9uoEhhzYCajhFTVMfYG2xdwa3UFFUeB941H6k70xIp79KP5PuM+vjY9ZBgPFVUneKmHLbs8gNLHzi6efot2P4A0sKa9mxwkqtjip9pA33geC5q73nQjtlkL3J/Rngodxlg/SaotGa4JAqkHAhlAeyqiGcCaIsXm8VvWrd90qopsqMsGzknflipTGfhCyCJfyvnOXseQnkCY7MxCp0no5/iwwkf3H05tLVT2eL2LbflyxGiSSx5Dv5T3Xe7c7UV2o8vW1lX69iAlH33mlcDvBgBWJFyQHdDh1d3DDykXItWhfvc2PYGppYnnV807K/lQelRJSlckowHp+g4MG1omssiJ57szPQsaWxpjeRPSHY57OBEyRGIU71gW/D5r98DwPXGZnss5t50VJT0=~4469045~4403522',
    'utrid': 'aW0JfUUdZxlQFV5SY09AMCM4NTA5NTM5OTgkMg%3D%3D.9a2f4c94150c0d61126fdbe31391799c',
    'bm_mi': 'E1C38B8B15A4FF2ACA93FED9E88819B2~YAAQnonTF7MW/QWRAQAAROGoEhjeEpFIKC/ckJxmhCFrdKEGEM8x+ml649lEhFpa+uqxRlqZ0lJfteKZJtwJ1KU1ilk+wtuGtLcDbP+qXGFbodm1L4/UyIYMB+qnSxAnezRYAZTOEphoIyfNQj6iRT7jfBtDzhQJHQicF2Jexsmh4LpKL/Fd/kJyGjyfTqFN+yp7zOyFCs4eaY+gWiCPe2KjbgZbFaI2/p3BnpKFygGFPYwFwYj5Sde6PJW/3gIEMH4ZK9A4yaVwcipNDoDL2LBsuWnMTmBx9UaGOEN02lRbXv8tqeQ/u9Lo2iq0vIxlPOumtJX6IEWYIOmvzqyImd/R6Tfv0AVv3jK3Qu0TUFDsQg==~1',
    'bm_sv': '562DEBB8644A469B2AF626405AE8728C~YAAQnonTF7QW/QWRAQAAROGoEhiOFpHDo3V5R0xzmd1yBN3x4iIvp5YEHue+3zzDnSUk0rENb2ORma3QV93sEg8xN/itvA8yUkX05lxaTB1Bp/n4wyI/i70hmpo5nWgwRdwt7RWwIOQR3eyPCJmxqFwOF8tMjlAnEO9EszzEMTwrluaXC8OSfQpTDfZs+l88HagnPLxe82+YAYPxpZYGiBzdB9Xgedzj+wbm1ImFYBwnwmrtdK0wCTg7nbSrzU14~1',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'at=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWWpNeFkySm1NelF0TkdOaFpTMHhNV1ZtTFRreVlqZ3RNV1ZsTmpjd1pXTTVabUk1SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzTXpjM01ERTROamdzSW1semN5STZJa2xFUlVFaWZRLjcyUTBZczRVNFdjT09zaEhuQnNlRWRTb3pHS01oR2c3VDhHSEwyUkpiaFk=; _d_id=4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb; mynt-eupv=1; x-mynt-pca=nH9mxtXUPchmnWDGbhXl9jaw-c5Vja_ovNGyjLbpRsDQIkl7OflPowdK8z8pxlicfpTpLHNuswY89SAkZ0oVceg_fRX_GCoVljGV-NLrKDUCeGRNSpaf2XMnYzvBI24aQdwXtGc0zx9tzATRW3LlN5Xa3EcQmrjYx43Q1R_Vq_62sBgai-E%3D; bm_so=E109E85282B2EDF1E26153975A59FFAE6442F951FCDF85BE3175DFB4A8619B05~YAAQjInTFxWXr+6QAQAAo+S4DwAdc9vA9ij+VOThLf5JjS+2IBvz3pawfnK2IGki5GdnWZSQsV3yw+HzZHRTU3HJYmEurWPNcsyJksBpzqx3457t8JX3fMu6OxWXA2mXues2Wwk1YluQ3wEKAw5EQ0Gb9dR12AS8lmuCLc27fEO3+bexdUiAX7r4nX8IBbpC/5INTge4ATgv3Ice6RdaSEyNtWZEi2Z8fxeJHV+3c8oegRxZrRoRBm7qDofm04Yrb7gfva9XsDrl2KdpaJBfeqdq+ZIyis5yVp/zFi7lgS7WANCyJtyeIEOmAwQx5G+rNtDVeWxd+3vO2jehD2zUqd7vAcViY1QqeTzepwEYtOhmvJ/UDV1xa8j7q0RXEiixSp/E6PaQPdKHEJR5y9pXrcAwpDJ3THXu6gMwGPkydnP+OqGeas+GmEj4XgdtaRv4XMEv95ceiG00EEmNSM0PYiRYbs3lcZ8Ib8KBdpWp6Umj+kqybg+YX2SK/YelbJegMzc2lMP7KP7FC3D+zRkEzorndI1DsnF+xaSK4n7iVtDw7h/40F7uurWe9Ghu0BVyByc9fvlm6CVo5oNdBy5/Zho=; bm_s=YAAQjInTF1GXr+6QAQAArum4DwEmTXiC/UubYUGVeSPuoiawy6zYxDOj6JWJqHzFv7povcf4HGVn/8vP8IqyBNpmdWfYBlX4NWKyLaT6z4fj5Vg2EnXcgMFxxsu16JbKW+6G80UKk4M1wlgN8140UND2Eq7/C+BwJdMgsmj3xW2yYx2HNoOBhiFRyMGxkNIYh6rhkj9oiGpY0KHVYA3Yd348IMcKPrwhiDhYs5WaRyecbvu69jP67grpKRKMGbhfjd3zvz+8nrvjC3nVpId+QHtwjL0zvxS0KpKRttrS2Fva8w5LELnC8uO8eIwFQDqGc4z5EdPfldJJ0T+lfCn7bho8FSqJzA==; mynt-ulc-api=pincode%3A700028; _abck=FA360452C255EDEFEF91C657BB89268A~0~YAAQMTXZFzx3ev6QAQAAZ5EWEgxHmf788Nrszbjhk4pmzdsCg+nlkFRyIrUOZrPQ/ZsTcxV0Kh3tAlsj/PnmZIXTtq+nwgKqkWBOfvF5eTel7vA6vtW7/vdFR1zwGqrBJLUhALDtJofrJOjVJr/sB+cSYBJ9zpQT+5qjH0Rr525Fxgvtn4qf1EI6KPIZXzKAVbGPgsAUHaAIyHON/IG39v5E/NMAFEtvbUjOQHip+qC4lc94j3Z308VtRu8VWxnZLbtifDyrzqRNI1zYGi1Of9xgupExd265LO3fnPgEBL1JYrWogfwmBKLPaKvO2rJIRdFXvM6RY8pPfSDmj1iIOLjfp6CL+2QiOHauH8M8w5WDn6QjmKDaOaGD3kbjxScMQxFCbQBldDa7Wy76MbvfYe02iPRy5ZLN~-1~-1~-1; _xsrf=EwrqylFLgZ3GKp1TLkoO3w5dAXPZkifN; mynt-loc-src=expiry%3A1722586796342%7Csource%3AIP; _mxab_=config.bucket%3Dregular%3BConvenience_fee_logged_out_user%3Denabled%3Bhpmweb.mycoupons.revamp%3DRevamp_ver1%3Bcoupon.cart.channelAware%3DchannelAware_Enabled%3Bdesktop.pla%3Denabled; _pv=default; dp=d; utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1722594941%2C%22trackend%22%3A1722595001%7D; lt_timeout=1; lt_session=1; ak_bmsc=BF2EDE66000C6058D5751985832A7489~000000000000000000000000000000~YAAQnonTF4YV/QWRAQAAZ9uoEhi5FSb9qYX0FMl1P6dwxEYr1vtIKJtpAkP6L3k9mjt8+xsPfdCb2TzO1C4JVGCPRm4RJwb9s93fQFoRDNHnwrcgq8bV/RrrELq9HyEPNLTByAPuoKJ7iWwGBl4MzEc8Fgdm8qnA4zH81ZP5fRNgiY/zWIF8h7mCJ0Pp4iDV5JceoMBoJZw/V88AJlUG4IFxYcokaTNdirEeZISzJXADtxrve1az7R/F7r2lMrX2X2w7ECKHR+ox1mpEECPtRiu2T1D+xt4nPCGjSRqKEis4vJMrWZsegR6i0oKzwbpaBuVA7OHMS7/Q5exXJhUyrua6XY0OpwzbzMcJqKkXUSRL65RGk9dhJeJZ5qoD+SZp9FIXxOA2HNFuz70=; bm_sz=8A68F248AAC0E85AA8CBA64AEB42542F~YAAQnonTF4gV/QWRAQAAZ9uoEhhzYCajhFTVMfYG2xdwa3UFFUeB941H6k70xIp79KP5PuM+vjY9ZBgPFVUneKmHLbs8gNLHzi6efot2P4A0sKa9mxwkqtjip9pA33geC5q73nQjtlkL3J/Rngodxlg/SaotGa4JAqkHAhlAeyqiGcCaIsXm8VvWrd90qopsqMsGzknflipTGfhCyCJfyvnOXseQnkCY7MxCp0no5/iwwkf3H05tLVT2eL2LbflyxGiSSx5Dv5T3Xe7c7UV2o8vW1lX69iAlH33mlcDvBgBWJFyQHdDh1d3DDykXItWhfvc2PYGppYnnV807K/lQelRJSlckowHp+g4MG1omssiJ57szPQsaWxpjeRPSHY57OBEyRGIU71gW/D5r98DwPXGZnss5t50VJT0=~4469045~4403522; utrid=aW0JfUUdZxlQFV5SY09AMCM4NTA5NTM5OTgkMg%3D%3D.9a2f4c94150c0d61126fdbe31391799c; bm_mi=E1C38B8B15A4FF2ACA93FED9E88819B2~YAAQnonTF7MW/QWRAQAAROGoEhjeEpFIKC/ckJxmhCFrdKEGEM8x+ml649lEhFpa+uqxRlqZ0lJfteKZJtwJ1KU1ilk+wtuGtLcDbP+qXGFbodm1L4/UyIYMB+qnSxAnezRYAZTOEphoIyfNQj6iRT7jfBtDzhQJHQicF2Jexsmh4LpKL/Fd/kJyGjyfTqFN+yp7zOyFCs4eaY+gWiCPe2KjbgZbFaI2/p3BnpKFygGFPYwFwYj5Sde6PJW/3gIEMH4ZK9A4yaVwcipNDoDL2LBsuWnMTmBx9UaGOEN02lRbXv8tqeQ/u9Lo2iq0vIxlPOumtJX6IEWYIOmvzqyImd/R6Tfv0AVv3jK3Qu0TUFDsQg==~1; bm_sv=562DEBB8644A469B2AF626405AE8728C~YAAQnonTF7QW/QWRAQAAROGoEhiOFpHDo3V5R0xzmd1yBN3x4iIvp5YEHue+3zzDnSUk0rENb2ORma3QV93sEg8xN/itvA8yUkX05lxaTB1Bp/n4wyI/i70hmpo5nWgwRdwt7RWwIOQR3eyPCJmxqFwOF8tMjlAnEO9EszzEMTwrluaXC8OSfQpTDfZs+l88HagnPLxe82+YAYPxpZYGiBzdB9Xgedzj+wbm1ImFYBwnwmrtdK0wCTg7nbSrzU14~1',
    'deviceid': '4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb',
    'origin': 'https://www.myntra.com',
    'priority': 'u=1, i',
    'referer': 'https://www.myntra.com/campussutra?f=Brand%3ACampus%20Sutra',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-location-context': 'pincode=700028;source=IP',
    'x-meta-app': 'deviceId=4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb;appFamily=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36;reqChannel=web;channel=web;',
    'x-myntraweb': 'Yes',
    'x-requested-with': 'browser',
}

json_data = {
    'previousContext': {
        'pincode': '700028',
        'source': 'IP',
    },
    'currentContext': None,
}
#%%
response = requests.post(
    'https://www.myntra.com/gateway/v1/user/locationContext',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"previousContext":{"pincode":"700028","source":"IP"},"currentContext":null}'
#response = requests.post('https://www.myntra.com/gateway/v1/user/locationContext', cookies=cookies, headers=headers, data=data)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://constant.myntassets.com/web/assets/img/80cc455a-92d2-4b5c-a038-7da0d92af33f1539674178924-google_play.png',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://constant.myntassets.com/web/assets/img/6c3306ca-1efa-4a27-8769-3b69d16948741574602902452-original.png',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}



headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'id': 'GTM-H34B',
}

response = requests.get('https://www.googletagmanager.com/gtm.js', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}




headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}



headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}



headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

params = {
    'secret': 'p4p3vo',
}



cookies = {
    'at': 'ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWWpNeFkySm1NelF0TkdOaFpTMHhNV1ZtTFRreVlqZ3RNV1ZsTmpjd1pXTTVabUk1SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzTXpjM01ERTROamdzSW1semN5STZJa2xFUlVFaWZRLjcyUTBZczRVNFdjT09zaEhuQnNlRWRTb3pHS01oR2c3VDhHSEwyUkpiaFk=',
    '_d_id': '4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb',
    'mynt-eupv': '1',
    'x-mynt-pca': 'nH9mxtXUPchmnWDGbhXl9jaw-c5Vja_ovNGyjLbpRsDQIkl7OflPowdK8z8pxlicfpTpLHNuswY89SAkZ0oVceg_fRX_GCoVljGV-NLrKDUCeGRNSpaf2XMnYzvBI24aQdwXtGc0zx9tzATRW3LlN5Xa3EcQmrjYx43Q1R_Vq_62sBgai-E%3D',
    'bm_so': 'E109E85282B2EDF1E26153975A59FFAE6442F951FCDF85BE3175DFB4A8619B05~YAAQjInTFxWXr+6QAQAAo+S4DwAdc9vA9ij+VOThLf5JjS+2IBvz3pawfnK2IGki5GdnWZSQsV3yw+HzZHRTU3HJYmEurWPNcsyJksBpzqx3457t8JX3fMu6OxWXA2mXues2Wwk1YluQ3wEKAw5EQ0Gb9dR12AS8lmuCLc27fEO3+bexdUiAX7r4nX8IBbpC/5INTge4ATgv3Ice6RdaSEyNtWZEi2Z8fxeJHV+3c8oegRxZrRoRBm7qDofm04Yrb7gfva9XsDrl2KdpaJBfeqdq+ZIyis5yVp/zFi7lgS7WANCyJtyeIEOmAwQx5G+rNtDVeWxd+3vO2jehD2zUqd7vAcViY1QqeTzepwEYtOhmvJ/UDV1xa8j7q0RXEiixSp/E6PaQPdKHEJR5y9pXrcAwpDJ3THXu6gMwGPkydnP+OqGeas+GmEj4XgdtaRv4XMEv95ceiG00EEmNSM0PYiRYbs3lcZ8Ib8KBdpWp6Umj+kqybg+YX2SK/YelbJegMzc2lMP7KP7FC3D+zRkEzorndI1DsnF+xaSK4n7iVtDw7h/40F7uurWe9Ghu0BVyByc9fvlm6CVo5oNdBy5/Zho=',
    'bm_s': 'YAAQjInTF1GXr+6QAQAArum4DwEmTXiC/UubYUGVeSPuoiawy6zYxDOj6JWJqHzFv7povcf4HGVn/8vP8IqyBNpmdWfYBlX4NWKyLaT6z4fj5Vg2EnXcgMFxxsu16JbKW+6G80UKk4M1wlgN8140UND2Eq7/C+BwJdMgsmj3xW2yYx2HNoOBhiFRyMGxkNIYh6rhkj9oiGpY0KHVYA3Yd348IMcKPrwhiDhYs5WaRyecbvu69jP67grpKRKMGbhfjd3zvz+8nrvjC3nVpId+QHtwjL0zvxS0KpKRttrS2Fva8w5LELnC8uO8eIwFQDqGc4z5EdPfldJJ0T+lfCn7bho8FSqJzA==',
    '_abck': 'FA360452C255EDEFEF91C657BB89268A~0~YAAQMTXZFzx3ev6QAQAAZ5EWEgxHmf788Nrszbjhk4pmzdsCg+nlkFRyIrUOZrPQ/ZsTcxV0Kh3tAlsj/PnmZIXTtq+nwgKqkWBOfvF5eTel7vA6vtW7/vdFR1zwGqrBJLUhALDtJofrJOjVJr/sB+cSYBJ9zpQT+5qjH0Rr525Fxgvtn4qf1EI6KPIZXzKAVbGPgsAUHaAIyHON/IG39v5E/NMAFEtvbUjOQHip+qC4lc94j3Z308VtRu8VWxnZLbtifDyrzqRNI1zYGi1Of9xgupExd265LO3fnPgEBL1JYrWogfwmBKLPaKvO2rJIRdFXvM6RY8pPfSDmj1iIOLjfp6CL+2QiOHauH8M8w5WDn6QjmKDaOaGD3kbjxScMQxFCbQBldDa7Wy76MbvfYe02iPRy5ZLN~-1~-1~-1',
    '_mxab_': 'config.bucket%3Dregular%3BConvenience_fee_logged_out_user%3Denabled%3Bhpmweb.mycoupons.revamp%3DRevamp_ver1%3Bcoupon.cart.channelAware%3DchannelAware_Enabled%3Bdesktop.pla%3Denabled',
    '_pv': 'default',
    'dp': 'd',
    'utm_track_v1': '%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1722594941%2C%22trackend%22%3A1722595001%7D',
    'lt_timeout': '1',
    'lt_session': '1',
    'ak_bmsc': 'BF2EDE66000C6058D5751985832A7489~000000000000000000000000000000~YAAQnonTF4YV/QWRAQAAZ9uoEhi5FSb9qYX0FMl1P6dwxEYr1vtIKJtpAkP6L3k9mjt8+xsPfdCb2TzO1C4JVGCPRm4RJwb9s93fQFoRDNHnwrcgq8bV/RrrELq9HyEPNLTByAPuoKJ7iWwGBl4MzEc8Fgdm8qnA4zH81ZP5fRNgiY/zWIF8h7mCJ0Pp4iDV5JceoMBoJZw/V88AJlUG4IFxYcokaTNdirEeZISzJXADtxrve1az7R/F7r2lMrX2X2w7ECKHR+ox1mpEECPtRiu2T1D+xt4nPCGjSRqKEis4vJMrWZsegR6i0oKzwbpaBuVA7OHMS7/Q5exXJhUyrua6XY0OpwzbzMcJqKkXUSRL65RGk9dhJeJZ5qoD+SZp9FIXxOA2HNFuz70=',
    'bm_sz': '8A68F248AAC0E85AA8CBA64AEB42542F~YAAQnonTF4gV/QWRAQAAZ9uoEhhzYCajhFTVMfYG2xdwa3UFFUeB941H6k70xIp79KP5PuM+vjY9ZBgPFVUneKmHLbs8gNLHzi6efot2P4A0sKa9mxwkqtjip9pA33geC5q73nQjtlkL3J/Rngodxlg/SaotGa4JAqkHAhlAeyqiGcCaIsXm8VvWrd90qopsqMsGzknflipTGfhCyCJfyvnOXseQnkCY7MxCp0no5/iwwkf3H05tLVT2eL2LbflyxGiSSx5Dv5T3Xe7c7UV2o8vW1lX69iAlH33mlcDvBgBWJFyQHdDh1d3DDykXItWhfvc2PYGppYnnV807K/lQelRJSlckowHp+g4MG1omssiJ57szPQsaWxpjeRPSHY57OBEyRGIU71gW/D5r98DwPXGZnss5t50VJT0=~4469045~4403522',
    'bm_mi': 'E1C38B8B15A4FF2ACA93FED9E88819B2~YAAQnonTF7MW/QWRAQAAROGoEhjeEpFIKC/ckJxmhCFrdKEGEM8x+ml649lEhFpa+uqxRlqZ0lJfteKZJtwJ1KU1ilk+wtuGtLcDbP+qXGFbodm1L4/UyIYMB+qnSxAnezRYAZTOEphoIyfNQj6iRT7jfBtDzhQJHQicF2Jexsmh4LpKL/Fd/kJyGjyfTqFN+yp7zOyFCs4eaY+gWiCPe2KjbgZbFaI2/p3BnpKFygGFPYwFwYj5Sde6PJW/3gIEMH4ZK9A4yaVwcipNDoDL2LBsuWnMTmBx9UaGOEN02lRbXv8tqeQ/u9Lo2iq0vIxlPOumtJX6IEWYIOmvzqyImd/R6Tfv0AVv3jK3Qu0TUFDsQg==~1',
    '_ma_session': '%7B%22id%22%3A%2224e5b2b3-8627-49e6-a1f2-ad491d211604-4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D',
    'microsessid': '608',
    'utrid': 'FUBeGWdVV2YVcllMAEdAMCMxNzYwOTY1MTQyJDI%3D.05712306d85dcc36bba8d375775e5757',
    '_xsrf': 'AHxlYBKiiN0vhYxDcpoU33VlEgykjoCt',
    'user_session': 'yZAnm9cKDEs-6PdDRL22gQ.VdL0Nqan_t5Dx4Avhi9x8vCltu5Y2qjrikC13QVRgLRzovxbWeAooNtoEdzeLS4RU4OkkLGzCwUvJ7ZL4RutU8NlnBgKbwFDKq_QL-CnVLTo1O8DwImpu2vF2qExCJna3vWBLRflLtdWfFDfZIPMTQ.1722594943643.86400000.bIkAGjWW_xYP13qoSs2CJlmiO_qa_ydH-N8NYdCN1MM',
    'bm_sv': '562DEBB8644A469B2AF626405AE8728C~YAAQnonTFw0X/QWRAQAA5eKoEhi3NpRmDiWD68UfvlEanc8O79ETmzICdR21q79CehJGAT5wlq3fW0fxlXkqEdWendNaakI3VFtliSGHRgv9+dWm1hoLJjsp5q5rQPx6W99G/NKGr8+CY33KWapIN1wqAQKfyLa7CQ+ex/fhKXn8unlsa5NR5JYw80E+pHpvrPdTjYh82hBpdyq7DYXMNo+NEV9KZVQpgukyAZWpQaSTEUtyE1W39QIluWM9i7im~1',
    'mynt-ulc-api': 'pincode%3A700006',
    'mynt-loc-src': 'expiry%3A1722596383657%7Csource%3AIP',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'at=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWWpNeFkySm1NelF0TkdOaFpTMHhNV1ZtTFRreVlqZ3RNV1ZsTmpjd1pXTTVabUk1SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzTXpjM01ERTROamdzSW1semN5STZJa2xFUlVFaWZRLjcyUTBZczRVNFdjT09zaEhuQnNlRWRTb3pHS01oR2c3VDhHSEwyUkpiaFk=; _d_id=4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb; mynt-eupv=1; x-mynt-pca=nH9mxtXUPchmnWDGbhXl9jaw-c5Vja_ovNGyjLbpRsDQIkl7OflPowdK8z8pxlicfpTpLHNuswY89SAkZ0oVceg_fRX_GCoVljGV-NLrKDUCeGRNSpaf2XMnYzvBI24aQdwXtGc0zx9tzATRW3LlN5Xa3EcQmrjYx43Q1R_Vq_62sBgai-E%3D; bm_so=E109E85282B2EDF1E26153975A59FFAE6442F951FCDF85BE3175DFB4A8619B05~YAAQjInTFxWXr+6QAQAAo+S4DwAdc9vA9ij+VOThLf5JjS+2IBvz3pawfnK2IGki5GdnWZSQsV3yw+HzZHRTU3HJYmEurWPNcsyJksBpzqx3457t8JX3fMu6OxWXA2mXues2Wwk1YluQ3wEKAw5EQ0Gb9dR12AS8lmuCLc27fEO3+bexdUiAX7r4nX8IBbpC/5INTge4ATgv3Ice6RdaSEyNtWZEi2Z8fxeJHV+3c8oegRxZrRoRBm7qDofm04Yrb7gfva9XsDrl2KdpaJBfeqdq+ZIyis5yVp/zFi7lgS7WANCyJtyeIEOmAwQx5G+rNtDVeWxd+3vO2jehD2zUqd7vAcViY1QqeTzepwEYtOhmvJ/UDV1xa8j7q0RXEiixSp/E6PaQPdKHEJR5y9pXrcAwpDJ3THXu6gMwGPkydnP+OqGeas+GmEj4XgdtaRv4XMEv95ceiG00EEmNSM0PYiRYbs3lcZ8Ib8KBdpWp6Umj+kqybg+YX2SK/YelbJegMzc2lMP7KP7FC3D+zRkEzorndI1DsnF+xaSK4n7iVtDw7h/40F7uurWe9Ghu0BVyByc9fvlm6CVo5oNdBy5/Zho=; bm_s=YAAQjInTF1GXr+6QAQAArum4DwEmTXiC/UubYUGVeSPuoiawy6zYxDOj6JWJqHzFv7povcf4HGVn/8vP8IqyBNpmdWfYBlX4NWKyLaT6z4fj5Vg2EnXcgMFxxsu16JbKW+6G80UKk4M1wlgN8140UND2Eq7/C+BwJdMgsmj3xW2yYx2HNoOBhiFRyMGxkNIYh6rhkj9oiGpY0KHVYA3Yd348IMcKPrwhiDhYs5WaRyecbvu69jP67grpKRKMGbhfjd3zvz+8nrvjC3nVpId+QHtwjL0zvxS0KpKRttrS2Fva8w5LELnC8uO8eIwFQDqGc4z5EdPfldJJ0T+lfCn7bho8FSqJzA==; _abck=FA360452C255EDEFEF91C657BB89268A~0~YAAQMTXZFzx3ev6QAQAAZ5EWEgxHmf788Nrszbjhk4pmzdsCg+nlkFRyIrUOZrPQ/ZsTcxV0Kh3tAlsj/PnmZIXTtq+nwgKqkWBOfvF5eTel7vA6vtW7/vdFR1zwGqrBJLUhALDtJofrJOjVJr/sB+cSYBJ9zpQT+5qjH0Rr525Fxgvtn4qf1EI6KPIZXzKAVbGPgsAUHaAIyHON/IG39v5E/NMAFEtvbUjOQHip+qC4lc94j3Z308VtRu8VWxnZLbtifDyrzqRNI1zYGi1Of9xgupExd265LO3fnPgEBL1JYrWogfwmBKLPaKvO2rJIRdFXvM6RY8pPfSDmj1iIOLjfp6CL+2QiOHauH8M8w5WDn6QjmKDaOaGD3kbjxScMQxFCbQBldDa7Wy76MbvfYe02iPRy5ZLN~-1~-1~-1; _mxab_=config.bucket%3Dregular%3BConvenience_fee_logged_out_user%3Denabled%3Bhpmweb.mycoupons.revamp%3DRevamp_ver1%3Bcoupon.cart.channelAware%3DchannelAware_Enabled%3Bdesktop.pla%3Denabled; _pv=default; dp=d; utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1722594941%2C%22trackend%22%3A1722595001%7D; lt_timeout=1; lt_session=1; ak_bmsc=BF2EDE66000C6058D5751985832A7489~000000000000000000000000000000~YAAQnonTF4YV/QWRAQAAZ9uoEhi5FSb9qYX0FMl1P6dwxEYr1vtIKJtpAkP6L3k9mjt8+xsPfdCb2TzO1C4JVGCPRm4RJwb9s93fQFoRDNHnwrcgq8bV/RrrELq9HyEPNLTByAPuoKJ7iWwGBl4MzEc8Fgdm8qnA4zH81ZP5fRNgiY/zWIF8h7mCJ0Pp4iDV5JceoMBoJZw/V88AJlUG4IFxYcokaTNdirEeZISzJXADtxrve1az7R/F7r2lMrX2X2w7ECKHR+ox1mpEECPtRiu2T1D+xt4nPCGjSRqKEis4vJMrWZsegR6i0oKzwbpaBuVA7OHMS7/Q5exXJhUyrua6XY0OpwzbzMcJqKkXUSRL65RGk9dhJeJZ5qoD+SZp9FIXxOA2HNFuz70=; bm_sz=8A68F248AAC0E85AA8CBA64AEB42542F~YAAQnonTF4gV/QWRAQAAZ9uoEhhzYCajhFTVMfYG2xdwa3UFFUeB941H6k70xIp79KP5PuM+vjY9ZBgPFVUneKmHLbs8gNLHzi6efot2P4A0sKa9mxwkqtjip9pA33geC5q73nQjtlkL3J/Rngodxlg/SaotGa4JAqkHAhlAeyqiGcCaIsXm8VvWrd90qopsqMsGzknflipTGfhCyCJfyvnOXseQnkCY7MxCp0no5/iwwkf3H05tLVT2eL2LbflyxGiSSx5Dv5T3Xe7c7UV2o8vW1lX69iAlH33mlcDvBgBWJFyQHdDh1d3DDykXItWhfvc2PYGppYnnV807K/lQelRJSlckowHp+g4MG1omssiJ57szPQsaWxpjeRPSHY57OBEyRGIU71gW/D5r98DwPXGZnss5t50VJT0=~4469045~4403522; bm_mi=E1C38B8B15A4FF2ACA93FED9E88819B2~YAAQnonTF7MW/QWRAQAAROGoEhjeEpFIKC/ckJxmhCFrdKEGEM8x+ml649lEhFpa+uqxRlqZ0lJfteKZJtwJ1KU1ilk+wtuGtLcDbP+qXGFbodm1L4/UyIYMB+qnSxAnezRYAZTOEphoIyfNQj6iRT7jfBtDzhQJHQicF2Jexsmh4LpKL/Fd/kJyGjyfTqFN+yp7zOyFCs4eaY+gWiCPe2KjbgZbFaI2/p3BnpKFygGFPYwFwYj5Sde6PJW/3gIEMH4ZK9A4yaVwcipNDoDL2LBsuWnMTmBx9UaGOEN02lRbXv8tqeQ/u9Lo2iq0vIxlPOumtJX6IEWYIOmvzqyImd/R6Tfv0AVv3jK3Qu0TUFDsQg==~1; _ma_session=%7B%22id%22%3A%2224e5b2b3-8627-49e6-a1f2-ad491d211604-4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D; microsessid=608; utrid=FUBeGWdVV2YVcllMAEdAMCMxNzYwOTY1MTQyJDI%3D.05712306d85dcc36bba8d375775e5757; _xsrf=AHxlYBKiiN0vhYxDcpoU33VlEgykjoCt; user_session=yZAnm9cKDEs-6PdDRL22gQ.VdL0Nqan_t5Dx4Avhi9x8vCltu5Y2qjrikC13QVRgLRzovxbWeAooNtoEdzeLS4RU4OkkLGzCwUvJ7ZL4RutU8NlnBgKbwFDKq_QL-CnVLTo1O8DwImpu2vF2qExCJna3vWBLRflLtdWfFDfZIPMTQ.1722594943643.86400000.bIkAGjWW_xYP13qoSs2CJlmiO_qa_ydH-N8NYdCN1MM; bm_sv=562DEBB8644A469B2AF626405AE8728C~YAAQnonTFw0X/QWRAQAA5eKoEhi3NpRmDiWD68UfvlEanc8O79ETmzICdR21q79CehJGAT5wlq3fW0fxlXkqEdWendNaakI3VFtliSGHRgv9+dWm1hoLJjsp5q5rQPx6W99G/NKGr8+CY33KWapIN1wqAQKfyLa7CQ+ex/fhKXn8unlsa5NR5JYw80E+pHpvrPdTjYh82hBpdyq7DYXMNo+NEV9KZVQpgukyAZWpQaSTEUtyE1W39QIluWM9i7im~1; mynt-ulc-api=pincode%3A700006; mynt-loc-src=expiry%3A1722596383657%7Csource%3AIP',
    'deviceid': '4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb',
    'priority': 'u=1, i',
    'referer': 'https://www.myntra.com/campussutra?f=Brand%3ACampus%20Sutra',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-location-context': 'pincode=700006;source=IP',
    'x-meta-app': 'deviceId=4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb;appFamily=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36;reqChannel=web;channel=web;',
    'x-myntraweb': 'Yes',
    'x-requested-with': 'browser',
}

response = requests.get('https://www.myntra.com/gateway/v1/cart/default/summary', cookies=cookies, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': 'application/json',
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
}

data = '[{"ab_tests":{"config.bucket":"regular","Convenience_fee_logged_out_user":"enabled","hpmweb.mycoupons.revamp":"Revamp_ver1","coupon.cart.channelAware":"channelAware_Enabled","desktop.pla":"enabled"},"event_meta_version":"1.3.0","event_payload_version":"1.1.0","geo":{"lat":0,"long":0,"pincode":{"ip":"700006"}},"network":{"bandwidth":"-1.0","bandwidth_bucket":"UNKNOWN","carrier":"","ip":"","type":""},"device":{"advertising_id":"","build_number":"","installation_id":"","device_id":"4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb","height":864,"width":1536,"category":"desktop","os":"Windows","os_api_version":-1,"os_version":"10.0.0","manufacturer":"","model_number":"","ga_client_id":null},"user":{"customer_id":"","is_logged_in":false,"uidx":"","segments":[]},"session":{"auto_id":null,"is_first_session":"0","server_offset":-1,"request_id":"2ad4be00-c5bd-4bc1-9bbb-e70635f62841","landing_screen":"/campussutra","session_id":"24e5b2b3-8627-49e6-a1f2-ad491d211604-4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb","session_referrer":{"url":"https://www.myntra.com/campussutra?f=Brand%3ACampus+Sutra&utm_channel=direct","referrer_url":"","medium":"","source":"","channel":"direct","referrer":"https://www.myntra.com/campussutra?f=Brand%3ACampus+Sutra&utm_channel=direct"},"start_time":1722594943767},"app":{"name":"MyntraRetailWeb","build":-1,"react_bundle_name":"","react_bundle_version":"","version":""},"event_sequence":null,"payload":{"data_set":{"entity_optional_attributes":{"referrer":"https://www.myntra.com/campussutra?f=Brand%3ACampus+Sutra&utm_channel=direct","url":"https://www.myntra.com/campussutra?f=Brand%3ACampus+Sutra&utm_channel=direct"}}},"client_id":"lzZNMYGoPkQVWOGL3wg81DLeJ4arpd","event_type":"DeepLink","user_attributes":{"pin":"700028","pin_src":"ip"},"_t":"DeepLink","time_stamp":1722594943768}]'

response = requests.post('https://touch.myntra.com/track-web', headers=headers, data=data)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': 'application/json',
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
}

data = '[{"ab_tests":{"config.bucket":"regular","Convenience_fee_logged_out_user":"enabled","hpmweb.mycoupons.revamp":"Revamp_ver1","coupon.cart.channelAware":"channelAware_Enabled","desktop.pla":"enabled"},"event_meta_version":"1.3.0","event_payload_version":"1.1.0","geo":{"lat":0,"long":0,"pincode":{"ip":"700006"}},"network":{"bandwidth":"-1.0","bandwidth_bucket":"UNKNOWN","carrier":"","ip":"","type":""},"device":{"advertising_id":"","build_number":"","installation_id":"","device_id":"4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb","height":864,"width":1536,"category":"desktop","os":"Windows","os_api_version":-1,"os_version":"10.0.0","manufacturer":"","model_number":"","ga_client_id":null},"user":{"customer_id":"","is_logged_in":false,"uidx":"","segments":[]},"session":{"auto_id":null,"is_first_session":"0","server_offset":-1,"request_id":"098e83fe-a16b-46ce-bf2e-7672968514c6","landing_screen":"/campussutra","session_id":"24e5b2b3-8627-49e6-a1f2-ad491d211604-4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb","session_referrer":{"referrer_url":"","medium":"","source":"","channel":"direct"},"start_time":1722594943772},"app":{"name":"MyntraRetailWeb","build":-1,"react_bundle_name":"","react_bundle_version":"","version":""},"event_sequence":null,"payload":{"screen":{"data_set":{"entity_type":"list","entity_name":"/campussutra","entity_optional_attributes":{"scroll-position":""}},"referer":{},"entity_type":"list","name":"Shopping Page-List Page/campussutra","url":"https://www.myntra.com/campussutra?f=Brand%3ACampus%20Sutra","variant":"web","type":"list"},"custom":{"v1":"1536"}},"client_id":"lzZNMYGoPkQVWOGL3wg81DLeJ4arpd","user_attributes":{"pin":"700028","pin_src":"ip"},"_t":"ScreenLoad","time_stamp":1722594943773}]'

response = requests.post('https://touch.myntra.com/track-web', headers=headers, data=data)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': 'application/json',
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
}

data = '[{"ab_tests":{"config.bucket":"regular","Convenience_fee_logged_out_user":"enabled","hpmweb.mycoupons.revamp":"Revamp_ver1","coupon.cart.channelAware":"channelAware_Enabled","desktop.pla":"enabled"},"event_meta_version":"1.3.0","event_payload_version":"1.1.0","geo":{"lat":0,"long":0,"pincode":{"ip":"700006"}},"network":{"bandwidth":"-1.0","bandwidth_bucket":"UNKNOWN","carrier":"","ip":"","type":""},"device":{"advertising_id":"","build_number":"","installation_id":"","device_id":"4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb","height":864,"width":1536,"category":"desktop","os":"Windows","os_api_version":-1,"os_version":"10.0.0","manufacturer":"","model_number":"","ga_client_id":null},"user":{"customer_id":"","is_logged_in":false,"uidx":"","segments":[]},"session":{"auto_id":null,"is_first_session":"0","server_offset":-1,"request_id":"d91918f5-0ad9-4a22-ba99-4a33aa0c9f7e","landing_screen":"/campussutra","session_id":"24e5b2b3-8627-49e6-a1f2-ad491d211604-4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb","session_referrer":{"referrer_url":"","medium":"","source":"","channel":"direct"},"start_time":1722594943776},"app":{"name":"MyntraRetailWeb","build":-1,"react_bundle_name":"","react_bundle_version":"","version":""},"event_sequence":null,"payload":{"screen":{"data_set":{"entity_name":"/campussutra","entity_type":"list"},"referer":{},"entity_type":"list","name":"Shopping Page - List Page /campussutra","url":"https://www.myntra.com/campussutra?f=Brand%3ACampus%20Sutra","type":"list","variant":"web","widget_items":{"data_set":{"data":[{"entity_name":"Campus Sutra Classic Self Design Spread Collar Casual Shirt","entity_id":28219632,"entity_type":"product","entity_optional_attributes":{"price":1899,"discounted_price":664,"discount":1235,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Women Olive Green Applique Detail Denim Jacket","entity_id":14862490,"entity_type":"product","entity_optional_attributes":{"price":2399,"discounted_price":719,"discount":1680,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Distressed Cotton Denim Shorts","entity_id":24442152,"entity_type":"product","entity_optional_attributes":{"price":1899,"discounted_price":759,"discount":1140,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Teal Green Classic Spread Collar Self Design Casual Shirt","entity_id":26712918,"entity_type":"product","entity_optional_attributes":{"price":1899,"discounted_price":664,"discount":1235,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Cable Knit Cable Knit Woollen Pullover","entity_id":25373430,"entity_type":"product","entity_optional_attributes":{"price":1999,"discounted_price":999,"discount":1000,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Blue Smart Light Fade Whiskers Cat Scratches Cotton Slim Fit Jeans","entity_id":22732960,"entity_type":"product","entity_optional_attributes":{"price":1899,"discounted_price":474,"discount":1425,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Grey & Black Colourblocked Track Pants","entity_id":16482190,"entity_type":"product","entity_optional_attributes":{"price":1799,"discounted_price":539,"discount":1260,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Teal Blue Printed Oversized T-Shirt & Shorts","entity_id":23563936,"entity_type":"product","entity_optional_attributes":{"price":2499,"discounted_price":874,"discount":1625,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Regular Fit Yoga Track Pants","entity_id":17388400,"entity_type":"product","entity_optional_attributes":{"price":1799,"discounted_price":629,"discount":1170,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"{\\"Tag\\":\\"MEXPRESS\\",\\"DeliveryBucket\\":\\"2DD\\"}","isUld":false}}},{"entity_name":"Campus Sutra Black Printed Oversized T-Shirt & Shorts","entity_id":23563952,"entity_type":"product","entity_optional_attributes":{"price":2499,"discounted_price":874,"discount":1625,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Windcheater Spread Collar Ribbed Hem Padded Jacket","entity_id":25160160,"entity_type":"product","entity_optional_attributes":{"price":3299,"discounted_price":1154,"discount":2145,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Blue Floral Printed Windcheater Cotton Denim Jacket","entity_id":25876820,"entity_type":"product","entity_optional_attributes":{"price":3499,"discounted_price":1224,"discount":2275,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Hooded Pullover Cotton Sweatshirt","entity_id":24583872,"entity_type":"product","entity_optional_attributes":{"price":2499,"discounted_price":749,"discount":1750,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Black Colourblocked Track Pants","entity_id":16482194,"entity_type":"product","entity_optional_attributes":{"price":1799,"discounted_price":719,"discount":1080,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Blue Typography Print Cotton Crop T-shirt","entity_id":23043994,"entity_type":"product","entity_optional_attributes":{"price":1049,"discounted_price":524,"discount":525,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Navy-Blue & Yellow Graphic Printed Co-Ords","entity_id":18810742,"entity_type":"product","entity_optional_attributes":{"price":1999,"discounted_price":799,"discount":1200,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Yellow Self Design Classic Fit Casual Shirt","entity_id":22736962,"entity_type":"product","entity_optional_attributes":{"price":1699,"discounted_price":764,"discount":935,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Classic Floral Printed Cotton Casual Shirt","entity_id":24443526,"entity_type":"product","entity_optional_attributes":{"price":1799,"discounted_price":359,"discount":1440,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Smart Slim Fit Low Distress Light Fade Stretchable Cotton Jeans","entity_id":22442368,"entity_type":"product","entity_optional_attributes":{"price":1699,"discounted_price":509,"discount":1190,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Women Navy Blue Hooded Sweatshirt","entity_id":20546602,"entity_type":"product","entity_optional_attributes":{"price":1699,"discounted_price":849,"discount":850,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Black Pure Cotton Oversized T-shirt & Mid-Rise Shorts","entity_id":27423166,"entity_type":"product","entity_optional_attributes":{"price":2499,"discounted_price":624,"discount":1875,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men White Printed Co-Ords","entity_id":18810738,"entity_type":"product","entity_optional_attributes":{"price":1999,"discounted_price":799,"discount":1200,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra New Multi Striped Spread Collar Cotton Casual Shirt","entity_id":26460996,"entity_type":"product","entity_optional_attributes":{"price":1499,"discounted_price":674,"discount":825,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Black Solid Windcheater","entity_id":12252608,"entity_type":"product","entity_optional_attributes":{"price":2299,"discounted_price":1034,"discount":1265,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Maroon Checked Puff Sleeves Cut-Outs Fit & Flare Midi Dress","entity_id":23862548,"entity_type":"product","entity_optional_attributes":{"price":1999,"discounted_price":699,"discount":1300,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Women Classic Boxy Opaque Striped Casual Shirt","entity_id":28088392,"entity_type":"product","entity_optional_attributes":{"price":1499,"discounted_price":599,"discount":900,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Blue Textured Classic Fit Casual Shirt","entity_id":22737000,"entity_type":"product","entity_optional_attributes":{"price":1599,"discounted_price":719,"discount":880,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Printed Detail Oversized Sporty T-Shirt With Shorts Co-Ords","entity_id":23563920,"entity_type":"product","entity_optional_attributes":{"price":2499,"discounted_price":874,"discount":1625,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Black & White Striped Casual Shirt","entity_id":14811402,"entity_type":"product","entity_optional_attributes":{"price":1499,"discounted_price":749,"discount":750,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Spread Collar Windcheater Outdoor Sporty Jacket","entity_id":25160162,"entity_type":"product","entity_optional_attributes":{"price":2799,"discounted_price":1119,"discount":1680,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Classic Spread Collar Floral Printed Cotton Casual Shirt","entity_id":24443520,"entity_type":"product","entity_optional_attributes":{"price":1799,"discounted_price":359,"discount":1440,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra White Dyed Lapel Collar Shirt & Mid-Rise Shorts","entity_id":27423190,"entity_type":"product","entity_optional_attributes":{"price":1999,"discounted_price":899,"discount":1100,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Windcheater Hooded Quilted Jacket","entity_id":26006938,"entity_type":"product","entity_optional_attributes":{"price":3999,"discounted_price":1399,"discount":2600,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Striped Cotton Regular Fit Mid-Rise Shorts","entity_id":22442662,"entity_type":"product","entity_optional_attributes":{"price":1399,"discounted_price":419,"discount":980,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Classic Tartan Checked Cotton Shirt","entity_id":23669714,"entity_type":"product","entity_optional_attributes":{"price":1899,"discounted_price":702,"discount":1197,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Pink Printed Round Neck T-shirt With Shorts","entity_id":23443256,"entity_type":"product","entity_optional_attributes":{"price":2499,"discounted_price":874,"discount":1625,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Printed T-Shirt & Shorts Co-Ords","entity_id":23563958,"entity_type":"product","entity_optional_attributes":{"price":2499,"discounted_price":874,"discount":1625,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Green & White Tie & Dye Shirt Collar Co-Ord","entity_id":22869072,"entity_type":"product","entity_optional_attributes":{"price":1999,"discounted_price":999,"discount":1000,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Black & White Printed Round Neck Co-Ord Set","entity_id":22869122,"entity_type":"product","entity_optional_attributes":{"price":2499,"discounted_price":874,"discount":1625,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Blue Smart Slim Fit Mildly Distressed Light Fade Stretchable Cotton Jeans","entity_id":23669690,"entity_type":"product","entity_optional_attributes":{"price":1899,"discounted_price":474,"discount":1425,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra White Classic Striped Cotton Casual Shirt","entity_id":22869144,"entity_type":"product","entity_optional_attributes":{"price":1899,"discounted_price":702,"discount":1197,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Black Striped Drop Shoulder Sleeves Pure Cotton Oversized T-Shirt & Short","entity_id":27423162,"entity_type":"product","entity_optional_attributes":{"price":2499,"discounted_price":749,"discount":1750,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Green & Black Printed Co-Ords","entity_id":20914414,"entity_type":"product","entity_optional_attributes":{"price":1999,"discounted_price":799,"discount":1200,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men White & Green Tie Dye Printed Co-Ords","entity_id":18810746,"entity_type":"product","entity_optional_attributes":{"price":1999,"discounted_price":799,"discount":1200,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Printed T-Shirt With Shorts","entity_id":25373294,"entity_type":"product","entity_optional_attributes":{"price":2499,"discounted_price":874,"discount":1625,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Black & White Graphic Printed Co-Ords","entity_id":18810748,"entity_type":"product","entity_optional_attributes":{"price":1999,"discounted_price":799,"discount":1200,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Spread Collar Long Sleeves Modern Boxy Striped Casual Cotton Shirt","entity_id":27449902,"entity_type":"product","entity_optional_attributes":{"price":1499,"discounted_price":674,"discount":825,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Checked Windcheater Cotton Tailored Jacket","entity_id":25810188,"entity_type":"product","entity_optional_attributes":{"price":3499,"discounted_price":2099,"discount":1400,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Oliv Green Printed T-Shirt & Shorts Co-Ords","entity_id":25373330,"entity_type":"product","entity_optional_attributes":{"price":2499,"discounted_price":1124,"discount":1375,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Printed Detail Oversized T-Shirt With Short Co-Ords","entity_id":23563934,"entity_type":"product","entity_optional_attributes":{"price":2499,"discounted_price":874,"discount":1625,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}}]}}}},"client_id":"lzZNMYGoPkQVWOGL3wg81DLeJ4arpd","user_attributes":{"pin":"700028","pin_src":"ip"},"_t":"Product list loaded","time_stamp":1722594943776}]'

response = requests.post('https://touch.myntra.com/track-web', headers=headers, data=data)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': 'application/json',
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
}

data = '[{"ab_tests":{"config.bucket":"regular","Convenience_fee_logged_out_user":"enabled","hpmweb.mycoupons.revamp":"Revamp_ver1","coupon.cart.channelAware":"channelAware_Enabled","desktop.pla":"enabled"},"event_meta_version":"1.3.0","event_payload_version":"1.1.0","geo":{"lat":0,"long":0,"pincode":{"ip":"700006"}},"network":{"bandwidth":"-1.0","bandwidth_bucket":"UNKNOWN","carrier":"","ip":"","type":""},"device":{"advertising_id":"","build_number":"","installation_id":"","device_id":"4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb","height":864,"width":1536,"category":"desktop","os":"Windows","os_api_version":-1,"os_version":"10.0.0","manufacturer":"","model_number":"","ga_client_id":null},"user":{"customer_id":"","is_logged_in":false,"uidx":"","segments":[]},"session":{"auto_id":null,"is_first_session":"0","server_offset":-1,"request_id":"f30535c0-5506-47d5-81ae-c3278d466753","landing_screen":"/campussutra","session_id":"24e5b2b3-8627-49e6-a1f2-ad491d211604-4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb","session_referrer":{"referrer_url":"","medium":"","source":"","channel":"direct"},"start_time":1722594943780},"app":{"name":"MyntraRetailWeb","build":-1,"react_bundle_name":"","react_bundle_version":"","version":""},"event_sequence":null,"payload":{"widget_items":{"data_set":{"data":[{"entity_name":"Campus Sutra Classic Self Design Spread Collar Casual Shirt","entity_id":28219632,"entity_type":"product","entity_optional_attributes":{"price":1899,"discounted_price":664,"discount":1235,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Women Olive Green Applique Detail Denim Jacket","entity_id":14862490,"entity_type":"product","entity_optional_attributes":{"price":2399,"discounted_price":719,"discount":1680,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Distressed Cotton Denim Shorts","entity_id":24442152,"entity_type":"product","entity_optional_attributes":{"price":1899,"discounted_price":759,"discount":1140,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Teal Green Classic Spread Collar Self Design Casual Shirt","entity_id":26712918,"entity_type":"product","entity_optional_attributes":{"price":1899,"discounted_price":664,"discount":1235,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Cable Knit Cable Knit Woollen Pullover","entity_id":25373430,"entity_type":"product","entity_optional_attributes":{"price":1999,"discounted_price":999,"discount":1000,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Blue Smart Light Fade Whiskers Cat Scratches Cotton Slim Fit Jeans","entity_id":22732960,"entity_type":"product","entity_optional_attributes":{"price":1899,"discounted_price":474,"discount":1425,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Grey & Black Colourblocked Track Pants","entity_id":16482190,"entity_type":"product","entity_optional_attributes":{"price":1799,"discounted_price":539,"discount":1260,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Teal Blue Printed Oversized T-Shirt & Shorts","entity_id":23563936,"entity_type":"product","entity_optional_attributes":{"price":2499,"discounted_price":874,"discount":1625,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}},{"entity_name":"Campus Sutra Men Regular Fit Yoga Track Pants","entity_id":17388400,"entity_type":"product","entity_optional_attributes":{"price":1799,"discounted_price":629,"discount":1170,"seller_partner_id":"4214","productMetaData":{"plaSlot":true,"plaReason":"PLA got exhausted","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"{\\"Tag\\":\\"MEXPRESS\\",\\"DeliveryBucket\\":\\"2DD\\"}","isUld":false}}},{"entity_name":"Campus Sutra Black Printed Oversized T-Shirt & Shorts","entity_id":23563952,"entity_type":"product","entity_optional_attributes":{"price":2499,"discounted_price":874,"discount":1625,"seller_partner_id":"4214","productMetaData":{"plaSlot":false,"plaReason":"","plaRank":0,"adSource":"","adsMeta":null,"lmsMetadata":"","isUld":false}}}]}},"screen":{"data_set":{"entity_name":"/campussutra","entity_type":"list"},"referer":{},"entity_type":"list","name":"Shopping Page - List Page /campussutra","url":"https://www.myntra.com/campussutra?f=Brand%3ACampus%20Sutra","type":"list","variant":"web"}},"client_id":"lzZNMYGoPkQVWOGL3wg81DLeJ4arpd","user_attributes":{"pin":"700028","pin_src":"ip"},"_t":"ProductListLoaded-ViewPort","time_stamp":1722594943781}]'

response = requests.post('https://touch.myntra.com/track-web', headers=headers, data=data)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'v': '1',
}

response = requests.get(
    'https://cdn.izooto.com/scripts/2d34f47ca3a13cbc90559ae77170feca968c14e4.js',
    params=params,
    headers=headers,
)


headers = {
    'Accept': '*/*',
    'Service-Worker': 'script',
}

response = requests.get('https://www.myntra.com/dsw.js', headers=headers)


headers = {
    'Referer': 'https://www.myntra.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

response = requests.get('https://cdn.izooto.com/scripts/workers/2d34f47ca3a13cbc90559ae77170feca968c14e4.js', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'FIREBASE_INSTALLATIONS_AUTH eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IjE6Nzg3MjQ1MDYwNDgxOndlYjpkMzlkNDgxZDNiMTBmN2UwYTUxODgwIiwiZXhwIjoxNzIyNzU0NjcxLCJmaWQiOiJlOTRDeTdvOGxyNmtNeDBsVHNMLVBpIiwicHJvamVjdE51bWJlciI6Nzg3MjQ1MDYwNDgxfQ.AB2LPV8wRAIgLUKcudvZmi32k3_So1yjlFc3Zqpd8rwAcurTlVYBDV4CIEupiyGX65FqNNYXfMsOaKf6aISj0YgTNs3Y9C40zWR8',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://www.myntra.com',
    'priority': 'u=1, i',
    'referer': 'https://www.myntra.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-client-data': 'CLC1yQEIj7bJAQiktskBCKmdygEI0aDKAQjY7soBCJKhywEIhaDNAQi8nc4BGPbJzQE=',
}

params = {
    'key': 'AIzaSyDAegtWIjzK09VsL5KH05nn-zzCSSql3H4',
}

data = '{"app_instance_id":"e94Cy7o8lr6kMx0lTsL-Pi","app_instance_id_token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IjE6Nzg3MjQ1MDYwNDgxOndlYjpkMzlkNDgxZDNiMTBmN2UwYTUxODgwIiwiZXhwIjoxNzIyNzU0NjcxLCJmaWQiOiJlOTRDeTdvOGxyNmtNeDBsVHNMLVBpIiwicHJvamVjdE51bWJlciI6Nzg3MjQ1MDYwNDgxfQ.AB2LPV8wRAIgLUKcudvZmi32k3_So1yjlFc3Zqpd8rwAcurTlVYBDV4CIEupiyGX65FqNNYXfMsOaKf6aISj0YgTNs3Y9C40zWR8","app_id":"1:787245060481:web:d39d481d3b10f7e0a51880","app_version":"0.5.7","sdk_version":"0.0.1"}'

response = requests.post(
    'https://firebaseremoteconfig.googleapis.com/v1/projects/valiant-airlock-578/namespaces/fireperf:fetch',
    params=params,
    headers=headers,
    data=data,
)


headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'access-control-request-headers': 'authorization',
    'access-control-request-method': 'POST',
    'origin': 'https://www.myntra.com',
    'priority': 'u=1, i',
    'referer': 'https://www.myntra.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

params = {
    'key': 'AIzaSyDAegtWIjzK09VsL5KH05nn-zzCSSql3H4',
}

response = requests.options(
    'https://firebaseremoteconfig.googleapis.com/v1/projects/valiant-airlock-578/namespaces/fireperf:fetch',
    params=params,
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': 'application/json',
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
}

data = '[{"ab_tests":{"config.bucket":"regular","Convenience_fee_logged_out_user":"enabled","hpmweb.mycoupons.revamp":"Revamp_ver1","coupon.cart.channelAware":"channelAware_Enabled","desktop.pla":"enabled"},"event_meta_version":"1.3.0","event_payload_version":"1.1.0","geo":{"lat":0,"long":0,"pincode":{"ip":"700006"}},"network":{"bandwidth":"-1.0","bandwidth_bucket":"UNKNOWN","carrier":"","ip":"","type":""},"device":{"advertising_id":"","build_number":"","installation_id":"","device_id":"4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb","height":864,"width":1536,"category":"desktop","os":"Windows","os_api_version":-1,"os_version":"10.0.0","manufacturer":"","model_number":"","ga_client_id":null},"user":{"customer_id":"","is_logged_in":false,"uidx":"","segments":[]},"session":{"auto_id":null,"is_first_session":"0","server_offset":-1,"request_id":"de517400-b949-4bb3-ae4d-d13868d0af63","landing_screen":"/campussutra","session_id":"24e5b2b3-8627-49e6-a1f2-ad491d211604-4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb","session_referrer":{"referrer_url":"","medium":"","source":"","channel":"direct"},"start_time":1722594945594},"app":{"name":"MyntraRetailWeb","build":-1,"react_bundle_name":"","react_bundle_version":"","version":""},"event_sequence":null,"payload":{"screen":{"data_set":{"entity_optional_attributes":{}},"referer":{},"entity_type":"list","name":"Shopping Page-List Page/campussutra","url":"/campussutra"}},"client_id":"lzZNMYGoPkQVWOGL3wg81DLeJ4arpd","user_attributes":{"pin":"700028","pin_src":"ip"},"_t":"realUserDetected","time_stamp":1722594945594}]'

response = requests.post('https://touch.myntra.com/track-web', headers=headers, data=data)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}



headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}



headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'key': 'AIzaSyCx80ru6-RXeTi3GvqkFsMVyMf-vpgIoVw',
}

data = '{"request_time_ms":"1722594959281","client_info":{"client_type":1,"js_client_info":{}},"log_source":462,"log_event":[{"source_extension_json_proto3":"{\\"application_info\\":{\\"google_app_id\\":\\"1:787245060481:web:d39d481d3b10f7e0a51880\\",\\"app_instance_id\\":\\"e94Cy7o8lr6kMx0lTsL-Pi\\",\\"web_app_info\\":{\\"sdk_version\\":\\"0.5.7\\",\\"page_url\\":\\"https://www.myntra.com/campussutra\\",\\"service_worker_status\\":3,\\"visibility_state\\":1,\\"effective_connection_type\\":4},\\"application_process_state\\":0},\\"trace_metric\\":{\\"name\\":\\"listPageLoadTime\\",\\"is_auto\\":false,\\"client_start_time_us\\":1722594943583900,\\"duration_us\\":99,\\"counters\\":{\\"ValueinMS\\":2408},\\"custom_attributes\\":{\\"pageBucket\\":\\"directLoad\\"}}}","event_time_ms":"1722594944677"},{"source_extension_json_proto3":"{\\"application_info\\":{\\"google_app_id\\":\\"1:787245060481:web:d39d481d3b10f7e0a51880\\",\\"app_instance_id\\":\\"e94Cy7o8lr6kMx0lTsL-Pi\\",\\"web_app_info\\":{\\"sdk_version\\":\\"0.5.7\\",\\"page_url\\":\\"https://www.myntra.com/campussutra\\",\\"service_worker_status\\":3,\\"visibility_state\\":1,\\"effective_connection_type\\":4},\\"application_process_state\\":0},\\"trace_metric\\":{\\"name\\":\\"_wt_https://www.myntra.com/campussutra\\",\\"is_auto\\":true,\\"client_start_time_us\\":1722594940990300,\\"duration_us\\":2811399,\\"counters\\":{\\"domInteractive\\":2044199,\\"domContentLoadedEventEnd\\":2355100,\\"loadEventEnd\\":2811399,\\"_fp\\":1297100,\\"_fcp\\":1297100}}}","event_time_ms":"1722594944679"}]}'

response = requests.post(
    'https://firebaselogging-pa.googleapis.com/v1/firelog/legacy/log',
    params=params,
    headers=headers,
    data=data,
)


cookies = {
    'at': 'ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWWpNeFkySm1NelF0TkdOaFpTMHhNV1ZtTFRreVlqZ3RNV1ZsTmpjd1pXTTVabUk1SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzTXpjM01ERTROamdzSW1semN5STZJa2xFUlVFaWZRLjcyUTBZczRVNFdjT09zaEhuQnNlRWRTb3pHS01oR2c3VDhHSEwyUkpiaFk=',
    '_d_id': '4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb',
    'mynt-eupv': '1',
    'x-mynt-pca': 'nH9mxtXUPchmnWDGbhXl9jaw-c5Vja_ovNGyjLbpRsDQIkl7OflPowdK8z8pxlicfpTpLHNuswY89SAkZ0oVceg_fRX_GCoVljGV-NLrKDUCeGRNSpaf2XMnYzvBI24aQdwXtGc0zx9tzATRW3LlN5Xa3EcQmrjYx43Q1R_Vq_62sBgai-E%3D',
    '_abck': 'FA360452C255EDEFEF91C657BB89268A~0~YAAQhonTF/LjvgSRAQAAcxgdEwyE/LEh9GKl38ZudhSq6wa3T/IXLSyfdUwnrS+9wIPZuVILXZK+soz+2wcrnKEnEW0SwAOFFuQY2fOQgfqV02CANtlB2PoBAMcpqLmrQIJ8+JKcJQ93aNpAvJkqQ5sQAmuzmYy5WIGFb6hba1GBzwVmRqUMtbNtOhupywl7cYTzzsQt5wf3BJXzXBZtMMnPuB1kKD6p1pu8L4X3AwXF20UsPLEAARIvKeLKrDcJ/vg3rKa45R+7WI7yZB8+4a+DEpDqOQpjzyKaw3ruMQdMyEl66gKaH4Sup9sTB0IE4x7VSXOk7kTv5hh4y0rHGKLkib1kBoF9oaj809R3n7PvR4f52vuMHvDBAzV7F2SVGmYFWG7HouFLwJx0DJVjFvAINZE7BolJ~-1~-1~-1',
    'ak_bmsc': '7865A8C846C71BBC8D985C0215B2B59F~000000000000000000000000000000~YAAQhonTF/PjvgSRAQAAdBgdExiJGXSqRp5sA+TfUYcGx1gN+ZF173fjsnsWHlgRCpQm/hpsQ+LTqc05mwERop+tn8hUdOah482rQC5hm1XPNUvCCVVtsuX0J7Oa2Xf/0T20yupkxeSdhYaxHwwYkLcWS1mnm2v5tOCZnJ1Mdr3OaEVbEzs4YRgg1dOzHQFJOV/PnuAIYMTdtJpsyt3mkWUqNmWoJa90QqpGb+19/yuhGJv/ymQJRiKMwpJU1A9AYtORv4pYYp+muAKV3K2/shpq+g7HUf+3sv1rTcEhGouQVAV/RVH57ApnY7zeDSNoKJPs85qrULct9O4l3ga/ScnwU+aDSaA/3P1I9chjiOui6qELzjXQCKXHiMmbQP104fqQG5Te7/+Toos=',
    'bm_so': 'D68DAB1621A251A648201BDE107521B6B6209431DD5B99BA2D4AD08D924A3406~YAAQhonTFyvxvgSRAQAANo8dEwAYqeJoxQ/F/1o0ki2iohltM/Ew9vMA8zLXbg2/oHU+MgfFu9I6f2dnmCwWaM6060mXk859Hf9xh4MyldLTAe7eebmh2rc1/wIrBlG8bLQXrA8iY8f9Y4VAPX3Dav7/sp2ew6zAu8/txGOdK2nuUNcQxgYG5mGLjDTIxMqblL6swj3pL9+BPTrsz0nM45zEJxHgH7SQeIOOH8Gkm5HHmhWLB+Z6wdaZchNg4HVtO0Z1GFEXgVL6ZczthYmM2c2niapiXRp9KoffPAtfeVQ5fsGFwqgNY9ODqCBZqzmqW4ld1gjdG1Ff959twCXrgMIu4E58ERC5WZovKiFJGyf7wBv+8uKQILVHW8NGW7dIFoF3jqf1QljTp9vil51Ie5WAQq8zi9MB2eh6GvBnDDE4CGwjPHKJIZPXxE/BX5rxqqN30nQLIl31oOvbEHr/JORApClwKDBM/inwZLFx1mV5K2prDGXCS4i5J5CUFd+zTy0lh34p08+ibYbTFxqdvJHzChALoC8Lcdg1DSxgofGalsDWSlKspnrijRWC1l4zdsf0O6Vur3Hqijby9Xph/XI=',
    'bm_s': 'YAAQhonTF/PxvgSRAQAAw5cdEwHy3ZYGzc+lDcrZ7kpOYOF7FdP7JWYPTDMcXd/lAUYgjNCXVRbNz+8Od/OwyPinhtW6qhA4q7zr4PJatNig0cPdKKoBeQjqzFZCpcvIQwWytZjO9QfxWXwzoh0mbtCOc3zfNTfgfV5Ugwx6TQDivCWWWiYzkjYK74m1+y3BgElVeP+BfqNJUxmU33a3JoiZav+ExlM0JLoZiAtNxkvAn3KTh3cEyWqg8hb07RyU2tJs5mwJllOqpuZjwMevLRfJM/RJ6t/ciFJthJ/07Zi+lQE5fLG+0dKQ961Kcmm6bC7KdPJuMUllzzadtQ5hUNlVsHnpxg==',
    '_mxab_': 'config.bucket%3Dregular%3BConvenience_fee_logged_out_user%3Denabled%3Bhpmweb.mycoupons.revamp%3DRevamp_ver1%3Bcoupon.cart.channelAware%3DchannelAware_Enabled%3Bdesktop.pla%3Denabled',
    '_pv': 'default',
    'dp': 'd',
    'utm_track_v1': '%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1722609502%2C%22trackend%22%3A1722609562%7D',
    'lt_timeout': '1',
    'lt_session': '1',
    'bm_mi': 'A115AA5B731B71D422B24C4428E04264~YAAQlwHVF2Lt3AGRAQAABQmHExjR9578aWKHyWbzM9wDHzKo/hz81mIQ3ErvGijhbAiCgYDfB8reGPj5cZwe5Yu82RhdK+44llWLAEPpUjRRAw6CY3er0PnOhRsAqyffF3pOffwQmUhVWQ1RlpCFRAik3lRWfPElaBwYum39WlfOO0r4lUfwBpFoBUucKf4pVRefMzmOHxSVnVzLQeK8IcZXgc0SMF5SfmbLJ/hfgMFI4kZRB+9r9GNbw9ljzC8rNUeK3tZ6spIQrAlOz34H81VYS5m+dcU5ZlGa0mdfb/rJWWgkN95ZHQthdCKIWvJgRxHfq/frjME0~1',
    'bm_sz': 'A5EC6853C490094A0A83E20B00D33818~YAAQlwHVF2Tt3AGRAQAABQmHExjMoDthcfPAVwqfMRMwQsNaV+Crp8bQAbHNU9W6pqH7CBMUh7eKS9MD0hTrre45+D2EC/FuzB9YPgkhGzdoXyF7WZZoq7z6b15sLlFe9tBxDkBE5n1enGNj/Na8fwjd6xgIxySGySauUKXJ6b+ponBrlOV78B4pN1dDgr6k+lFe7cKkhXQUBuHLn0IpmM47N39/CTgUWmTJlks0ZOiyBnnq/jfUfdal4WROynOV6bbO+HrpN1C62iDml6GBYcUBrpu6T/C+bwsqNUJwFfR28xAl+ACDK11j+3OhCp6wl1qB6zyQqD064cEjD6LXpmE0CUEZ7nsaL8WeJG6UA9pmHJmYoaxMybwBBG5CNLIPODNxlf28Qz9iTCxgol8Jpsfd5dgXc06n1W0YQljQeHw=~3224624~3618869',
    '_ma_session': '%7B%22id%22%3A%22ed72b826-0a87-4f89-bb20-74cca965dfa9-4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D',
    'microsessid': '519',
    '_xsrf': 'cvCLA6rxBiReARWA3hpPJUJ8TpZ3V1GV',
    'user_session': 'JbSwYkbR7VuTIH6jRslK5w.Hv6yZ6QRkd6XX5anaV6GsrT7YpjJBTsyfV_krlxqqS16lJTy81bXI6-yOWAxTWQu54c-6TIlywh34YXsjDHN0oECsicDPtApbpjDD7lDmcZe6Vh-cfH5CnW1lJg6Aiu9P6s4PwOanLNnSykWSvH7Mw.1722609503843.86400000.4dTIfDFPQI3OvZvlIjqz7c0qghE1XScp2LqWGcxBTH0',
    'mynt-ulc-api': 'pincode%3A700028',
    'mynt-loc-src': 'expiry%3A1722610944378%7Csource%3AIP',
    'utrid': 'YXsBQ2VaTE0DdU9oUHZAMCMxOTI2MTgyMDk1JDI%3D.d35ab534faf738e1c09883d29b4737ea',
    'bm_sv': '8439DEF48C6F77C1D15C3279536E9CD8~YAAQlwHVF7Pt3AGRAQAAixSHExg2sBh4chFwS3WEnHCw5YpdoAqijHYxrDRwYSceDh9Dr4JJRA7Eyr6ae0pw5OhlA7G7rerPmcEvSnJT/v2LkuO/u30bYlkiZIt0ta0F2zkphWyu2APExt1dasfArLMdiChud26m2liP6cSOBu9tQFefX3zSLkZP39SfMvdiTWZELTbS30yqqQjZ3HF4oSWRj0HQO6JCiDUGHeJIyEbshk43uovP4pP6RZxn8pHz+w==~1',
}


headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'app': 'web',
    'content-type': 'application/json',
    # 'cookie': 'at=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWWpNeFkySm1NelF0TkdOaFpTMHhNV1ZtTFRreVlqZ3RNV1ZsTmpjd1pXTTVabUk1SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzTXpjM01ERTROamdzSW1semN5STZJa2xFUlVFaWZRLjcyUTBZczRVNFdjT09zaEhuQnNlRWRTb3pHS01oR2c3VDhHSEwyUkpiaFk=; _d_id=4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb; mynt-eupv=1; x-mynt-pca=nH9mxtXUPchmnWDGbhXl9jaw-c5Vja_ovNGyjLbpRsDQIkl7OflPowdK8z8pxlicfpTpLHNuswY89SAkZ0oVceg_fRX_GCoVljGV-NLrKDUCeGRNSpaf2XMnYzvBI24aQdwXtGc0zx9tzATRW3LlN5Xa3EcQmrjYx43Q1R_Vq_62sBgai-E%3D; bm_so=E109E85282B2EDF1E26153975A59FFAE6442F951FCDF85BE3175DFB4A8619B05~YAAQjInTFxWXr+6QAQAAo+S4DwAdc9vA9ij+VOThLf5JjS+2IBvz3pawfnK2IGki5GdnWZSQsV3yw+HzZHRTU3HJYmEurWPNcsyJksBpzqx3457t8JX3fMu6OxWXA2mXues2Wwk1YluQ3wEKAw5EQ0Gb9dR12AS8lmuCLc27fEO3+bexdUiAX7r4nX8IBbpC/5INTge4ATgv3Ice6RdaSEyNtWZEi2Z8fxeJHV+3c8oegRxZrRoRBm7qDofm04Yrb7gfva9XsDrl2KdpaJBfeqdq+ZIyis5yVp/zFi7lgS7WANCyJtyeIEOmAwQx5G+rNtDVeWxd+3vO2jehD2zUqd7vAcViY1QqeTzepwEYtOhmvJ/UDV1xa8j7q0RXEiixSp/E6PaQPdKHEJR5y9pXrcAwpDJ3THXu6gMwGPkydnP+OqGeas+GmEj4XgdtaRv4XMEv95ceiG00EEmNSM0PYiRYbs3lcZ8Ib8KBdpWp6Umj+kqybg+YX2SK/YelbJegMzc2lMP7KP7FC3D+zRkEzorndI1DsnF+xaSK4n7iVtDw7h/40F7uurWe9Ghu0BVyByc9fvlm6CVo5oNdBy5/Zho=; bm_s=YAAQjInTF1GXr+6QAQAArum4DwEmTXiC/UubYUGVeSPuoiawy6zYxDOj6JWJqHzFv7povcf4HGVn/8vP8IqyBNpmdWfYBlX4NWKyLaT6z4fj5Vg2EnXcgMFxxsu16JbKW+6G80UKk4M1wlgN8140UND2Eq7/C+BwJdMgsmj3xW2yYx2HNoOBhiFRyMGxkNIYh6rhkj9oiGpY0KHVYA3Yd348IMcKPrwhiDhYs5WaRyecbvu69jP67grpKRKMGbhfjd3zvz+8nrvjC3nVpId+QHtwjL0zvxS0KpKRttrS2Fva8w5LELnC8uO8eIwFQDqGc4z5EdPfldJJ0T+lfCn7bho8FSqJzA==; _abck=FA360452C255EDEFEF91C657BB89268A~0~YAAQMTXZFzx3ev6QAQAAZ5EWEgxHmf788Nrszbjhk4pmzdsCg+nlkFRyIrUOZrPQ/ZsTcxV0Kh3tAlsj/PnmZIXTtq+nwgKqkWBOfvF5eTel7vA6vtW7/vdFR1zwGqrBJLUhALDtJofrJOjVJr/sB+cSYBJ9zpQT+5qjH0Rr525Fxgvtn4qf1EI6KPIZXzKAVbGPgsAUHaAIyHON/IG39v5E/NMAFEtvbUjOQHip+qC4lc94j3Z308VtRu8VWxnZLbtifDyrzqRNI1zYGi1Of9xgupExd265LO3fnPgEBL1JYrWogfwmBKLPaKvO2rJIRdFXvM6RY8pPfSDmj1iIOLjfp6CL+2QiOHauH8M8w5WDn6QjmKDaOaGD3kbjxScMQxFCbQBldDa7Wy76MbvfYe02iPRy5ZLN~-1~-1~-1; _mxab_=config.bucket%3Dregular%3BConvenience_fee_logged_out_user%3Denabled%3Bhpmweb.mycoupons.revamp%3DRevamp_ver1%3Bcoupon.cart.channelAware%3DchannelAware_Enabled%3Bdesktop.pla%3Denabled; _pv=default; dp=d; utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1722594941%2C%22trackend%22%3A1722595001%7D; lt_timeout=1; lt_session=1; ak_bmsc=BF2EDE66000C6058D5751985832A7489~000000000000000000000000000000~YAAQnonTF4YV/QWRAQAAZ9uoEhi5FSb9qYX0FMl1P6dwxEYr1vtIKJtpAkP6L3k9mjt8+xsPfdCb2TzO1C4JVGCPRm4RJwb9s93fQFoRDNHnwrcgq8bV/RrrELq9HyEPNLTByAPuoKJ7iWwGBl4MzEc8Fgdm8qnA4zH81ZP5fRNgiY/zWIF8h7mCJ0Pp4iDV5JceoMBoJZw/V88AJlUG4IFxYcokaTNdirEeZISzJXADtxrve1az7R/F7r2lMrX2X2w7ECKHR+ox1mpEECPtRiu2T1D+xt4nPCGjSRqKEis4vJMrWZsegR6i0oKzwbpaBuVA7OHMS7/Q5exXJhUyrua6XY0OpwzbzMcJqKkXUSRL65RGk9dhJeJZ5qoD+SZp9FIXxOA2HNFuz70=; bm_sz=8A68F248AAC0E85AA8CBA64AEB42542F~YAAQnonTF4gV/QWRAQAAZ9uoEhhzYCajhFTVMfYG2xdwa3UFFUeB941H6k70xIp79KP5PuM+vjY9ZBgPFVUneKmHLbs8gNLHzi6efot2P4A0sKa9mxwkqtjip9pA33geC5q73nQjtlkL3J/Rngodxlg/SaotGa4JAqkHAhlAeyqiGcCaIsXm8VvWrd90qopsqMsGzknflipTGfhCyCJfyvnOXseQnkCY7MxCp0no5/iwwkf3H05tLVT2eL2LbflyxGiSSx5Dv5T3Xe7c7UV2o8vW1lX69iAlH33mlcDvBgBWJFyQHdDh1d3DDykXItWhfvc2PYGppYnnV807K/lQelRJSlckowHp+g4MG1omssiJ57szPQsaWxpjeRPSHY57OBEyRGIU71gW/D5r98DwPXGZnss5t50VJT0=~4469045~4403522; bm_mi=E1C38B8B15A4FF2ACA93FED9E88819B2~YAAQnonTF7MW/QWRAQAAROGoEhjeEpFIKC/ckJxmhCFrdKEGEM8x+ml649lEhFpa+uqxRlqZ0lJfteKZJtwJ1KU1ilk+wtuGtLcDbP+qXGFbodm1L4/UyIYMB+qnSxAnezRYAZTOEphoIyfNQj6iRT7jfBtDzhQJHQicF2Jexsmh4LpKL/Fd/kJyGjyfTqFN+yp7zOyFCs4eaY+gWiCPe2KjbgZbFaI2/p3BnpKFygGFPYwFwYj5Sde6PJW/3gIEMH4ZK9A4yaVwcipNDoDL2LBsuWnMTmBx9UaGOEN02lRbXv8tqeQ/u9Lo2iq0vIxlPOumtJX6IEWYIOmvzqyImd/R6Tfv0AVv3jK3Qu0TUFDsQg==~1; _ma_session=%7B%22id%22%3A%2224e5b2b3-8627-49e6-a1f2-ad491d211604-4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D; microsessid=608; utrid=FUBeGWdVV2YVcllMAEdAMCMxNzYwOTY1MTQyJDI%3D.05712306d85dcc36bba8d375775e5757; _xsrf=AHxlYBKiiN0vhYxDcpoU33VlEgykjoCt; user_session=yZAnm9cKDEs-6PdDRL22gQ.VdL0Nqan_t5Dx4Avhi9x8vCltu5Y2qjrikC13QVRgLRzovxbWeAooNtoEdzeLS4RU4OkkLGzCwUvJ7ZL4RutU8NlnBgKbwFDKq_QL-CnVLTo1O8DwImpu2vF2qExCJna3vWBLRflLtdWfFDfZIPMTQ.1722594943643.86400000.bIkAGjWW_xYP13qoSs2CJlmiO_qa_ydH-N8NYdCN1MM; mynt-ulc-api=pincode%3A700006; mynt-loc-src=expiry%3A1722596383657%7Csource%3AIP; bm_sv=562DEBB8644A469B2AF626405AE8728C~YAAQnonTF1gX/QWRAQAAMOSoEhho4VcerTNVnUKsDSl6mAhtp9hdSuzoBLwcYEEsbMb7aLbVIi/5DHBlf0WsQ9pnSz0X/FAEXGmVXLIw2EtA8IMrDiFz6bwGZWVRhtNi3P6cF/wYGoHBb0QRvlBoB6xp8r/nvd4IU9tUIRwmPIrPPLJOd3dPcRJq8EnH8fbazmSN3svuiGodaHfcbq+BDCoUpZ3212kvVMRU1wQnVI+DrnZmx4Up/RavhQeEpnxg~1',
    'pagination-context': '{"v":1.0,"productsRowsShown":0,"paginationCacheKey":"5a4033eb-943a-4d05-8891-1fd019d29ce8","inorganicRowsShown":0,"plaContext":"eyJwbGFPZmZzZXQiOjAsIm9yZ2FuaWNPZmZzZXQiOjUwLCJmY2NQbGFPZmZzZXQiOjAsIm9yZ2FuaWNDb25zdW1lZENvdW50IjoxMjgsImFkc0NvbnN1bWVkQ291bnQiOjAsInBsYXNDb25zdW1lZCI6W10sImFkc0NvbnN1bWVkIjpbXSwib3JnYW5pY0NvbnN1bWVkIjpbXX0\\u003d","refresh":false,"scOffset":0,"reqId":"5a4033eb-943a-4d05-8891-1fd019d29ce8"}',
    'priority': 'u=1, i',
    'referer': 'https://www.myntra.com/campussutra?f=Brand%3ACampus%20Sutra',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-location-context': 'pincode=700006;source=IP',
    'x-meta-app': 'channel=web',
    'x-myntra-app': 'deviceID=4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb;customerID=;reqChannel=web;appFamily=MyntraRetailWeb;',
    'x-myntraweb': 'Yes',
    'x-requested-with': 'browser',
}

params = {
    'f': 'Brand:Campus Sutra',
    'rows': '50',
    'o': '49',
    'plaEnabled': 'true',
    'xdEnabled': 'false',
    'pincode': '700028',
}

response = requests.get('https://www.myntra.com/gateway/v2/search/campussutra', params=params, cookies=cookies, headers=headers)




import requests

headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'onload': 'init',
}

response = requests.get('https://apis.google.com/js/platform.js', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://clientcdn.pushengage.com/core/1984.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'id': 'GTM-KGJPN7D',
}

response = requests.get('https://www.googletagmanager.com/gtm.js', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.google-analytics.com/analytics.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://clientcdn.pushengage.com/core/1984.js', headers=headers)


cookies = {
    '__Secure-3PAPISID': '7c1ChnDwe6MLcM2_/A5Zm2qyn_JXTSHFUq',
    '__Secure-3PSID': 'g.a000mAhz3VP0EIAOvjsYPNr-mJoU_K2VLtJMHsqryQJv4e7P9ai856kKCsHDmDeaT0F21q8-RgACgYKAYQSARESFQHGX2MiRwlXJEA_OYOgemVER9XLghoVAUF8yKqRzTZLjdOB6c2aR9ERucFO0076',
    'NID': '516=bCwRo2fGH4IxHlxc59Clva9Zz-_JqE4uFVJNyr8AICB7k1qsCRtQefr1Bv5IhhMC1g77A4_B7M7C_12V2__XJ7fai55H3g1Y5IBafB8M1vsFg7O9BKN9TRsNcMItkAGCDLV0429ddOhZVm2buFhgW7JV_hcL37QXCoU9FH7X6XagLH_hRwHDykcxOD7KGvuGL0OVQ5spOxh1jUJapUzvXsOm9quD1EI58KYKOHNAFxPq48dUTilWQjN7pnwbW3xXpsDDCxZ-Lqg1EnPXqbRelnCgohm-FwlZ8jAoxNO61-GeYKZk4hfCJhoS5EO4e_BgnmwfUGYMaSqTqoAPdOeXjt1mn0-edPkortKgCeD4OjAQESRNtbZEDvAiGKiCEz31hQ',
    '__Secure-3PSIDTS': 'sidts-CjEB4E2dkVyMc3nzNOLHTdAbQiSIee3colWawi3ns4nB6aRgrALhMyC3ey35OHz0ylYLEAA',
    '__Secure-3PSIDCC': 'AKEyXzVxWPvWnJgzP5n6xYez3Oigv9ttGG8qW3dhzGnk13QdElj8N5ZGTBMR_t37C_XgMqCmeg',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': '__Secure-3PAPISID=7c1ChnDwe6MLcM2_/A5Zm2qyn_JXTSHFUq; __Secure-3PSID=g.a000mAhz3VP0EIAOvjsYPNr-mJoU_K2VLtJMHsqryQJv4e7P9ai856kKCsHDmDeaT0F21q8-RgACgYKAYQSARESFQHGX2MiRwlXJEA_OYOgemVER9XLghoVAUF8yKqRzTZLjdOB6c2aR9ERucFO0076; NID=516=bCwRo2fGH4IxHlxc59Clva9Zz-_JqE4uFVJNyr8AICB7k1qsCRtQefr1Bv5IhhMC1g77A4_B7M7C_12V2__XJ7fai55H3g1Y5IBafB8M1vsFg7O9BKN9TRsNcMItkAGCDLV0429ddOhZVm2buFhgW7JV_hcL37QXCoU9FH7X6XagLH_hRwHDykcxOD7KGvuGL0OVQ5spOxh1jUJapUzvXsOm9quD1EI58KYKOHNAFxPq48dUTilWQjN7pnwbW3xXpsDDCxZ-Lqg1EnPXqbRelnCgohm-FwlZ8jAoxNO61-GeYKZk4hfCJhoS5EO4e_BgnmwfUGYMaSqTqoAPdOeXjt1mn0-edPkortKgCeD4OjAQESRNtbZEDvAiGKiCEz31hQ; __Secure-3PSIDTS=sidts-CjEB4E2dkVyMc3nzNOLHTdAbQiSIee3colWawi3ns4nB6aRgrALhMyC3ey35OHz0ylYLEAA; __Secure-3PSIDCC=AKEyXzVxWPvWnJgzP5n6xYez3Oigv9ttGG8qW3dhzGnk13QdElj8N5ZGTBMR_t37C_XgMqCmeg',
    'if-none-match': '"e17ec99fff31b210"',
    'priority': 'u=4, i',
    'referer': 'https://www.ajio.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-client-data': 'CLC1yQEIj7bJAQiktskBCKmdygEI0aDKAQjY7soBCJShywEIhaDNAQi8nc4BGPbJzQE=',
}

params = {
    'onload': 'init',
}

response = requests.get('https://apis.google.com/js/platform.js', params=params, cookies=cookies, headers=headers)


headers = {
    'Referer': 'https://www.ajio.com/sw.js',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

params = {
    'query': ':newn:brand:Campus Sutra:occasion:Casual:l1l3nestedcategory:Men - Shirts:l1l3nestedcategory:Women - Shirts:genderfilter:Men:rating:4 star & above',
    'classifier': 'intent',
    'gridColumns': '5',
    'segmentIds': '',
}

response = requests.get('https://www.ajio.com/b/campus-sutra', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://connect.facebook.net/en_US/sdk.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://connect.facebook.net/en_US/sdk.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'Origin': 'https://www.ajio.com',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://assets.ajio.com/static/assets/fonts/SourceSansPro-Regular--70479481cd786114774c92e8d04a4028.70479481cd786114774c92e8d04a4028.woff',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://assets.ajio.com/static/img/wishlistIcon.svg', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'Origin': 'https://www.ajio.com',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://assets.ajio.com/static/assets/fonts/Lora-Regular--12c052959e60357f292b2bed94162d01.12c052959e60357f292b2bed94162d01.woff',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'Origin': 'https://www.ajio.com',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'hash': 'a14589a821da1f4b9d501ae2a56c7643',
}

response = requests.get('https://connect.facebook.net/en_US/sdk.js', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'Origin': 'https://www.ajio.com',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'hash': 'a14589a821da1f4b9d501ae2a56c7643',
}

response = requests.get('https://connect.facebook.net/en_US/sdk.js', params=params, headers=headers)


cookies = {
    '__Secure-3PAPISID': '7c1ChnDwe6MLcM2_/A5Zm2qyn_JXTSHFUq',
    'LSOLH': 'AH+1Ng3+VjjzicQyKNga4mxgJCDk9AnLA6gRfkzn2TWaeIdrdxWAe0sW7gfg/x8anwXW/NYiXGJ7',
    '__Secure-3PSID': 'g.a000mAhz3VP0EIAOvjsYPNr-mJoU_K2VLtJMHsqryQJv4e7P9ai856kKCsHDmDeaT0F21q8-RgACgYKAYQSARESFQHGX2MiRwlXJEA_OYOgemVER9XLghoVAUF8yKqRzTZLjdOB6c2aR9ERucFO0076',
    '__Host-3PLSID': 'o.drive.google.com|o.lens.google.com|o.mail.google.com|o.myaccount.google.com|s.IN|s.youtube:g.a000mAhz3Skjbys2iNi9lIStH2ZpaUfzXJGrFWKXu6IqFVLgwlWQEVpemqz2wvqtokCe0UOm8wACgYKAS0SARESFQHGX2MiNgJ77yFDMZ-Si4ZEEuRaJBoVAUF8yKp5aSo57F0J5BuvhEqUo1Pr0076',
    'NID': '516=bCwRo2fGH4IxHlxc59Clva9Zz-_JqE4uFVJNyr8AICB7k1qsCRtQefr1Bv5IhhMC1g77A4_B7M7C_12V2__XJ7fai55H3g1Y5IBafB8M1vsFg7O9BKN9TRsNcMItkAGCDLV0429ddOhZVm2buFhgW7JV_hcL37QXCoU9FH7X6XagLH_hRwHDykcxOD7KGvuGL0OVQ5spOxh1jUJapUzvXsOm9quD1EI58KYKOHNAFxPq48dUTilWQjN7pnwbW3xXpsDDCxZ-Lqg1EnPXqbRelnCgohm-FwlZ8jAoxNO61-GeYKZk4hfCJhoS5EO4e_BgnmwfUGYMaSqTqoAPdOeXjt1mn0-edPkortKgCeD4OjAQESRNtbZEDvAiGKiCEz31hQ',
    '__Secure-3PSIDTS': 'sidts-CjEB4E2dkVyMc3nzNOLHTdAbQiSIee3colWawi3ns4nB6aRgrALhMyC3ey35OHz0ylYLEAA',
    '__Secure-3PSIDCC': 'AKEyXzVxWPvWnJgzP5n6xYez3Oigv9ttGG8qW3dhzGnk13QdElj8N5ZGTBMR_t37C_XgMqCmeg',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': '__Secure-3PAPISID=7c1ChnDwe6MLcM2_/A5Zm2qyn_JXTSHFUq; LSOLH=AH+1Ng3+VjjzicQyKNga4mxgJCDk9AnLA6gRfkzn2TWaeIdrdxWAe0sW7gfg/x8anwXW/NYiXGJ7; __Secure-3PSID=g.a000mAhz3VP0EIAOvjsYPNr-mJoU_K2VLtJMHsqryQJv4e7P9ai856kKCsHDmDeaT0F21q8-RgACgYKAYQSARESFQHGX2MiRwlXJEA_OYOgemVER9XLghoVAUF8yKqRzTZLjdOB6c2aR9ERucFO0076; __Host-3PLSID=o.drive.google.com|o.lens.google.com|o.mail.google.com|o.myaccount.google.com|s.IN|s.youtube:g.a000mAhz3Skjbys2iNi9lIStH2ZpaUfzXJGrFWKXu6IqFVLgwlWQEVpemqz2wvqtokCe0UOm8wACgYKAS0SARESFQHGX2MiNgJ77yFDMZ-Si4ZEEuRaJBoVAUF8yKp5aSo57F0J5BuvhEqUo1Pr0076; NID=516=bCwRo2fGH4IxHlxc59Clva9Zz-_JqE4uFVJNyr8AICB7k1qsCRtQefr1Bv5IhhMC1g77A4_B7M7C_12V2__XJ7fai55H3g1Y5IBafB8M1vsFg7O9BKN9TRsNcMItkAGCDLV0429ddOhZVm2buFhgW7JV_hcL37QXCoU9FH7X6XagLH_hRwHDykcxOD7KGvuGL0OVQ5spOxh1jUJapUzvXsOm9quD1EI58KYKOHNAFxPq48dUTilWQjN7pnwbW3xXpsDDCxZ-Lqg1EnPXqbRelnCgohm-FwlZ8jAoxNO61-GeYKZk4hfCJhoS5EO4e_BgnmwfUGYMaSqTqoAPdOeXjt1mn0-edPkortKgCeD4OjAQESRNtbZEDvAiGKiCEz31hQ; __Secure-3PSIDTS=sidts-CjEB4E2dkVyMc3nzNOLHTdAbQiSIee3colWawi3ns4nB6aRgrALhMyC3ey35OHz0ylYLEAA; __Secure-3PSIDCC=AKEyXzVxWPvWnJgzP5n6xYez3Oigv9ttGG8qW3dhzGnk13QdElj8N5ZGTBMR_t37C_XgMqCmeg',
    'priority': 'i',
    'referer': 'https://www.ajio.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-client-data': 'CLC1yQEIj7bJAQiktskBCKmdygEI0aDKAQjY7soBCJShywEIhaDNAQi8nc4BGPbJzQE=',
}

response = requests.get('https://accounts.google.com/gsi/client', cookies=cookies, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.gstatic.com/firebasejs/7.6.1/firebase-app.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://accounts.google.com/gsi/client', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.gstatic.com/firebasejs/7.6.1/firebase-app.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'id': 'GTM-5XMX63',
}

response = requests.get('https://www.googletagmanager.com/gtm.js', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://mercury.akamaized.net/jioads/retargeting/default/1_2_3/jioAds.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'id': 'GTM-5XMX63',
}

response = requests.get('https://www.googletagmanager.com/gtm.js', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://mercury.akamaized.net/jioads/retargeting/default/1_2_3/jioAds.js', headers=headers)




cookies = {
    'V': '201',
    'A': 'eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJjbGllbnQiLCJjbGllbnROYW1lIjoid2ViX2NsaWVudCIsInJvbGVzIjpbeyJuYW1lIjoiUk9MRV9UUlVTVEVEX0NMSUVOVCJ9XSwiZXhwIjoxNzI0MDUxNDM3LCJpYXQiOjE3MjE0NTk0Mzd9.stU2wLuFoJIP5yKgy9LqMbGy-H8JkBZL_MWGMDOjIq9W7XXl0Mdx4A3pxCIRQJskED5fkPc5kwlpYGJf4s0HTIdXhAG62wo7_Ro6bCd9X4Es5zr_B9HBK6gf_7tKBhe3HxdNMoKXZZY0oVArgp9E2YUy5uMicCGDjUufWppyOyHqQ4pt1fGNY_Gs680USZ0B6J1wYz5fmkfGU9VX7RLwVxNDkxpUhyCE197RyV4khHu8p4ui1X_GMam5GtRa8f7eaLuQQ5RzpLIiT1wyoMGFGRA6Qvx7i5oZxcsKYTAsZGXWWuvIfzWXs3VHLpXmdZPyHJRdSkoOyLfKsxSZ14f4kA',
    'U': 'anonymous',
    'TS01ac9890': '01ef61aed0a15ed3b0a4da4423f10e946e2d060a744782ab1fdc489cf6d7bd40826d68f7a0db8d351a9484e47a27e657ac5026304e',
    '_fpuuid': 'oSgjFQp888RFeksofgGgP',
    'deviceId': 'oSgjFQp888RFeksofgGgP',
    'jioAdsFeatureVariant': 'true',
    'recentlyViewed': '[{"id":"463779234_yellow","store":0},{"id":"466380767_yellow","store":0},{"id":"466065907_black","store":0},{"id":"700129394_brown","store":0},{"id":"463775643_blue","store":0}]',
    '_ga': 'GA1.2.407987584.1722876649',
    '_gid': 'GA1.2.161608813.1722876649',
    '_gcl_au': '1.1.465699326.1722876652',
    'sessionStatus': 'true|undefined',
    'FirstPage': 'Mon Aug 05 2024 22:20:51 GMT+0530 (India Standard Time)',
    'AB': 'B',
    'cdigiMrkt': 'utm_source%3A%7Cutm_medium%3A%7Cdevice%3Ad%7Cexpires%3AWed%2C%2004%20Sep%202024%2016%3A50%3A52%20GMT%7C',
    'ADRUM_BT': 'R:26|i:4822|g:b0ff639a-571a-47f9-bf4d-5a0af7adb15223124857|e:348|s:f|n:customer1_be12de70-87be-45ee-86d9-ba878ff9a400',
    'TS01de1f4a': '01ef61aed03ff042da1eb92e93e9e4a69ad3b96840b393e31e1b3e8f51bde5675550683719da59feb2b2c45ffe638019358d86ef5c331c1cba2eba3d56b97f0de618b37849cb03aee234702b253e77b861c1cebceeffececf3276bc144e14aad2eebee7400',
}

headers = {
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'V=201; A=eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJjbGllbnQiLCJjbGllbnROYW1lIjoid2ViX2NsaWVudCIsInJvbGVzIjpbeyJuYW1lIjoiUk9MRV9UUlVTVEVEX0NMSUVOVCJ9XSwiZXhwIjoxNzI0MDUxNDM3LCJpYXQiOjE3MjE0NTk0Mzd9.stU2wLuFoJIP5yKgy9LqMbGy-H8JkBZL_MWGMDOjIq9W7XXl0Mdx4A3pxCIRQJskED5fkPc5kwlpYGJf4s0HTIdXhAG62wo7_Ro6bCd9X4Es5zr_B9HBK6gf_7tKBhe3HxdNMoKXZZY0oVArgp9E2YUy5uMicCGDjUufWppyOyHqQ4pt1fGNY_Gs680USZ0B6J1wYz5fmkfGU9VX7RLwVxNDkxpUhyCE197RyV4khHu8p4ui1X_GMam5GtRa8f7eaLuQQ5RzpLIiT1wyoMGFGRA6Qvx7i5oZxcsKYTAsZGXWWuvIfzWXs3VHLpXmdZPyHJRdSkoOyLfKsxSZ14f4kA; U=anonymous; TS01ac9890=01ef61aed0a15ed3b0a4da4423f10e946e2d060a744782ab1fdc489cf6d7bd40826d68f7a0db8d351a9484e47a27e657ac5026304e; _fpuuid=oSgjFQp888RFeksofgGgP; deviceId=oSgjFQp888RFeksofgGgP; jioAdsFeatureVariant=true; recentlyViewed=[{"id":"463779234_yellow","store":0},{"id":"466380767_yellow","store":0},{"id":"466065907_black","store":0},{"id":"700129394_brown","store":0},{"id":"463775643_blue","store":0}]; _ga=GA1.2.407987584.1722876649; _gid=GA1.2.161608813.1722876649; _gcl_au=1.1.465699326.1722876652; sessionStatus=true|undefined; FirstPage=Mon Aug 05 2024 22:20:51 GMT+0530 (India Standard Time); AB=B; cdigiMrkt=utm_source%3A%7Cutm_medium%3A%7Cdevice%3Ad%7Cexpires%3AWed%2C%2004%20Sep%202024%2016%3A50%3A52%20GMT%7C; ADRUM_BT=R:26|i:4822|g:b0ff639a-571a-47f9-bf4d-5a0af7adb15223124857|e:348|s:f|n:customer1_be12de70-87be-45ee-86d9-ba878ff9a400; TS01de1f4a=01ef61aed03ff042da1eb92e93e9e4a69ad3b96840b393e31e1b3e8f51bde5675550683719da59feb2b2c45ffe638019358d86ef5c331c1cba2eba3d56b97f0de618b37849cb03aee234702b253e77b861c1cebceeffececf3276bc144e14aad2eebee7400',
    'If-None-Match': 'W/"15b-oPCU8vY12uGIepJhoEvCoNrSeK4"',
    'Referer': 'https://www.ajio.com/b/campus-sutra?query=%3Anewn%3Abrand%3ACampus%20Sutra%3Aoccasion%3ACasual%3Al1l3nestedcategory%3AMen%20-%20Shirts%3Al1l3nestedcategory%3AWomen%20-%20Shirts%3Agenderfilter%3AMen%3Arating%3A4%20star%20%26%20above&classifier=intent&gridColumns=5&segmentIds=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.ajio.com/api/home/topSearches', cookies=cookies, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'accept': 'application/json',
    'Referer': 'https://www.ajio.com/b/campus-sutra?query=%3Anewn%3Abrand%3ACampus%20Sutra%3Aoccasion%3ACasual%3Al1l3nestedcategory%3AMen%20-%20Shirts%3Al1l3nestedcategory%3AWomen%20-%20Shirts%3Agenderfilter%3AMen%3Arating%3A4%20star%20%26%20above&classifier=intent&gridColumns=5&segmentIds=',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.ajio.com/api/home/topSearches', headers=headers)




cookies = {
    'V': '201',
    'A': 'eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJjbGllbnQiLCJjbGllbnROYW1lIjoid2ViX2NsaWVudCIsInJvbGVzIjpbeyJuYW1lIjoiUk9MRV9UUlVTVEVEX0NMSUVOVCJ9XSwiZXhwIjoxNzI0MDUxNDM3LCJpYXQiOjE3MjE0NTk0Mzd9.stU2wLuFoJIP5yKgy9LqMbGy-H8JkBZL_MWGMDOjIq9W7XXl0Mdx4A3pxCIRQJskED5fkPc5kwlpYGJf4s0HTIdXhAG62wo7_Ro6bCd9X4Es5zr_B9HBK6gf_7tKBhe3HxdNMoKXZZY0oVArgp9E2YUy5uMicCGDjUufWppyOyHqQ4pt1fGNY_Gs680USZ0B6J1wYz5fmkfGU9VX7RLwVxNDkxpUhyCE197RyV4khHu8p4ui1X_GMam5GtRa8f7eaLuQQ5RzpLIiT1wyoMGFGRA6Qvx7i5oZxcsKYTAsZGXWWuvIfzWXs3VHLpXmdZPyHJRdSkoOyLfKsxSZ14f4kA',
    'U': 'anonymous',
    'TS01ac9890': '01ef61aed0a15ed3b0a4da4423f10e946e2d060a744782ab1fdc489cf6d7bd40826d68f7a0db8d351a9484e47a27e657ac5026304e',
    '_fpuuid': 'oSgjFQp888RFeksofgGgP',
    'deviceId': 'oSgjFQp888RFeksofgGgP',
    'jioAdsFeatureVariant': 'true',
    'recentlyViewed': '[{"id":"463779234_yellow","store":0},{"id":"466380767_yellow","store":0},{"id":"466065907_black","store":0},{"id":"700129394_brown","store":0},{"id":"463775643_blue","store":0}]',
    '_ga': 'GA1.2.407987584.1722876649',
    '_gid': 'GA1.2.161608813.1722876649',
    '_gcl_au': '1.1.465699326.1722876652',
    'sessionStatus': 'true|undefined',
    'FirstPage': 'Mon Aug 05 2024 22:20:51 GMT+0530 (India Standard Time)',
    'AB': 'B',
    'cdigiMrkt': 'utm_source%3A%7Cutm_medium%3A%7Cdevice%3Ad%7Cexpires%3AWed%2C%2004%20Sep%202024%2016%3A50%3A52%20GMT%7C',
    'TS01de1f4a': '01ef61aed03ff042da1eb92e93e9e4a69ad3b96840b393e31e1b3e8f51bde5675550683719da59feb2b2c45ffe638019358d86ef5c331c1cba2eba3d56b97f0de618b37849cb03aee234702b253e77b861c1cebceeffececf3276bc144e14aad2eebee7400',
    'ADRUM_BT': 'R:275|i:5064|g:682cb95d-7fea-43b3-808c-be5e0db44db422883082|e:140|n:customer1_be12de70-87be-45ee-86d9-ba878ff9a400',
}

headers = {
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'V=201; A=eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJjbGllbnQiLCJjbGllbnROYW1lIjoid2ViX2NsaWVudCIsInJvbGVzIjpbeyJuYW1lIjoiUk9MRV9UUlVTVEVEX0NMSUVOVCJ9XSwiZXhwIjoxNzI0MDUxNDM3LCJpYXQiOjE3MjE0NTk0Mzd9.stU2wLuFoJIP5yKgy9LqMbGy-H8JkBZL_MWGMDOjIq9W7XXl0Mdx4A3pxCIRQJskED5fkPc5kwlpYGJf4s0HTIdXhAG62wo7_Ro6bCd9X4Es5zr_B9HBK6gf_7tKBhe3HxdNMoKXZZY0oVArgp9E2YUy5uMicCGDjUufWppyOyHqQ4pt1fGNY_Gs680USZ0B6J1wYz5fmkfGU9VX7RLwVxNDkxpUhyCE197RyV4khHu8p4ui1X_GMam5GtRa8f7eaLuQQ5RzpLIiT1wyoMGFGRA6Qvx7i5oZxcsKYTAsZGXWWuvIfzWXs3VHLpXmdZPyHJRdSkoOyLfKsxSZ14f4kA; U=anonymous; TS01ac9890=01ef61aed0a15ed3b0a4da4423f10e946e2d060a744782ab1fdc489cf6d7bd40826d68f7a0db8d351a9484e47a27e657ac5026304e; _fpuuid=oSgjFQp888RFeksofgGgP; deviceId=oSgjFQp888RFeksofgGgP; jioAdsFeatureVariant=true; recentlyViewed=[{"id":"463779234_yellow","store":0},{"id":"466380767_yellow","store":0},{"id":"466065907_black","store":0},{"id":"700129394_brown","store":0},{"id":"463775643_blue","store":0}]; _ga=GA1.2.407987584.1722876649; _gid=GA1.2.161608813.1722876649; _gcl_au=1.1.465699326.1722876652; sessionStatus=true|undefined; FirstPage=Mon Aug 05 2024 22:20:51 GMT+0530 (India Standard Time); AB=B; cdigiMrkt=utm_source%3A%7Cutm_medium%3A%7Cdevice%3Ad%7Cexpires%3AWed%2C%2004%20Sep%202024%2016%3A50%3A52%20GMT%7C; TS01de1f4a=01ef61aed03ff042da1eb92e93e9e4a69ad3b96840b393e31e1b3e8f51bde5675550683719da59feb2b2c45ffe638019358d86ef5c331c1cba2eba3d56b97f0de618b37849cb03aee234702b253e77b861c1cebceeffececf3276bc144e14aad2eebee7400; ADRUM_BT=R:275|i:5064|g:682cb95d-7fea-43b3-808c-be5e0db44db422883082|e:140|n:customer1_be12de70-87be-45ee-86d9-ba878ff9a400',
    'If-None-Match': 'W/"2-vyGp6PvFo4RvsFtPoIWeCReyIC8"',
    'Referer': 'https://www.ajio.com/b/campus-sutra?query=%3Anewn%3Abrand%3ACampus%20Sutra%3Aoccasion%3ACasual%3Al1l3nestedcategory%3AMen%20-%20Shirts%3Al1l3nestedcategory%3AWomen%20-%20Shirts%3Agenderfilter%3AMen%3Arating%3A4%20star%20%26%20above&classifier=intent&gridColumns=5&segmentIds=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.ajio.com/api/ratings/unratedItems/user', cookies=cookies, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'accept': 'application/json',
    'Referer': 'https://www.ajio.com/b/campus-sutra?query=%3Anewn%3Abrand%3ACampus%20Sutra%3Aoccasion%3ACasual%3Al1l3nestedcategory%3AMen%20-%20Shirts%3Al1l3nestedcategory%3AWomen%20-%20Shirts%3Agenderfilter%3AMen%3Arating%3A4%20star%20%26%20above&classifier=intent&gridColumns=5&segmentIds=',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.ajio.com/api/ratings/unratedItems/user', headers=headers)



headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://assets.ajio.com/static/img/white-star-display.svg', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://assets.ajio.com/medias/sys_master/root/20240716/rir3/6695869c1d763220fab78194/campus_sutra_beige_men_regular_fit_shirt_with_spread_collar.jpg',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://assets.ajio.com/medias/sys_master/root/20240716/cu7Y/6695a6856f60443f3141342f/campus_sutra_purple_men_regular_fit_shirt_with_spread_collar.jpg',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://assets.ajio.com/medias/sys_master/root/20240716/pBcy/66959bf16f60443f31408a5b/campus_sutra_pink_men_pebbles_print_regular_fit_shirt_with_spread_collar.jpg',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://assets.ajio.com/medias/sys_master/root/20240716/i4xJ/6695b6326f60443f31416800/campus_sutra_green_men_embroidered_regular_fit_shirt_with_cuban_collar.jpg',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://assets.ajio.com/medias/sys_master/root/20240716/kaW4/6695a5876f60443f3141171d/campus_sutra_black_men_pebbles_print_regular_fit_shirt_with_spread_collar.jpg',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://assets.ajio.com/medias/sys_master/root/20240715/r2i7/66951baf1d763220fab48b50/campus_sutra_grey_men_regular_fit_shirt_with_cuban_collar.jpg',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://assets.ajio.com/medias/sys_master/root/20240715/WqqZ/66951c751d763220fab4a17f/campus_sutra_brown_men_regular_fit_shirt_with_spread_collar.jpg',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://assets.ajio.com/medias/sys_master/root/20240531/VPfT/6659268a05ac7d77bb927e33/campus_sutra_beige_men_regular_fit_shirt_with_spread_collar_.jpg',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://assets.ajio.com/medias/sys_master/root/20240531/o5wr/6659263605ac7d77bb927489/campus_sutra_yellow_men_regular_fit_shirt_with_spread_collar_.jpg',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://assets.ajio.com/medias/sys_master/root/20240523/6dIN/664e703605ac7d77bb7139a3/campus_sutra_multicoloured_men_checked_regular_fit_shirt_with_patch_pocket.jpg',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://assets.ajio.com/medias/sys_master/root/20240522/m1dc/664df4bb05ac7d77bb70209c/campus_sutra_mauve_men_regular_fit_spread-collar_shirt.jpg',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://assets.ajio.com/medias/sys_master/root/20240522/lQWn/664df4a105ac7d77bb701d9d/campus_sutra_white_men_regular_fit_spread-collar_shirt.jpg',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://assets.ajio.com/medias/sys_master/root/20240708/BRAj/668b7a6c1d763220fa1518d7/campus_sutra_multicoloured_men_regular_fit_spread-collar_shirt.jpg',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://assets.ajio.com/medias/sys_master/root/20240507/b4fY/663a577f16fd2c6e6af13acd/campus_sutra_white_men_regular_fit_shirt_with_spread_collar.jpg',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://assets.ajio.com/medias/sys_master/root/20240507/X5Rf/663a56c816fd2c6e6af121a2/campus_sutra_pink_men_regular_fit_shirt_with_cuban_collar.jpg',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://mercury.akamaized.net/i/44105d5c5c6dca7a9511775401121f45_272765_0.jpg', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://mercury.akamaized.net/i/44105d5c5c6dca7a9511775401121f45_272765_0.jpg', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'appKey': 'c58a39eb46bfd43b62704a0ecf8d6fd8',
}

response = requests.get('https://static.site24x7rum.com/beacon/site24x7rum-min.js', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'appKey': 'c58a39eb46bfd43b62704a0ecf8d6fd8',
}

response = requests.get('https://static.site24x7rum.com/beacon/site24x7rum-min.js', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'appKey': 'c58a39eb46bfd43b62704a0ecf8d6fd8',
}

response = requests.get('https://static.site24x7rum.com/beacon/site24x7rum-min.js', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.gstatic.com/firebasejs/7.6.1/firebase-performance.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.gstatic.com/firebasejs/7.6.1/firebase-performance.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://mercury.akamaized.net/jioads/retargeting/JioEventsConfig_beta.json', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://mercury.akamaized.net/jioads/retargeting/JioEventsConfig_beta.json', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://assets.ajio.com/static/img/favicon.ico', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'id': 'AW-713319256',
    'l': 'dataLayer',
    'cx': 'c',
}

response = requests.get('https://www.googletagmanager.com/gtag/destination', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'id': 'GTM-PF2BPZ8',
    'l': 'dataLayer',
}

response = requests.get('https://www.googletagmanager.com/gtm.js', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'id': 'AW-713319256',
    'l': 'dataLayer',
    'cx': 'c',
}

response = requests.get('https://www.googletagmanager.com/gtag/destination', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'id': 'AW-713319256',
    'l': 'dataLayer',
    'cx': 'c',
}

response = requests.get('https://www.googletagmanager.com/gtag/destination', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'id': 'GTM-PF2BPZ8',
    'l': 'dataLayer',
}

response = requests.get('https://www.googletagmanager.com/gtm.js', params=params, headers=headers)


headers = {
    'Referer': 'https://www.ajio.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = ''

response = requests.get(
    'https://6045405.fls.doubleclick.net/activityi;src=6045405;type=invmedia;cat=whedd4mh;u1=productlistingpage;u2=;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;ord=2450258534759.244',
    params=params,
    headers=headers,
)


headers = {
    'Referer': 'https://www.ajio.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = ''

response = requests.get(
    'https://6045405.fls.doubleclick.net/activityi;src=6045405;type=invmedia;cat=whedd4mh;u1=productlistingpage;u2=;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;ord=1',
    params=params,
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://connect.facebook.net/en_US/fbevents.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://connect.facebook.net/en_US/fbevents.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'id': 'DC-10209894',
    'l': 'dataLayer',
    'cx': 'c',
}

response = requests.get('https://www.googletagmanager.com/gtag/destination', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://sc-static.net/scevent.min.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'id': 'DC-10209894',
    'l': 'dataLayer',
    'cx': 'c',
}

response = requests.get('https://www.googletagmanager.com/gtag/destination', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': '*/*',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://sc-static.net/scevent.min.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://connect.facebook.net/en_US/fbevents.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.ajio.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'id': 'DC-10209894',
    'l': 'dataLayer',
    'cx': 'c',
}

response = requests.get('https://www.googletagmanager.com/gtag/destination', params=params, headers=headers)



