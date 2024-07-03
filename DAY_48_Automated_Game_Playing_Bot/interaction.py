from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Replace 'C:\\Program Files\\Google\\Chrome_Driver\\chromedriver.exe' with the actual path to your ChromeDriver executable
service = Service('C:\\Program Files\\Google\\Chrome_Driver\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com")

first_name=driver.find_element(By.NAME, 'fName')
first_name.send_keys('Mr', Keys.ENTER)
last_name= driver.find_element(By.NAME, 'lName')
last_name.send_keys('KuSH', Keys.ENTER)
email=driver.find_element(By.NAME, 'email')
email.send_keys('kushal@gmail.com', Keys.ENTER)
button = driver.find_element(By.TAG_NAME, 'button')
button.click()