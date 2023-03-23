from selenium import webdriver
from PIL import Image
import time
driver = webdriver.Chrome("D:\\Chromedriver\\chromedriver.exe")
url="https://google.com"
driver.get(url)
#driver.execute_script()
driver.maximize_window()
time.sleep(1)
driver.save_screenshot("image1.jpg")
Image.open("image1.jpg")
print("screenshot saved")