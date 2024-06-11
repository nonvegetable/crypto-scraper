import requests
from bs4 import BeautifulSoup
from selenium import webdriver

class CoinMarketCap:
    def __init__(self):
        self.base_url = "https://coinmarketcap.com/currencies/"

    def fetch_coin_data(self, coin):
        url = f"{self.base_url}{coin}/"
        response = requests.get(url)
        if response.status_code == 200:
            return self.parse_data(response.text, coin)
        else:
            return None

    def parse_data(self, html, coin):
        soup = BeautifulSoup(html, 'html.parser')
        # Extract the required data using soup
        # Example:
        price = soup.find('div', {'class': 'priceValue'}).text
        # Extract other data similarly
        data = {
            "price": price,
            # Add other fields here
        }
        return data