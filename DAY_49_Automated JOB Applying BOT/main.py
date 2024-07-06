from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException, WebDriverException
import time
import os 
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
EMAIL = os.getenv('my_email')
PASSWORD = os.getenv('LINKED_PASS')
PHONE_NO = os.getenv('PHONE_NO')

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Set up ChromeDriver service
service = Service('C:\\Program Files\\Google\\Chrome_Driver\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

def sign_in():
    driver.get(
        "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
        "&keywords=Marketing%20Intern"
        "&location=London%2C%20England%2C%20United%20Kingdom"
        "&redirect=false&position=1&pageNum=0"
    )

    # Click on the sign-in button
    time.sleep(5)
    sign_in_button = driver.find_element(By.LINK_TEXT, 'Sign in')
    sign_in_button.click()

    time.sleep(5)

    # Sign in to LinkedIn
    email_field = driver.find_element(By.ID, 'username')
    email_field.send_keys(EMAIL)
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.ENTER)

def abort_application():
    try:
        # Click close button
        close_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
        close_button.click()
        
        time.sleep(2)
        
        # Click discard button
        discard_buttons = driver.find_elements(By.CLASS_NAME, 'artdeco-modal__confirm-dialog-btn')
        if discard_buttons:
            discard_button = discard_buttons[1]
            discard_button.click()
    except (NoSuchElementException, TimeoutException, ElementClickInterceptedException):
        pass

def main():
    sign_in()
    input("Solve the CAPTCHA and press Enter to continue...")

    # Get job listings
    job_list = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')

    for job in job_list[:4:1]:
        job.click()
        time.sleep(2)
        try:
            # Click Apply button
            apply_button = driver.find_element(By.CSS_SELECTOR, '.jobs-s-apply button')
            apply_button.click()

            time.sleep(2)
            
            # Insert phone number if necessary
            phone_input = driver.find_element(By.CSS_SELECTOR, "input[id*=phoneNumber]")
            if phone_input.get_attribute('value') == "":
                phone_input.send_keys(PHONE_NO)

            # Check for complex applications
            submit_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary.ember-view")

            if submit_button.get_attribute("aria-label") == "Continue to next step":
                abort_application()
                print("Complex application, skipped.")
                continue
            else:
                # Submit application
                submit_button.click()
                print("Application submitted.")

            time.sleep(2)
            driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss').click()

        except (NoSuchElementException, TimeoutException, ElementClickInterceptedException) as e:
            abort_application()
            print(f"Exception occurred: {e}. No application button, skipped.")
            continue
        except WebDriverException as e:
            print(f"WebDriver exception occurred: {e}.")
            break

    driver.quit()

if __name__ == "__main__":
    main()
