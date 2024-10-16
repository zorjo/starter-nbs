# %%
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.safari.options  import Options
from selenium.webdriver.safari.service import Service as SafariService
#import os
import time
import csv
#from datetime import date
#from datetime import datetime

# %%
cosmix_asins=['B0BCWW8C99','B0B257V797','B0B2579LQV','B0B254BYGW','B0BL135876','B0CNTNX44L','B0B253Y351','B0B25BRTJX','B0CNTNFMS9']
price01='#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-small.aok-align-center > span > span.aok-relative > span.a-size-small.a-color-secondary.aok-align-center.basisPrice > span > span:nth-child(2)'
price1='#corePrice_feature_div > div > div > span.a-price.aok-align-center > span:nth-child(2) > span.a-price-whole'
#price2='//*[@id="corePrice_feature_div"]/div/div/span[1]/span[2]/span[2]'
qty='//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[last()-1]/td'
packz='//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[last()]/td/span/span[1]'

# %%
safari_service = SafariService('/usr/bin/safaridriver')  # Adjust path if necessary
options=Options()
#options.headless=True
# headless is disabled on safari
driver = webdriver.Safari(service=safari_service)
driver.maximize_window()
driver.get("https://www.amazon.in/gp/bestsellers/home-improvement/10079360031/ref=zg_bs_nav_home-improvement_3_10079359031")
for x in range(0,80,4):driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight*.{x})");time.sleep(1.5)
searchres1=driver.page_source
driver.get("https://www.amazon.in/gp/bestsellers/home-improvement/10079360031/ref=zg_bs_pg_2_home-improvement?ie=UTF8&pg=2")
for x in range(0,90,2):driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight*.{x})");time.sleep(2)
searchres2=driver.page_source
driver.get("https://www.amazon.in/stores/page/E0AE2F92-6AEB-4113-8204-6412C0DEF4DF?ingress=2&visitId=7f694a92-dc46-4ae5-baac-109c38acc6f3&store_ref=bl_ast_dp_brandLogo_sto&ref_=ast_bln")
for x in range(0,80,4):driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight*.{x})");time.sleep(1.5)
searchres3=driver.page_source
driver.close()
# %%
arr=[]
arr2=[]
driver = webdriver.Safari(service=safari_service)
driver.maximize_window()
soup = BeautifulSoup(searchres1, "html.parser" )
outer_divs=soup.select('div.zg-grid-general-faceout>div.p13n-sc-uncoverable-faceout')
for i,div1 in enumerate(outer_divs[:50]):
    print(div1.select_one("img")['alt'])
    #print(div1)
    print(div1['id'],i+1)
    price = div1.select_one("div._cDEzb_p13n-sc-price-animation-wrapper_3PzN2").text if div1.select_one("div._cDEzb_p13n-sc-price-animation-wrapper_3PzN2") else "N/A"
    arr=arr+[[i+1,div1.select_one("img")['alt'],div1['id'],price]]
    print(price)
soup = BeautifulSoup(searchres2, "html.parser" )
outer_divs=soup.select('div.zg-grid-general-faceout>div.p13n-sc-uncoverable-faceout')
for i,div1 in enumerate(outer_divs[:50]):
    print(div1.select_one("img")['alt'])
    #print(div1)
    print(div1['id'],50+i+1)
    price = div1.select_one("div._cDEzb_p13n-sc-price-animation-wrapper_3PzN2").text if div1.select_one("div._cDEzb_p13n-sc-price-animation-wrapper_3PzN2") else "N/A"
    arr=arr+[[i+51,div1.select_one("img")['alt'],div1['id'],price]]
    print(price)
soup1=BeautifulSoup(searchres3,'html.parser')
outer_divs=soup1.select('#ProductGrid-hnc082ysu9 > div > div > div > div > ul > li')#ProductGrid-hnc082ysu9 > div > div > div > div > ul > li:nth-child(1) > div.ProductGridItem__item__IkSDt.ProductGridItem__item-with-best-seller__JKmOp > div.ProductGridItem__itemInfo__wl2YN > div.ProductGridItem__itemInfoChild__hUHB0
for i,div in enumerate(outer_divs):
    try:
        asin=div.select_one('div>a')['href'].split('/')[-1][:10]
    except:
        continue
    #print(asin)
    #title=div.select_one('a')
    title=div.select_one('div>a')['title']
    try:
        price=div.select_one('span> span > span > span.Price__whole__mQGs5').text
    except:
        price="N/A"
    try:
        mrp=div.select('span > span > span > span.Price__whole__mQGs5')[1].text
    except:
        mrp=price
    driver.maximize_window()
    driver.get(f"https://www.amazon.in/dp/{asin}")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.65)")
    time.sleep(1)
    y=driver.page_source
    soup=BeautifulSoup(y,'html.parser')
    try:
        for x in soup.select('#productDetails_detailBullets_sections1 > tbody > tr > td'):
            if 'Home Improvement'in x.text:bsr=x.text
        #bsr=soup.select_one('#productDetails_detailBullets_sections1 > tbody > tr:nth-child(8) > td').text
    except:
        bsr='N/A'
    #print(title)
    #print(price)
    #print(mrp)
    arr2=arr2+[[i+1,title,asin,price,mrp,bsr]]
driver.close()
with open('amazon_bestsellers.csv', 'a', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(arr)
with open('amazon_31m.csv', 'a', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(arr2)


