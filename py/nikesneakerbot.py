# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:26:42 2019

@author: Jon Wang
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import numpy as np
import scipy.stats as stats

keys = {
        "product_url": "https://www.nike.com/launch/t/air-jordan-1-high-travis-scott/",
        "name": "Jon Wang",
        "email": "yelin66@gmail.com",
        "password": "Wang3747xiao",
        "telephone": "3215763601",
        "address": "6144 Anello Drive",
        "zip": "32940",
        "card": "1111111111111111",
        "CVV": "111",
        "expiration": "0622"
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
    #driver.find_element_by_xpath('//*[@id="AccountNavigationContainer"]/button').click()
    driver.find_element_by_xpath('//*[@id="buyTools"]/div[1]/div[2]/label[5]').click()
    driver.find_element_by_xpath('//*[@id="buyTools"]/div[2]/button[1]').click()
    driver.find_element_by_xpath('//*[@id="gen-nav-commerce-header"]/header/nav/section[1]/div/div/ul[2]/li[3]').click()
    time.sleep(2)
    driver.find_element_by_css_selector('#Cart > div.ncss-row.u-full-width.css-10qap0j > div.ncss-col-sm-12.ncss-col-lg-4.css-szgf5x > aside > div.ncss-row.css-1ygripx > div > button.css-dgm8zs.e1o7oqt06').click()
    time.sleep(10)
    driver.find_element_by_class_name('emailAddress').send_keys(keys["email"])
    driver.find_element_by_xpath('//*[@id="22e2837f-e77c-428a-83a9-d11e7efcb5b7"]').send_keys(keys["password"])
    driver.find_element_by_xpath('//*[@id="creditCardNumber"]').send_keys(keys["card"])
    driver.find_element_by_xpath('//*[@id="expirationDate"]').send_keys(keys["expiration"])
    driver.find_element_by_xpath('//*[@id="cvNumber"]').send_keys(keys["CVV"])
    #driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys["CVV"])
    #driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
    #driver.find_element_by_xpath('//*[@id="pay"]/input').click()


if __name__ == '__main__':
     driver = webdriver.Chrome(r"C:\Users\Jon Wang\Downloads\chromedriver.exe")
     #url = driver.command_executor._url
     #session_id = '4861325843693568'
     #driver = webdriver.Remote(command_executor=url,desired_capabilities={})
     #driver.session_id = session_id
     order(keys)