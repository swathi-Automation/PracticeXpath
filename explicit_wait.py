import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Xpath.xpath_practice1 import element

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
wait=WebDriverWait(driver,10)
element=wait.until(EC.presence_of_element_located(By.ID, "APjFqb"))
element.click()
element.send_keys("selenium")
time.sleep(10)
driver.close()
