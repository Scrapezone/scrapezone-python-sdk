<p align="center">
    <a href="https://scrapezone.com/"><img src="https://app.scrapezone.com/img/logo.svg" alt="Scrapezone Logo" width="300" height="60"></a>
  </a>
</p>

<h2 align="center">
  Getting Data Was Never Easier
</h2>

<p align="center">
Forget about proxies, servers, and IP addresses. Just get the data you need.
</p>

Google and eCommerce HTML Scraper
Send a request with up to 1,000 URLs and receive the raw, unblocked HTML files.

## Quick Start

1. Create a new account at: https://app.scrapezone.com
2. Copy your scrape username and password.
3. Start getting the data you need.

## Example request:

```
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

```

Full documentation can be found [Here](https://github.com/Scrapezone/documentation).
