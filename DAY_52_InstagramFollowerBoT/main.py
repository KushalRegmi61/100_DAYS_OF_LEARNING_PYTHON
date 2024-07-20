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

        #TODO: 1 method to loginIN to the account 
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(7)
        
        # Sending username and password
        username_xpath = "//*[@aria-label='Phone number, username, or email']"
        self.wait_and_send_keys(xpath=username_xpath, keys=EMAIL)
        
        password_xpath = "//*[@aria-label='Password']"
        self.wait_and_send_keys(password_xpath, PASSWORD, enterkey=Keys.ENTER)
        # time.sleep(8)
        
        # Sending the backup code
        # backupCode_buttonXpath = "//button[contains(text(),'backup codes')]"
        
        # try:
        #     backupCode_button = WebDriverWait(self.driver, 20).until(
        #         EC.presence_of_element_located((By.XPATH, backupCode_buttonXpath))
        #     )
        #     self.driver.execute_script('arguments[0].click()', backupCode_button)
        # except Exception as e:
        #     print(f"An error occurred: {e}")
        #     self.driver.save_screenshot('error_screenshot.png')
        #     raise e
            
        # #sending backup code using environment variable
        # # input_xpath='//*[@aria-label="Security Code"]'
        # # self.wait_and_send_keys(xpath=input_xpath, keys=INSTA_BACKUP, enterkey=Keys.ENTER)
        
                
        #veryfing the browser  manually..
        # input("Press Enter to After you complete verification: ")
        
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
    def find_followers(self):
        time.sleep(5)
        # Show followers of the selected account. 
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")

        time.sleep(3)
        #pressing follower button 
        follower_xpath="//a[contains(@href, '/kushalregmi_/followers/')]"
        self.wait_and_click(follower_xpath)
        time.sleep(6)
        
        # The xpath of the modal that shows the followers will change over time. Update yours accordingly.
        modal_xpath = "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        
        self.follow(self.driver)
        
        
        
        # for i in range(10):
        #     # In this case we're executing some Javascript, that's what the execute_script() method does.
        #     # The method can accept the script as well as an HTML element.
        #     # The modal in this case, becomes the arguments[0] in the script.
        #     # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
        #     self.follow(self.driver)
        #     time.sleep(1)
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     time.sleep(4)
            
            
            
            
    #TODO: 3 Method for following INsta accounts
    
    def follow(self, driver):
        try: 
            followButton_xpath='//button[@class=" _acan _acap _acas _aj1- _ap30"]'
            followButtons=driver.find_elements(By.XPATH, followButton_xpath)#list of follow button in that page
            for element in followButtons:
                try:
                    element.click()
                    
                except ElementClickInterceptedException:
                    time.sleep(1)
                    cancelButton_xpath='//button[contains(text(),"Cancel")]' 
                    self.wait_and_click(cancelButton_xpath)
                
                finally:
                    time.sleep(2)
                               
   
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
            print(f"Exception during wait_and_send_keys: {e}")
    
    #method to send keys
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
bot.find_followers()# finding the insta_id



    
    
    