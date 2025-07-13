import requests

def get_price(symbol: str) -> float:
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}" #инфу будем брать с binance
    response = requests.get(url)
    response.raise_for_status()
    return float(response.json()["price"])
