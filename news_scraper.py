# news_scraper.py

import requests
from bs4 import BeautifulSoup

# Target news site (you can change to any public news site with <h2> or <title> tags)
URL = "https://www.bbc.com/news"

def fetch_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all <h3> elements with headline text (BBC uses <h3> for headlines)
    headlines = []
    for tag in soup.find_all(['h1', 'h2', 'h3']):
        text = tag.get_text(strip=True)
        if text and len(text) > 20 and text not in headlines:
            headlines.append(text)
    
    return headlines

def save_to_file(headlines, filename="headlines.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        for line in headlines:
            file.write(line + '\n')
    print(f"{len(headlines)} headlines saved to {filename}.")

def main():
    print("Fetching headlines...")
    headlines = fetch_headlines(URL)
    if headlines:
        save_to_file(headlines)
    else:
        print("No headlines found.")

if __name__ == "__main__":
    main()
