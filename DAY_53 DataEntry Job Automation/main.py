"""This a intermediate Day_53 project that utilizes the concept of BeautifulSoup and Selenium.
This is intermediate data entry automation project. That scraps the data from Zillow.com regarding the
rental properties in particular loaction and the a using Selenium google form is filled which can later 
be converted in to spreadsheet document. This help to find rental properties in your locations."""


from bs4 import BeautifulSoup
import requests
from pprint import pprint
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time


# Path to your ChromeDriver executable
webdriver_path = 'C:\\Program Files\\Google\\Chrome_Driver\\chromedriver.exe'

#website links and headers
googleForm_link="https://forms.gle/ViQztU7SdT8aweRa6"
weblite_link="https://appbrewery.github.io/Zillow-Clone/"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0"
}

#TODO 1: Fetching the website  content
response= requests.get(weblite_link, headers=headers)

if response.status_code != 200:
    print(f"Failed to retrive data. Error occured{response.text}")
    exit(0)

data= response.content

#TODO 2: creating soup
soup = BeautifulSoup(data, 'html.parser')

#getting hold of links of the post
element_1 = soup.find_all(name='a', class_='property-card-link')
article_links=[element.get('href') for element in element_1]

#getting hold of house rent prices
element_2 = soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')
prices=[element.getText() for element in element_2]

# Function to clean and format prices
def format_price(price):
    # Remove unwanted characters using regex
    cleaned_price = re.sub(r'[^\d]', '', price)
    # Format to the desired output with commas
    formatted_price = f"${int(cleaned_price):,}"
    return formatted_price

# Apply the formatting function to each price
rentPrice_list= [format_price(price) for price in prices]

#getting hold of house_address
element_3=soup.find_all(name='address')
addresses=[element.getText() for element in element_3]

# Function to clean and format addresses
def clean_address(address):
    # Remove leading/trailing whitespace and newlines
    address = address.strip()
    # Remove " | " substring
    address = address.replace(" | ", ", ")
    # Remove multiple spaces
    address = re.sub(r'\s+', ' ', address)
    return address

# Apply the cleaning function to each address
address_list = [clean_address(address) for address in addresses]

#TODO 2: Filling google forms using selenium
chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")

# Start WebDriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

#method to send keys:
def wait_and_send_keys(driver, xpath, keys, enterkey=None, timeout=20):
    try:
        element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.send_keys(keys)
        if enterkey:
            element.send_keys(enterkey)
    except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
        print(f"Exception during wait_and_send_keys: {e}")

qns1_xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
qns2_xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
qns3_xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
submitButton_xpath='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'

for i in range(len(rentPrice_list)):
    driver.get(googleForm_link)
    time.sleep(4)
    try:
        wait_and_send_keys(driver=driver, xpath=qns1_xpath, keys=address_list[i],enterkey=Keys.ENTER)  #sending Qn_1 answer
        wait_and_send_keys(driver=driver, xpath=qns2_xpath, keys=rentPrice_list[i],enterkey=Keys.ENTER)  #sending Qn_2 answer
        wait_and_send_keys(driver=driver, xpath=qns3_xpath, keys=article_links[i],enterkey=Keys.ENTER)  #sending Qn_3 answer
        time.sleep(1)
        subbmit_button=driver.find_element(By.XPATH, submitButton_xpath)
        subbmit_button.click()#clicking on submit button
        
    except (NoSuchElementException, ElementClickInterceptedException, TimeoutException) as e:
        print(f"Error Occured: {e}")
    else:
        print(f"Form NO: {i+1} subbmittted successfully.")
    finally:     
        time.sleep(1)
    
#finally closes the driver
driver.quit()    
