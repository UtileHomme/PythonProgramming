import requests

APP_ID = "b6edf3a7ebad499c9f941c278812d8e2"
ENDPOINT = "https://openexchangerates.org/api/latest.json"

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
print(response.json())
exchange_rates = response.json()["rates"]

usd_amount = 1000
gbp_amount = usd_amount * exchange_rates["GBP"]

print(f"USD{usd_amount} is GBP{gbp_amount}")
