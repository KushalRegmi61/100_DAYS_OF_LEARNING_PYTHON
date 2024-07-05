from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time

# Path to your ChromeDriver executable
webdriver_path = 'C:\\Program Files\\Google\\Chrome_Driver\\chromedriver.exe'

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Start WebDriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Cookie Clicker game
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Find initial elements
cookie_clicker = driver.find_element(By.ID, "cookie")

# Function to get the price list and IDs of store items with explicit wait
def get_cookie_upgrades():
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "store"))
        )
        store_elements = driver.find_elements(By.CSS_SELECTOR, "#store div")
        cookie_upgrades = {}
        for element in store_elements[:8]:  # Limit to first 8 store items
            try:
                item_name = element.get_attribute("id")
                item_cost_str = WebDriverWait(driver, 10).until(
                    EC.visibility_of(element.find_element(By.CSS_SELECTOR, "b"))
                ).text
                item_cost = int(item_cost_str.split('-')[-1].strip().replace(',', ''))
                cookie_upgrades[item_cost] = item_name
            except (NoSuchElementException, StaleElementReferenceException, ValueError):
                continue
        return cookie_upgrades
    except TimeoutException:
        return {}

# Function to find the most expensive affordable upgrade
def find_max_affordable_upgrade(cookie_upgrades, money):
    affordable_upgrades = {cost: id for cost, id in cookie_upgrades.items() if cost <= money}
    if affordable_upgrades:
        highest_price = max(affordable_upgrades)
        return affordable_upgrades[highest_price]
    return None

# Function to get current money
def get_money():
    try:
        money = int(driver.find_element(By.ID, "money").text.replace(',', ''))
        return money
    except NoSuchElementException:
        return 0

# Main loop to play the game
start_time = time.time()
while True:
    # Click the big cookie
    cookie_clicker.click()
    
    # Every 10 seconds, check and purchase the most expensive affordable upgrade
    if int(time.time() - start_time) % 10 == 0:
        try:
            cookie_upgrades = get_cookie_upgrades()
            money = get_money()
            to_purchase_id = find_max_affordable_upgrade(cookie_upgrades, money)
            
            if to_purchase_id:
                try:
                    driver.find_element(By.ID, to_purchase_id).click()
                    print(f"Purchased upgrade: {to_purchase_id}")
                except (StaleElementReferenceException, NoSuchElementException):
                    continue
        except (StaleElementReferenceException, NoSuchElementException):
            continue

    # Stop after 5 minutes
    if time.time() - start_time > 300:
        break

# Calculate and print CPS (Cookies Per Second)
total_cookies = get_money()
cps = total_cookies / 300  # 300 seconds = 5 minutes
print(f"Cookies per second (CPS): {cps}")

# Close the browser
driver.quit()
