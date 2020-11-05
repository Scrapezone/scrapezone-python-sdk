from client import ScrapezoneClient
from decouple import config

username = config('SCRAPEZONE_USERNAME')
password = config('SCRAPEZONE_PASSWORD')

scrapezoneClient = ScrapezoneClient(username, password)

results = scrapezoneClient.scrape(
    {'scraper_name': 'amazon_product_display', 'query': [
        'https://amazon.com/dp/B01LSUQSB0',
        'https://amazon.com/dp/B084K5HNCB'
    ]})

print(results)
