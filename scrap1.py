import requests
from bs4 import BeautifulSoup
import json

def fetch_quotes():
    # URL e faqes që do të bëjmë scraping
    url = 'http://quotes.toscrape.com/'

    # Dërgo një kërkesë HTTP për faqen
    response = requests.get(url)

    if response.status_code == 200:
        # Përdor BeautifulSoup për të analizuar HTML-në
        soup = BeautifulSoup(response.text, 'html.parser')

        # Gjej të gjitha citatet dhe autorët
        quotes = []
        quote_elements = soup.find_all('div', class_='quote')

        for element in quote_elements:
            text = element.find('span', class_='text').text
            author = element.find('small', class_='author').text
            quotes.append({
                'quote': text,
                'author': author
            })

        # Ruaj citatet në një skedar JSON
        with open('quotes.json', 'w', encoding='utf-8') as f:
            json.dump(quotes, f, indent=4, ensure_ascii=False)

        print(f"{len(quotes)} citate u ruajtën me sukses në 'quotes.json'.")
        return quotes
    else:
        print(f"Gabim gjatë kërkesës. Statusi: {response.status_code}")
        return None

if __name__ == "__main__":
    fetch_quotes()
