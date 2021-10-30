from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import numpy as np
import scipy.stats as stats

url = input("Enter url: ")

keys = {
        "product_url": url,
        "name": "Jon Wang",
        "email": "xjonwang@gmail.com",
        "telephone": "3215763601",
        "address": "6144 Anello Drive",
        "zip": "32940",
        "card": "1111111111111111",
        "CVV": "111"
        }

def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print("Execution time: {}".format((endTime - startTime)/1000))
        return result
    return wrapper


@timeme
def order(keys):
    driver.get(keys['product_url'])
    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    time.sleep(.15)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(keys["name"])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys["email"])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys["telephone"])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(keys["address"])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys["zip"])
    driver.find_element_by_xpath('//*[@id="nnaerb"]').send_keys(keys["card"])
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[6]').click()
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[4]').click()
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys["CVV"])
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()

	
if __name__ == '__main__':
     driver = webdriver.Chrome(r"C:\Users\Jon Wang\Downloads\chromedriver.exe")
     order(keys)
