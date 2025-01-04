
from arbitrage import *
from graph import Graph
import numpy as np
import datetime
import requests
import time

def get_price(coin_id, vs_currency):
    URL = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={vs_currency}"
    try:
        response = requests.get(URL)
        response.raise_for_status()  
        data = response.json()
        return data.get(coin_id, {}).get(vs_currency)
    except requests.RequestException as e:
        print(f"Error fetching data for {coin_id} in {vs_currency}: {e}")
        return None



def create_conversion_matrix(prices):
    matrix = np.zeros((3, 3))
    
    matrix[0, 1] = prices[0]
    matrix[0, 2] = prices[1]
    matrix[1, 0] = prices[2]
    matrix[1, 2] = prices[3]
    matrix[2, 0] = prices[4]
    matrix[2, 1] = prices[5]
    
    np.fill_diagonal(matrix, 1)
    
    return matrix

def main():
    print("Fetching data from CoinGecko API...")
    
    pairs = {
        "btc_eth": ("bitcoin", "eth"),
        "btc_xrp": ("bitcoin", "xrp"),
        "eth_btc": ("ethereum", "btc"),
        "eth_xrp": ("ethereum", "xrp"),
        "xrp_btc": ("ripple", "btc"),
        "xrp_eth": ("ripple", "eth")
    }
    prices = []
    for _, (coin, currency) in pairs.items():
        price = get_price(coin, currency)
        time.sleep(10)
        if price is not None:
            print(f"Price of {coin.upper()}/{currency.upper()} is {price}")
            prices.append(price)
        else:
            print(f"Failed to fetch price for {coin.upper()}/{currency.upper()}")
    print(f"\nTime of data fetched: {datetime.datetime.now()}\n")
    
    rates = create_conversion_matrix(prices)
    graph = Graph(['BTC', 'ETH', 'XRP'], rates)
    detect_arbitrage(graph)

if __name__ == "__main__":
    main()