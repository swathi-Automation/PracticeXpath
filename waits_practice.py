import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/")
wait=WebDriverWait(driver,10)
element=wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='comp']/div[2]/div[1]/div[2]/input[1]")))
element.click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//*[@id='comp']/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]").click()
driver.close()
