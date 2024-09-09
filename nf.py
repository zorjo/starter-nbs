import requests

cookies = {
    'at': 'ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWWpNeFkySm1NelF0TkdOaFpTMHhNV1ZtTFRreVlqZ3RNV1ZsTmpjd1pXTTVabUk1SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzTXpjM01ERTROamdzSW1semN5STZJa2xFUlVFaWZRLjcyUTBZczRVNFdjT09zaEhuQnNlRWRTb3pHS01oR2c3VDhHSEwyUkpiaFk=',
    '_d_id': '4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb',
    'mynt-eupv': '1',
    '_mxab_': 'config.bucket%3Dregular%3BConvenience_fee_logged_out_user%3Denabled%3Bhpmweb.mycoupons.revamp%3DRevamp_ver1%3Bcoupon.cart.channelAware%3DchannelAware_Enabled%3Bdesktop.pla%3Denabled',
    'lt_timeout': '1',
    'lt_session': '1',
    'bm_ss': 'ab8e18ef4e',
    '_abck': 'FA360452C255EDEFEF91C657BB89268A~0~YAAQjInTF0abru6QAQAACfagDwyC8wXbZa7f4T4FAUGQ18KdgPvsIGMPt/jv8qGkeekl0vRrBDOl1NS9tDNaYaTT9cupC4v6FUqX/1FVrpNURllZvMHD/mqamnmNxtSLNBkv1udPM4UvwQAUj8LN3R4JuZwDgxWWSZMTjGldZAYityPM9RcnOfIYTdL2ca+GiDkxGfNXxEhfea5zXX2/lDqpcpYtpeTgKKP93l+OVsO9C62UlIVFb2sTTglRihM0lWo14VA2Wr44FkHyqir7zUICtZaGjU2wCvrLAMbdWxGDpKP/F7DZ3FFUpq5M2XI8ZKqSYH7JZXlDYsxmuQupLhtkmeFGtwf5YQklluCnzZDQ4EzzgoKrWSGbXo4qOkXD9LB7XWukrbaXCbtFaLjXJFZmQj9Y9D+4~-1~-1~-1',
    'ak_bmsc': 'EFC17FA6C7EDB26DD3214C0E0719BEEE~000000000000000000000000000000~YAAQjInTF0ebru6QAQAACfagDxghJYshlpwUoz9BA+Is3Rit52xSsVaYhoNTkIHSZakyPvw7Z7XOA6wHkjqobzG8V4q8widldHps+1S7VPrID5n3cEeVPiuzeENBKLIL7VoZAIWq/FmH9T20hj8/+aaKRg2Qp5IE4c0CGws/+AU0Dm6ptLor5E8pTlZBtSZS3QFXrulJg+OMuVFqrIiSyqLfA9aAwBGuAldt6Nja735XDrIEOuUHOOTqDPC495lTOGnAKW8kVq3I4zp6iYRDCFYzzoFQy+EGqb0bqEEAIf216UzvIVwXIsEr7Xx2i7/R0FXctstUkheUz5PwBxEZJvvPTp6+bT9tIi57woGVDvjRtA903Eg1zKs82oZ4d/Cszo2r5n/2WIb8Dx8=',
    'bm_s': 'YAAQjInTF0mbru6QAQAACfagDwHgQHOk+0U1qMyTdYETChd79v5nGSawI7bHMBxwszMYSF9f/Sw/kOW/nzMG4cmlyxpCCUsyj80a/poumuBZWT4lFnGUXUOinOpMV59dOyG/cah283kjlOjVoGsi4O4VNtiQX2sPuerlXrwTgvsmmyxYENSnlval4NwXXY0P/pwpaFV2RAXTKuxLBXfrS6Xtr3wX2s5QFQwoCuxQ5agxyVMsmNfBCJcC6mylhl/Z9ciHEbTcuU44oZaNiyjkuQcNPJ1q527rqjZoeoYyQTV33074xshCzYGUdWA7x/KM+smUIlZxGHd06+445aoxttFkrjotcA==',
    'bm_so': 'A0CCB058200355A3F3AE920597BA11FEF8A9973E5AC21426219EAC833187BE97~YAAQjInTF0qbru6QAQAACfagDwAC8UpoSfmWCTkTLockoDt7ojCDxCY2t41BDZT3q5HSfWw6cafzjumw/Cyvixb1RJGIhnKw2ERHBcf/gzUBDVhG4kb9A+2cdPg9aOWSOUPo4wShxCRZcYzhq9bIAk1CifdvibM9M0kc7V82KLUzVo6/1Db5OHzeJAS8tORAQA83XZZA6s9mpCFlSaUvUDsOmVS54gowl8tnRCGxZcdvrrYG5xO/6eDbyn8yd+Flan8esVjca2FquPDfsOp6hu8YTHiAEiXtadZ1MrBL4h6ghn3szMSs0L3HPPnOwPgcfUw0mCChdhXSFbRH1L0jDXdYB8Ep+kT19/s6vrVVcs7k1jSLur1ya8BFbqRzJIBK83xU2Dzce8boAdBKiR/9KRx8TBafYeV9v88yNDLYx+O0TiggwbFn6DJ2o2LjdbQqozyvRH8dbxlD78V5Ay/cV1a6FkiAX22nTWNIhE+Wut+DYyIAVm70xMSC18M0lV4=',
    '_ma_session': '%7B%22id%22%3A%2276de98cc-f530-4039-9db2-f93144fe0fdb-4b9b5630-8fe4-4823-bc6e-1b0ee56f89fb%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D',
    'microsessid': '262',
    '_xsrf': 'sMG6z3Bg2wL0NfafFLcgHlcW1VYdrrEB',
    'mynt-ulc-api': 'pincode%3A700006',
    'mynt-loc-src': 'expiry%3A1722545534145%7Csource%3AIP',
    'x-mynt-pca': 'nH9mxtXUPchmnWDGbhXl9jaw-c5Vja_ovNGyjLbpRsDQIkl7OflPowdK8z8pxlicfpTpLHNuswY89SAkZ0oVceg_fRX_GCoVljGV-NLrKDUCeGRNSpaf2XMnYzvBI24aQdwXtGc0zx9tzATRW3LlN5Xa3EcQmrjYx43Q1R_Vq_62sBgai-E%3D',
    'bm_mi': '29E716E16E8F65347CDE6DC4797202C5~YAAQjInTFxahru6QAQAAWouhDxhxnlINBiuP555xet6HUoc/3YymF5LqMNOXcTxY9BpGaBN4NgAR/ZkJimPE1XekPDHpB5Chv/CLo9H1n5sV1tRo3pG86eQPwoKvX42K0qdDTqcWb1f/Aya+T56RpcfH7Wo+VuUxNvjZHSHxnAVynTuEfv4hHM7FtNQB6asHzEf/VL1DfAY9h3idddEA+rQ3XUYkaKiQcNDNofJK4Z4sIPcC4I5I5cyGGgJp9olUPKuBvEC3wl/0GM1deIQTDwFyFzm5/yPY/7SZe9SaJxJ9+CtEzGn3OxtXvtsNalDh8xq0Pi3GkUlX~1',
    'bm_sz': 'F72F7D30B2B2ABACF9A56B9E722D9EFD~YAAQjInTFxihru6QAQAAWouhDxh6eyQdd8zW5PVAU67NeVtXvBktcdW+tdOqgmmRD9UgJCCGoLIw4u7O0pfYCNtAHISQHbbw9RdlGI9FNkljiqGgM0CU5FhzM8m5u2jW/ZhhUgZ70AGFukLVCtbgUMXssVlDWR0T9mwTUCa2XSxitinHlH+4eoUP1eAFWAHhZGaDUR7FPfwl94oalBNBVtZl4y8n98gbuiw7/oP9r6T0J1TipDiUOeFgjFSl8RTI95zLyXtJAu0nCFkfJ5vAYBP4Gcenuz+kXqe284H7reOBUkDFckCU8q2MEZpuhw3j+PW4oNr96/H0MPwbGQ8i/eak1jPNzeyPDkYylv4SqnzVbiFFCF/fzVc8x99PNWndy1ttOaaW6lk0I+rkidfncOsLYnzqcwPSsZKvaA==~3553092~3424822',
    'utrid': 'HHdUd3sGcGwdEG0GF2VAMCMxODg1Mjk4NzYyJDI%3D.86d39c7b5344ff305e5b4514890bf9fc',
    'bm_sv': '66FEB442DBBAA140C7A0E053FA987E40~YAAQjInTFxALr+6QAQAAWlGrDxi/8knDAQ+YXSWSA3QFxKWUjHTtBLbhGgYXubgmA/47FllHs7s4EBGchsx6daiRKZeZAlnCkq56kN5GdTiD3QzieqS79uCybsdPZWRJdAnQ1H1hwrjA6yQ5sq9biNdJONinn0MP3CVd+GxIEOFqsP63f+0acjNZWRsISycn0chV/m9xSFnn3TWp5J0XrL4Wd5Q20OELwKyeUwD2n4byDf4ZoEl9fpq7bUaSNTKq/g==~1',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'app': 'web',
    'content-type': 'application/json',
    'pagination-context': '{"refresh":true,"v":1}',
    'priority': 'u=1, i',
    'referer': 'https://www.myntra.com/campussutra?f=Brand%3ACampus%20Sutra&sort=new',
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
    'sort': 'new',
    'rows': '100',
    'o': '0',
    'plaEnabled': 'true',
    'xdEnabled': 'false',
    'pincode': '700006',
}

response = requests.get('https://www.myntra.com/gateway/v2/search/campussutra', params=params, headers=headers,cookies=cookies) 