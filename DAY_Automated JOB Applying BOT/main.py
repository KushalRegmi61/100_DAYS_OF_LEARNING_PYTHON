from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os 
from dotenv import load_dotenv
load_dotenv()
#password
Password = os.getenv('LINKED_PASS')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Replace 'C:\\Program Files\\Google\\Chrome_Driver\\chromedriver.exe' with the actual path to your ChromeDriver executable
service = Service('C:\\Program Files\\Google\\Chrome_Driver\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=marketing%20intern"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)

time.sleep(5)

#Clicking on signin button
sign_in_button=driver.find_element(By.LINK_TEXT, 'Sign in')
sign_in_button.click()

time.sleep(4)

#signing in to liked_IN
username=driver.find_element(By.ID, 'username')
username.send_keys('nepmrkush@gmail.com', Keys.ENTER)
password=driver.find_element(By.ID, 'password')
password.send_keys(Password, Keys.ENTER)

time.sleep(1)





time.sleep(5)
search= driver.find_element(By.CSS_SELECTOR, '.global-nav__search-typeahead button')
search.send_keys('Python Developer', Keys.ENTER)



