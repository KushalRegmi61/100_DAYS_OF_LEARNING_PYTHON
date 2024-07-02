from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Global Variables
PRICE = 100
EMAIL = os.getenv('my_email')
PASSWORD = os.getenv('my_password')

# Product link URL
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0"
}

# Step 3: Fetch the webpage content
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print("Failed to retrieve data. Please check the date format or try a different date.")
    exit(0)

xml_data = response.content

# Step 2: Parse the XML data
soup = BeautifulSoup(xml_data, 'lxml')
item_price = float(soup.select_one(".a-offscreen").get_text().strip('$').replace(',', ''))
item_name = soup.find(id="productTitle").get_text().strip()

# Sending email if price drops
if item_price < PRICE:
    message = (f'Subject: Amazon Price Drop Alert!\n\n'
               f'{item_name} is now available at ${item_price}.\n'
               f'\nCheck the link: {url}')

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="kushalbro82@gmail.com",
            msg=message.encode('utf-8')
        )

    print("Email sent successfully!")
else:
    print(f"No price drop. Current price is ${item_price}.")
