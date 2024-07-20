'''This project might be helpful if you want to create a new brand using Instagram or become an influencer.
For example, if you want to create a food influencer account, then using this code you can search for popular food influencers
in your country. Then, you can go through their follower list and follow all the followers of that account 
who watch food-related content. They might go through your account and follow you back if they like your 
content. Thus, your reach and engagement increases, and this will boost your growth as an influencer.'''

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
EMAIL = os.getenv('INSTA_EMAIL')
PASSWORD = os.getenv('INSTA_PASS')
SIMILAR_ACCOUNT='kushalregmi_'

# Path to your ChromeDriver executable
webdriver_path = 'C:\\Program Files\\Google\\Chrome_Driver\\chromedriver.exe'

#creating instaFollower class
class InstaFollower:
    def __init__(self):
        # Configure Chrome options
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--disable-software-rasterizer")

        # Start WebDriver
        self.service = Service(webdriver_path)
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(7)
        
        # Sending username and password
        username_xpath = "//*[@aria-label='Phone number, username, or email']"
        self.wait_and_send_keys(xpath=username_xpath, keys=EMAIL)
        
        password_xpath = "//*[@aria-label='Password']"
        self.wait_and_send_keys(password_xpath, PASSWORD, enterkey=Keys.ENTER)
        
        #verifying the browser manually..
        # input("Press Enter after you complete verification: ")
        
        #save_info button 
        info_xpath="""// div[contains(text(), 'Not now')]"""
        time.sleep(4)
        self.wait_and_click(info_xpath)
        
        time.sleep(4)
        #turning off the notification
        turn_off_xpath="// button[contains(text(), 'Not Now')]"
        self.wait_and_click(turn_off_xpath)
        time.sleep(2)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        time.sleep(3)
        
        follower_xpath="//a[contains(@href, '/kushalregmi_/followers/')]"
        self.wait_and_click(follower_xpath)
        time.sleep(5)
        
        modal_xpath = "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        
        for i in range(5):
            time.sleep(1)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(4)

    def follow(self):
        try: 
            followButton_xpath='//button[@class=" _acan _acap _acas _aj1- _ap30"]'
            followButtons = self.driver.find_elements(By.XPATH, followButton_xpath)  # list of follow buttons on that page
            for element in followButtons:
                try:
                    element.click()
                    time.sleep(3)
                except ElementClickInterceptedException:
                    time.sleep(2)
                    cancelButton_xpath='//button[contains(text(), "OK")]'
                    # cancelButton_xpath='//button[contains(text(), "Cancel")]'
                    
                    self.wait_and_click(cancelButton_xpath)
                finally:
                    time.sleep(1)
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
            print(f"Exception during follow: {e}")
        else:
            self.driver.quit()

    def wait_and_send_keys(self, xpath, keys, enterkey=None, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            element.send_keys(keys)
            if enterkey:
                element.send_keys(enterkey)
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

# Creating an InstaFollower class bot
bot = InstaFollower()
bot.login()  # Login to the Instagram account
bot.find_followers()  # Finding the Instagram followers
bot.follow()  # Following Instagram accounts
