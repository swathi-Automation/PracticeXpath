import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://selectorshub.com/xpath-practice-page/")
driver.implicitly_wait(10)
element=driver.find_element(By.XPATH, "//*[@class='dropbtn']")
driver.execute_script("arguments[0].scrollIntoView();", element)
drop=driver.find_element(By.XPATH,"//button[text()= 'Checkout here']")
action=ActionChains(driver)
action.move_to_element(drop).perform()
driver.implicitly_wait(50)
dropdwn=driver.find_element(By.ID, "cars")
select=Select(dropdwn)
select.select_by_visible_text("Saab")
time.sleep(5)
driver.close()

#adding new code

