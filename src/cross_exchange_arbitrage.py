from arbitrage import *
from graph import Graph
import numpy as np
import requests
import time

URL = "https://api.coingecko.com/api/v3/coins/bitcoin/tickers"

def get_bitcoin_price(exchanges):
    exchanges_price = []
    
    for exchange in exchanges:
        try:
            url = URL.replace("{exchange_id}", exchange)
            response = requests.get(url)
            response.raise_for_status()
            time.sleep(0.2)
            
            data = response.json()
            tickers = data.get("tickers", [])

            for ticker in tickers:
                if ticker["base"] == "BTC" and ticker["target"] == "USD":
                    price = ticker["last"]
                    if (price in exchanges_price):
                        continue
                    print(f"Bitcoin price on {exchange.capitalize()}: {price} USD")
                    exchanges_price.append(price)
                    break

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {exchange}: {e}")
    
    return exchanges_price

def create_cross_exchange_matrix(exchanges_price):
    n = len(exchanges_price)
    matrix = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = exchanges_price[j] / exchanges_price[i]
                
    return matrix


def main():
    # Bitcoin price fetching using CoinGecko API
    exchanges = ['binance', 'kraken', 'coinbase', 'bitstamp']
    exchanges_price = get_bitcoin_price(exchanges)
    print("\n")
    rates = create_cross_exchange_matrix(exchanges_price)
    
    graph = Graph(exchanges, rates)
    detect_arbitrage(graph)
    
if __name__ == "__main__":
    main()
