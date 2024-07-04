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

# Function to get the price list of store items with explicit wait
def get_price_list(store_elements):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "store"))
        )
        price_list = []
        for element in store_elements[:8]:  # Limit to first 8 store items
            try:
                item_cost_str = WebDriverWait(driver, 10).until(
                    EC.visibility_of(element.find_element(By.CSS_SELECTOR, "b"))
                ).text
                item_cost = int(item_cost_str.split('-')[-1].strip().replace(',', ''))
                price_list.append(item_cost)
            except (NoSuchElementException, StaleElementReferenceException, ValueError):
                continue
        return price_list
    except TimeoutException:
        return []

# Function to find index of maximum value below a threshold
def find_max_index_below_threshold(integer_list, money):
    max_value = -1
    max_index = -1
    for index, value in enumerate(integer_list):
        if value <= money:
            if value > max_value:
                max_value = value
                max_index = index
    return max_index

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
            store_elements = driver.find_elements(By.CSS_SELECTOR, "#store div")
            price_list = get_price_list(store_elements=store_elements)
            print(price_list)
            money = get_money()
            index = find_max_index_below_threshold(price_list, money)
            
            if index != -1:
                try:
                    
                    store_elements[index].click()
                    print(f"Purchased upgrade at index {index} costing {price_list[index]} cookies.")
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
