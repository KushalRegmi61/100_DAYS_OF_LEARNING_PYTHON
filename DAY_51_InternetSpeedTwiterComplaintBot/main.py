from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
EMAIL = os.getenv('GF_FB_EMAIL')
PASSWORD = os.getenv('TWITTER_PASS')
PROMISE_UPLOAD=20
PROMISE_DOWN=100

# Path to your ChromeDriver executable
webdriver_path = 'C:\\Program Files\\Google\\Chrome_Driver\\chromedriver.exe'

class InternetSpeedTwitterBot:
    def __init__(self):
        # Configure Chrome options
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        # Start WebDriver
        self.service = Service(webdriver_path)
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        
        self.down=0
        self.up = 0
        
        
    def get_internet_speed(self):
        pass
    
    def tweet_at_provider(self):
        pass
    
    
#TODO: CREATING OBJECT
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()   
bot.tweet_at_provider()     
        
        
        