import os
from urllib.parse import urlparse

from bs4 import BeautifulSoup
import requests

base_url = "https://nzgovt.utf9k.net/nz_government/organisations.json?_shape=array&_col=website"

organisations = []

if not os.path.exists('robots_files'):
    os.mkdir('robots_files')

def fetch_organisations(url=base_url):
    r = requests.get(url)
    if r.ok:
        organisations.extend(r.json())
    else:
        print(f"Received status {r.status_code} trying to fetch {base_url}")
        os.exit(1)
    next_url = r.links.get('next', {}).get('url', False)
    if next_url:
        fetch_organisations(next_url)

fetch_organisations()

browserless_api_token = os.environ.get("BROWSERLESS_API_TOKEN", False)
if not browserless_api_token:
    print("Please set BROWSERLESS_API_TOKEN env var")
    os.exit(1)

scrape_url = os.environ.get("BROWSERLESS_URL", False)
if not scrape_url:
    print("Please set BROWSERLESS_URL env var")
    os.exit(1)

scrape_params = {"token": browserless_api_token, "stealth": True}

for organisation in organisations:
    print(organisation['id'])
    website_parsed = urlparse(organisation['website'])
    robots_url = f"{website_parsed.scheme}://{website_parsed.netloc}/robots.txt"
    r = requests.post(scrape_url, params=scrape_params, json={"url": robots_url})
    if r.ok:
        if 'user-agent:' in r.text.lower() or 'disallow:' in r.text.lower() or 'allow:' in r.text.lower():
            soup = BeautifulSoup(r.text, 'html.parser')
            print("- found robots.txt")
            with open(f"robots_files/{organisation['id']}.txt", "w") as file:
                file.write(soup.text)