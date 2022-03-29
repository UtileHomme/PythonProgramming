import time
from libs.openexchange import OpenExchangeClient

APP_ID = "b6edf3a7ebad499c9f941c278812d8e2"

client = OpenExchangeClient(APP_ID)

start = time.time()

usd_amount = 1000

gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end - start)

print(f"USD{usd_amount} is GBP{gbp_amount:.2f}")
