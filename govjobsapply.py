from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests
from bs4 import BeautifulSoup



driver = webdriver.Firefox()
driver.get('https://www.usajobs.gov')

jobsearch = driver.find_element(By.ID, 'nav-keyword')
jobsearch.send_keys("IT")
jobsearch.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

url = driver.current_url
html = requests.get(url)
s = BeautifulSoup(html.content, 'html.parser')

print(s)

# results = s.find(id='usajob-search-results')
# job_title = results.find_all('a', class_='usajobs-search-result--core__title search-joa-link')

# print(job_title[0].text)

# jobtitle = driver.find_element(By.ID, "text-input-what")
# jobtitle.send_keys("cloud support")
# jobtitle.send_keys(Keys.RETURN)