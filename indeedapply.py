from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests
from bs4 import BeautifulSoup



driver = webdriver.Firefox()
driver.get('https://bestchoiceproducts.com/pages/careers')

content = driver.find_element(By.CSS_SELECTOR, '.m-auto')
content.click()

driver.implicitly_wait(10)

view_all = driver.find_element(By.CSS_SELECTOR, '#recruitment_careerCenter_showAllJobs')
view_all.click()

driver.implicitly_wait(30)

url = driver.current_url
html = requests.get(url)
s = BeautifulSoup(html.content, 'html.parser')

print(s)

# results = s.find(class_='current-opening-list')
# job_title = results.find_all('div', class_='current-opening-title')

# print(job_title[0].text)





# jobtitle = driver.find_element(By.ID, "text-input-what")
# jobtitle.send_keys("cloud support")
# jobtitle.send_keys(Keys.RETURN)