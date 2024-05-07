import os
from dotenv import load_dotenv
import requests
import smtplib
import html
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
email_password = os.getenv("EMAIL_PASSWORD")
my_email = os.getenv("my_email")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_api_parameters={"function":"TIME_SERIES_DAILY",
                  "symbol":STOCK,
                  "apikey":os.getenv("STOCK_API_KEY"),
                  "outputsize":"compact"
                  }

new_api_parameters = {
                    "q": COMPANY_NAME,
                    "from":"2024-04-07",
                    "sortBy":"publishedAt",
                    "apiKey": os.getenv("NEWS_API_KEY"),
                    "language": "en"
}

def news(rate):
    news_response = requests.get(url=NEWS_ENDPOINT, params=new_api_parameters)
    news_response.raise_for_status()
    data = news_response.json()
    articles = data['articles'][:3]  # Get the first 3 articles
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=email_password)
        for article in articles:
            headline = article['title']
            brief = article['description']
            # Construct email message with required format
            subject = f"{STOCK}: {'🔺' if yesterday_price > day_before_yesterday_price else '🔻'}{abs(rate):.2f}%"
            message = f"Subject:{subject}\n\nHeadline: {headline}\n\n\n\nBrief: {brief}"
            connection.sendmail(
                from_addr=my_email,
                to_addrs="kushalbro82@gmail.com",
                msg=message.encode('utf-8')
            )


#making request to stock_api
stock_response= requests.get(url=STOCK_ENDPOINT, params= stock_api_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
#getting hold of yesterday date and closing price of the stock
yesterday = list(stock_data['Time Series (Daily)'].keys())[0]
yesterday_price = float(stock_data['Time Series (Daily)'][yesterday]['4. close'])

#getting hold of the_day_before_yesterday date and opening price of the stock
day_before_yesterday = list(stock_data['Time Series (Daily)'].keys())[1]
day_before_yesterday_price = float(stock_data['Time Series (Daily)'][day_before_yesterday]['1. open'])
print(day_before_yesterday_price)

# When STOCK price increase/decreases by 1% between yesterday and the day before yesterday then Sending Mail to the client
stock_rate = (abs(yesterday_price-day_before_yesterday_price)/yesterday_price)*100
if stock_rate>1:
    news(stock_rate)













