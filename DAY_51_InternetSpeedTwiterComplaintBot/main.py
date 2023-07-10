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
        
        # Add options to disable GPU hardware acceleration
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--disable-software-rasterizer")

        # Start WebDriver
        self.service = Service(webdriver_path)
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        
        self.down = 0
        self.upload = 0
        
    # Function to get the internet speed using speedtest website    
    def get_internet_speed(self):
        pass
    #     self.driver.get('https://www.speedtest.net')
    #     go_button = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
    #     self.wait_and_click(self.driver, go_button)
        
    # # Getting hold of upload and download Internet speed

    #     self.upload=WebDriverWait(self.driver, 20).until(
    #             EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'))
    #             ).text
    #     time.sleep(2)
    #     self.down = self.driver.find_element(By.XPATH,
    #                                          value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
    #                                          ).text
        # self.driver.quit()
        
    #     print("upload_speed= ",self.upload)
    #     print("Download_speed= ",self.down)
        
    # Method to make a complaint tweet
    def tweet_at_provider(self):
        # time.sleep(4)
        self.driver.get('https://x.com')
        time.sleep(2)
        signIN_xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[2]'
        # signIn_button= WebDriverWait(self.driver, 20).until(
        #         EC.presence_of_element_located((By.XPATH,signIN_xpath))
        #         )
        # signIn_button.click()
        self.wait_and_click(self.driver, signIN_xpath)
        
    # Method to click on buttons
    def wait_and_click(self, driver, xpath, timeout=20):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
            print(f"Exception during wait_and_click: {e}")
    
    
# Creating object
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()   
bot.tweet_at_provider()
