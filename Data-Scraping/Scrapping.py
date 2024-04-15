import os
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_news():
    # Send a GET request to the website
    page = requests.get("https://www.republika.co.id/")
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # Find all the news on the website
    articles = soup.find_all('li', class_='list-group-item list-border conten1')
    scraped_data = []

    # Loop for every news on the website
    for index, article in enumerate(articles, start=1):
        title = article.find('h3').text.strip()
        category = article.find('span', class_='kanal-info').text.strip()
        date_element = article.find('div', class_='date')
        publish_time = date_element.text.strip() if date_element else None

        # Clean "-" in the publish time text
        publish_time = publish_time.lstrip('- ') if publish_time else None

        if publish_time:
            time_info = publish_time.split("-")[-1].strip()
            scraped_data.append({
                'number': index,
                'title': title,
                'category': category,
                'publish_time': time_info,
                'scraping_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

    return scraped_data

# Scraping the data
scraped_data = scrape_news()

# Convert the data to JSON format
json_data = json.dumps(scraped_data)

# Get the absolute path to the 'Data.json' file within the 'Data-Scraping' folder
file_path = os.path.join(os.path.dirname(__file__), 'Data.json')

# Appending the JSON data to an existing file
with open(file_path, 'w') as file:
    if os.stat(file_path).st_size != 0:
        file.write('\n')
    file.write(json_data)

# Printing the scraped information
print(scraped_data)
