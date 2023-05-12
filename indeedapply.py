from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.indeed.com/")
jobtitle = driver.find_element(By.ID, "text-input-what")
jobtitle.send_keys("cloud support")
jobtitle.send_keys(Keys.RETURN)