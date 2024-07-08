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
PASSWORD = os.getenv('GF_FB_PASS')

# Path to your ChromeDriver executable
webdriver_path = 'C:\\Program Files\\Google\\Chrome_Driver\\chromedriver.exe'

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Start WebDriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Tinder
driver.get("https://tinder.com")
time.sleep(6)

def wait_and_click(driver, xpath, timeout=20):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element.click()
    except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
        print(f"Exception during wait_and_click: {e}")

try:
    # Accept Cookies Button
    wait_and_click(driver, '//*[@id="u-1419960890"]/div/div[2]/div/div/div[1]/div[1]/button')
    print("Cookies accepted")

    # Click on the "Log in" button
    wait_and_click(driver, '//*[@id="u-1419960890"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
    print("Clicked on log in button")

    # Click on login using Google button
    FB_login_button_xpath = '//*[@id="u1146625330"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button'
    time.sleep(7)
    wait_and_click(driver, FB_login_button_xpath)
    print("Clicked on Google login button")

    # Switching to FB login window
    base_window = driver.window_handles[0]
    fb_login_window = WebDriverWait(driver, 10).until(
        lambda d: [window for window in d.window_handles if window != base_window][0]
    )
    driver.switch_to.window(fb_login_window)
    print(driver.title)

    # Signing in using Facebook
    username = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]'))
    )
    username.send_keys(EMAIL)
    password = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="pass"]'))
    )
    password.send_keys(PASSWORD, Keys.ENTER)

    time.sleep(4)

    # Switching back to Tinder window
    driver.switch_to.window(base_window)
    print(driver.title)

    # Allowing Location Access
    wait_and_click(driver, '//*[@id="u1146625330"]/div/div/div/div/div[3]/button[1]')

    # Allowing Notifications Access
    wait_and_click(driver, '//*[@id="u1146625330"]/div/div/div/div/div[3]/button[1]')
    
    time.sleep(7)
    like_button_path = '//*[@id="u-1419960890"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button'

    for n in range(5):
        time.sleep(2)
        try:
            print("called")
            like_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, like_button_path))
            )
            like_button.click()
        except ElementClickInterceptedException:
            try:
                match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
                match_popup.click()
            except NoSuchElementException:
                driver.refresh()
                time.sleep(2)
                
        except TimeoutException:
            time.sleep(4)
            continue
        
                
except TimeoutException:
    print("Timed out waiting for page to load")
except NoSuchElementException:
    print("Element not found")
except StaleElementReferenceException:
    print("Stale element reference exception")
finally:
    driver.quit()
