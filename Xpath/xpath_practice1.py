from selenium import webdriver
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/p/add-padding-to-containers.html")
driver.implicitly_wait(10)
element=driver.find_element(By.XPATH,"//*[@id='post-body-299858861183690484']/div/form/div[1]/input[1]")
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.find_element(By.XPATH,"//*[@id='post-body-299858861183690484']/div/form/div[1]/input[1]").send_keys("ABC")
driver.find_element(By.XPATH,"//*[@id='post-body-299858861183690484']/div/form/div[1]/input[2]").send_keys("welcome")
driver.find_element(By.XPATH,"//*[@id='post-body-299858861183690484']/div/form/div[1]/input[3]").send_keys("abc@gmail.com")
driver.find_element(By.XPATH,"//*[@id='post-body-299858861183690484']/div/form/div[1]/div[2]/input[1]").send_keys("Abc@123")
driver.find_element(By.XPATH,"//*[@id='post-body-299858861183690484']/div/form/div[1]/input[4]").send_keys("Abc@123")
driver.find_element(By.XPATH,"//*[@class='buttons']/button[1]").click()
# scroll_element=driver.find_element(By.XPATH,"//*[@id='contactList']/tbody/tr[2]/td[2]")
# driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
# driver.implicitly_wait(5)
# driver.find_element(By.XPATH, "//*[@id='contactList']/tbody/tr[2]/td[1]").click()
driver.close()
