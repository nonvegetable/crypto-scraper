from celery import app
from .coinmarketcap import CoinMarketCap
from .models import Task

@app.task
def scrape_coins(coin_list, job_id):
    scraper = CoinMarketCap()
    tasks = []
    for coin in coin_list:
        try:
            data = scraper.scrape_data(f'https://coinmarketcap.com/currencies/{coin}')
            task = Task.objects.create(coin=coin, data=data, job_id=job_id)
            tasks.append(task)
        except Exception:
            pass