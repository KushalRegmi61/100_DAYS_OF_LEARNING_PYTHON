'''This project might be helpful if you want to create a new brand using instagram or becaome a influencer.
For example, if you want to create a food_influencer then using this code you search popular food influencer
in your country then you can go throught their follower list and follow all the followers of that account 
that watches food related content then might go through your account and follow you back if they like your 
content . Thus, your reach and id engagement increases and  This will boost you growth as an influencer'''

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

    #TODO: 1 method to loginIN to the account 
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(7)
        
        #sending username and password
        username_xpath="//*[@aria-label='Phone number, username, or email']"
        self.wait_and_send_keys(xpath=username_xpath,keys= EMAIL)
        
        password_xpath="""//*[@aria-label='Password']"""
        self.wait_and_send_keys(password_xpath,PASSWORD,enterkey=Keys.ENTER)
        time.sleep(2)
                
        #veryfing the browser  manually..
        input("Press Enter to After you complete verification: ")
        
        #save_info button  value="//button[contains(text(), 'Click me')]")
        info_xpath="""// div[contains(text(), 'Not now')]"""
        time.sleep(4)
        self.wait_and_click(info_xpath)
        
        time.sleep(4)
        #turning off the notification
        turn_off_xpath="// button[contains(text(), 'Not Now')]"
        self.wait_and_click(turn_off_xpath)
        time.sleep(2)
    
    #TODO: 2 method to find_followers()
    def find_follower(self):
        similarAcc_link=f'https://www.instagram.com/{SIMILAR_ACCOUNT}/'
        self.driver.get(similarAcc_link)
        time.sleep(2)
        followerButton_xpath=f"//a[contains(@href, '/{SIMILAR_ACCOUNT}/followers/')]"
        self.wait_and_click(followerButton_xpath)
    
    #TODO: 3 Method for following INsta accounts
    
    def follow(self):
        pass
    
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

    #method to click buttons  
    def wait_and_click(self, xpath, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
            print(f"Exception during wait_and_click: {e}")

    

# creating a instaFollower class bot
bot = InstaFollower()
bot.login()#login to the insta id..
bot.find_follower()# finding the insta_id
bot.follow() #method to folllow insta account

    
    
    