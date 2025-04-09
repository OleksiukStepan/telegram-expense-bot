import requests
from bs4 import BeautifulSoup

URL = "https://minfin.com.ua/"


def get_usd_exchange_rate():
    request = requests.get(URL).content
    soup = BeautifulSoup(request, "html.parser")

    rate_tag = soup.select_one("#currencyWgt .mf-currency-ask")

    if not rate_tag:
        raise ValueError("Couldn't find USD exchange rate on the page.")

    rate_text = rate_tag.text.strip().replace(",", ".")
    return float(rate_text)
