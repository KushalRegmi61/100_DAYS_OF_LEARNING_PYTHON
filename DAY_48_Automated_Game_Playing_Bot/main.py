from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Replace 'C:\\Program Files\\Google\\Chrome_Driver\\chromedriver.exe' with the actual path to your ChromeDriver executable
service = Service('C:\\Program Files\\Google\\Chrome_Driver\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.python.org")

event_dates = driver.find_elements(By.CSS_SELECTOR ,value='.event-widget .menu time ')
date_List = [date.text for date in event_dates]
print(date_List)
event_names = driver.find_elements(By.CSS_SELECTOR ,
                                   value='.event-widget .shrubbery .menu li a')
Name_list = [names.text for names in event_names]
print(Name_list)



driver.quit()
