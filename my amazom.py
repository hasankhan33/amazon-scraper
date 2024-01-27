import time
import csv
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
name="iphone 14"
driver.get("https://www.amazon.com")
class information:
    def __init__(self,title,price):
        self.title=title
        self.price=price
productlist=[]
time.sleep(5)
search=driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
search.click()
search.send_keys(name)
searchpress=driver.find_element(By.ID,"nav-search-submit-button")
searchpress.click()
for i in range(2):
    for j in range(1,16):
        # getting title
        try:
            titlexpath=f"(//span[@class='a-size-medium a-color-base a-text-normal']){[j]}"
            title=driver.find_element(By.XPATH,titlexpath)
            titletext=title.text
        except:
            continue    
        print(titletext)
        # getting price
        try:
            pricexpath=f"(//span[@class='a-price-whole']){[j]}"
            price=driver.find_element(By.XPATH,pricexpath)
            pricetext=price.text
        except:
            continue    
        print(pricetext)
        info=information(titletext,pricetext)
        productlist.append(info)
    try:    
        nextbutton=driver.find_element(By.XPATH,"//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']")
        nextbutton.click()
        time.sleep(2)
    except:
       url="https://www.amazon.com/s?k=" + name + "&page=" + [i+1]
       driver.get(url)     
with open("new.csv","w", encoding='utf-8', newline='') as csvfile:
    writer=csv.writer(csvfile,delimiter=',',quotechar='"' , quoting=csv.QUOTE_MINIMAL ) 
    for product in productlist:
        writer.writerow([product.title,product.price])
