from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
EMAIL = os.getenv('GF_FB_EMAIL')
PASSWORD = os.getenv('TWITTER_PASS')
PROMISE_UPLOAD = 80
PROMISE_DOWN = 100

# Path to your ChromeDriver executable
webdriver_path = 'C:\\Program Files\\Google\\Chrome_Driver\\chromedriver.exe'

class InternetSpeedTwitterBot:
    def __init__(self):
        # Configure Chrome options
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--disable-software-rasterizer")

        # Start WebDriver
        self.service = Service(webdriver_path)
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        
        self.down = 0
        self.upload = 0
        
    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net')
        go_button_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        self.wait_and_click(go_button_xpath)
        time.sleep(60)
        self.upload = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'))
        ).text
        time.sleep(2)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
                                             ).text
        time.sleep(4)
        print("Upload Speed:", self.upload)
        print("Download Speed:", self.down)
        
        
    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/login')
        time.sleep(10)

        # Logging in to Twitter
        email_xpath = '//input[@name="text"]'
        self.wait_and_send_keys(email_xpath, EMAIL)

        password_xpath = '//input[@name="password"]'
        self.wait_and_send_keys(password_xpath, PASSWORD)

        # Handle CAPTCHA if it appears
        self.handle_captcha()

        # Tweeting
        time.sleep(8)
        tweet_box_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div'
        tweet_text = f"My internet speed is {self.down} Mbps download / {self.upload} Mbps upload, but I pay for {PROMISE_DOWN} Mbps / {PROMISE_UPLOAD} Mbps. #InternetSpeed"
        
        tweet_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, tweet_box_xpath))
        )
        tweet_box.send_keys(tweet_text)

        time.sleep(7)
        tweet_button_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button' 
        try:
            tweet_button = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, tweet_button_xpath))
                )
            self.driver.execute_script('arguments[0].click()', tweet_button)
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
            print(f"Exception during wait_and_send_keys: {e}")
            
            
            
    def wait_and_click(self, xpath, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
            print(f"Exception during wait_and_click: {e}")
            
    def wait_and_send_keys(self, xpath, keys, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            element.send_keys(keys, Keys.ENTER)
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
            print(f"Exception during wait_and_send_keys: {e}")

    def handle_captcha(self):
        # Handle CAPTCHA if it appears
        try:
            captcha_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="captcha"]'))
            )
            if captcha_element:
                print("CAPTCHA detected. Please solve it manually.")
                time.sleep(60)  # Give user time to solve CAPTCHA
        except TimeoutException:
            # CAPTCHA not found
            pass
        

            

# Creating object
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if float(bot.upload)<float(PROMISE_UPLOAD) and float(bot.down)<float(PROMISE_DOWN):
    bot.tweet_at_provider()
else:
    print(f"Internet Speed is as promised.{bot.upload} up Mbps/ {bot.down} down Mbps")    
