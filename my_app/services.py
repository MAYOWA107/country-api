import requests
from django.conf import settings


def get_country_api(country):

    url = f"https://restcountries.com/v3.1/name/{country}"

    response = requests.get(url)

    if response.status_code != 200:
        print(response.text)

        return None
    data = response.json()
    country_data = data[0]

    name = country_data["name"]["common"]
    capital = country_data.get("capital", ["N/A"])[0]
    region = country_data.get("region", "N/A")
    population = country_data.get("population", 0)

    currencies = country_data.get("currencies", {})
    currency_name = "N/A"

    if currencies:
        currency_name = list(currencies.values())[0].get("name", "N/A")

    return {
        "name": name,
        "capital": capital,
        "region": region,
        "population": population,
        "currency": currency_name,
    }
