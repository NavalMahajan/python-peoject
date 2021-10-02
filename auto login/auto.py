from selenium import webdriver
import time
from datetime import datetime
import pynput
from pynput.keyboard import Controller,Key
isStarted=True
import webbrowser
import sys
url="https://www.prepbytes.com/login"
   
while isStarted:
     if datetime.now().hour ==18 and  datetime.now().minute ==30: 
      driver=webdriver.Chrome("C:/Users/HP/Desktop/chromedriver")
      driver.get(url)
      driver.find_element_by_name("email_input").send_keys("navalmahajan2001@gmail.com")
      driver.find_element_by_name("password_input").send_keys("Naval@1235432")
      driver.find_element_by_xpath('//button[normalize-space()="Sign In"]').click()
      time.sleep(4)
      driver.close()
      isStarted=False
      sys.exit()   
      exit
if isStarted==False:
    sys.exit()   
    exit 



