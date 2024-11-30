from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL of the webpage
url = "https://www.audible.com/search?keywords=book&node=18573211011"

# Add headers to mimic a browser
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

# Send a GET request to the webpage
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code != 200:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
    exit(0)

print("Page fetched successfully!")

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all elements that contain the book titles
book_titles = soup.select("h3 a")
# Extract the text from the book titles
book_titles = [title.getText(strip=True) for title in book_titles if title.getText(strip=True)]


book_author = soup.find(name='li', class_="bc-list-item authorLabel").find('a').getText(strip=True)

# Getting hold of the book authors 
book_authors = soup.select("li.bc-list-item.authorLabel a")
# Extract the text from the book authors
book_authors = [author.getText(strip=True) for author in book_authors if author.getText(strip=True)]


# Getting hold of the book naraators
book_narrators = soup.select("li.bc-list-item.narratorLabel  span a")
# Extract the text from the book narrators
book_narrators = [narrator.getText(strip=True) for narrator in book_narrators if narrator.getText(strip=True)]



# Getting hold of the book length
book_length = soup.select("li.bc-list-item.runtimeLabel span")
# Extract the text from the book length and filter out non-length text
book_length = [length.getText(strip=True).replace('Length: ', '') for length in book_length if length.getText(strip=True).startswith('Length:')]


# Getting hold of release_date
release_date = soup.select("li.bc-list-item.releaseDateLabel span")
# Extract the text from the release_date
release_date = [date.getText(strip=True).split()[2] for date in release_date if date.getText(strip=True)]

# Getting hold of the language
language = soup.select("li.bc-list-item.languageLabel span")
# Extract the text from the language
language = [lang.getText(strip=True).split()[1] for lang in language if lang.getText(strip=True)]
# print(language)

# Getting hold of the ratings
ratings = soup.select("li span.bc-text.bc-pub-offscreen")

# Extract the text from the ratings
ratings = [rating.getText(strip=True).split()[0] for rating in ratings if rating.getText(strip=True)]
 


# Extracing the price of the books
prices = soup.select("p span.bc-text.bc-size-base.bc-color-base")
# Extract the text from the prices and filter out non-price text
prices = [price.getText(strip=True) for price in prices if price.getText(strip=True).startswith('$')]



# Create a dictionary to store the data
book_data = { 
    "Title": book_titles[:20],
    "Author": book_authors[:20],
    "Narrator": book_narrators[:20],
    "Length": book_length[:20],
    "Release Date": release_date[:20],
    "Language": language[:20],
    "Rating": ratings[:20],
    "Price": prices[:20]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(book_data)

# Save the DataFrame to a CSV file
df.to_csv("DAY_93_AudibleBookWebscrapping/audible_books.csv", index=True)