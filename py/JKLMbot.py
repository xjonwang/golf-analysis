from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import numpy as np
import keyboard
import nltk
nltk.download('words')
from nltk.corpus import words

url = input("Enter URL: ")

keys = {
        "game_url": url,
        }

word_list = words.words()
print(len(word_list))

def wrapper(*args, **kw):
	startTime = int(round(time.time() * 1000))
	result = method(*args, **kw)
	endTime = int(round(time.time() * 1000))
	print("Execution time: {}".format((endTime - startTime)/1000))
	return result
	return wrapper

#@timeme
def wordAlgorithm(keys):
	driver.get(keys['game_url'])
	#time.sleep(10)
	#driver.find_element_by_xpath('/html/body/div[2]/div[3]/form/div[2]/button').click()
	#time.sleep(5)
	#driver.find_element_by_xpath('//button[text()="Join game"]').click()
	while true:
		if keyboard.is_pressed('r'):
			print("r has been pressed")
			for word in word_list:
				syllable = span_element = driver.find_element_by_css_selector(".syllable")
				print(syllable)


driver = webdriver.Chrome(r"C:\Users\Jon Wang\Downloads\chromedriver92.exe")
#wordAlgorithm(keys)
while True:
	if keyboard.read_key == "r":
		print("r has been pressed")
	else:
		continue