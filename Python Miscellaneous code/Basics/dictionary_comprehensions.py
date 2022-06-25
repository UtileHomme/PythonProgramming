stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219
}

new_stocks = {}

for symbol, price in stocks.items():
    new_stocks[symbol] = price * 1.02

print(new_stocks)

# Dictionary comprehensions
new_stocks1 = {symbol: price * 1.02 for (symbol, price) in stocks.items()}

print(new_stocks1)

selected_stocks = {s: p for (s, p) in stocks.items() if p > 200}

print(selected_stocks)
