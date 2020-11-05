from client import ScrapeZoneClient
from decouple import config

username = config('SCRAPEZONE_USERNAME')
password = config('SCRAPEZONE_PASSWORD')

scrapeZoneClient = ScrapeZoneClient(username, password)

scraper_name = 'amazon_product_display'
query = [
    'https://amazon.com/dp/B01LSUQSB0',
    'https://amazon.com/dp/B084K5HNCB'
]

results = scrapeZoneClient.scrape(
    {'scraper_name': scraper_name, 'query': query})

print(results)
