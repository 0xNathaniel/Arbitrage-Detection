from arbitrage import *
from graph import Graph
import numpy as np

def main():
    currency_names = ['USD', 'EUR', 'GBP', 'JPY']
    rates = np.array([
        [1.0000, 0.8425, 0.7250, 113.50], 
        [1.1860, 1.0000, 0.8650, 134.50],  
        [1.3800, 1.1555, 1.0000, 148.00],  
        [0.0088, 0.0074, 0.0068, 1.0000]   
    ])
    
    graph = Graph(currency_names, rates)
    detect_arbitrage(graph)
    
if __name__ == "__main__":
    main()
