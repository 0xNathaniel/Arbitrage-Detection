from bellman_ford import bellman_ford
from math import exp
import matplotlib.pyplot as plt
import networkx as nx

def reconstruct_cycle(predecessors, start):
    cycle = []
    current = start
    while predecessors[current] is not None and current not in cycle:
        cycle.append(current)
        current = predecessors[current]
    cycle.append(start)  
    return cycle

def print_cycle(cycle, currency_names):
    path = ' -> '.join(currency_names[i] for i in cycle)
    print(f"{path}")

def plot_arbitrage_graph(cycle, rates, currency_names):
    G = nx.DiGraph()
    labels = {}

    for i in range(len(cycle) - 1):
        u, v = cycle[i], cycle[i + 1]
        G.add_edge(currency_names[u], currency_names[v])
        labels[(currency_names[u], currency_names[v])] = f"{rates[i]:.5f}"

    u, v = cycle[-1], cycle[0]
    G.add_edge(currency_names[u], currency_names[v])
    labels[(currency_names[u], currency_names[v])] = f"{rates[-1]:.5f}"

    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=20000, edge_color='k', linewidths=1, font_size=25)

    edge_labels_font_size = 20  
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red', font_size=edge_labels_font_size)

    plt.title("Arbitrage Cycle Graph", fontsize=20) 
    plt.show()

def calculate_profit(cycle, graph):
    profit = 1.0
    initial_amount = 1.0  
    current_amount = initial_amount
    currency_names = graph.currency_names
    rates = []
    print("Arbitrage opportunity detected!\n")
    print("Step-by-step trading process:")
    for i in range(len(cycle) - 1):
        u, v = cycle[i], cycle[i + 1]
        rate = exp(-next(w for (x, y, w) in graph.edges if x == u and y == v))
        current_amount *= rate
        print(f"Trade from {currency_names[u]} to {currency_names[v]} at rate {rate:.5f}: new amount = {current_amount:.5f}")
        profit *= rate
        rates.append(rate)
    print_cycle(cycle, currency_names)
    print(f"Final amount after completing the cycle starting with {initial_amount} {currency_names[cycle[0]]}: {current_amount:.5f}")
    print(f"Total profit: {(profit - 1) * 100:.2f}%\n")
    plot_arbitrage_graph(cycle, rates, currency_names) 
    return profit


def is_valid_arbitrage_cycle(cycle, graph):
    product = 1.0
    for i in range(len(cycle) - 1):
        u, v = cycle[i], cycle[i + 1]
        rate = exp(-next(w for (x, y, w) in graph.edges if x == u and y == v))
        product *= rate
    return product > 1

def detect_arbitrage(graph):
    for src in range(graph.vertices):
        has_cycle, predecessors = bellman_ford(graph, src)
        cycle = reconstruct_cycle(predecessors, src)[::-1]
        if has_cycle and is_valid_arbitrage_cycle(cycle, graph):
            calculate_profit(cycle, graph)