import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import glob

print("hello")
root = os.path.dirname(os.path.dirname(__file__))
driver_path = os.path.join(root,"chromedriver")
storage_path = os.path.join(root,"data-storage")
print(storage_path)
driver = webdriver.Chrome(driver_path)