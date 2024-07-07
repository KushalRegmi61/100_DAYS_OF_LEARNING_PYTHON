from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import os 
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
EMAIL = os.getenv('my_email')
PASSWORD = os.getenv('LINKED_PASS')
PHONE_NO = os.getenv('PHONE_NO')

# Path to your ChromeDriver executable
webdriver_path = 'C:\\Program Files\\Google\\Chrome_Driver\\chromedriver.exe'

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Start WebDriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


# Open Cookie  Tinder
driver.get("https://tinder.com")
time.sleep(6)

#Accept Cookies Button
 # Accept Cookies Button
WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="u-1419960890"]/div/div[2]/div/div/div[1]/div[1]/button'))
    ).click()

# Click on the "Log in" button
# login_button = driver.find_element(By.XPATH, '//*[@id="u-1419960890"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
# login_button.click()
 # Click on the "Log in" button
WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "login")]'))
    ).click()