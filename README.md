# Cryptocurrency Arbitrage Analysis

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Requests](https://img.shields.io/badge/Requests-2.26%2B-brightgreen)
![NumPy](https://img.shields.io/badge/NumPy-1.21%2B-orange)
![matplotlib](https://img.shields.io/badge/matplotlib-3.4%2B-blue)
![networkx](https://img.shields.io/badge/networkx-2.5%2B-brightgreen)
![math](https://img.shields.io/badge/math-used-blueviolet)
![time](https://img.shields.io/badge/time-used-brightgreen)


This repository contains the implementation and analysis of various arbitrage strategies across cryptocurrency and forex markets. The project employs Python to detect potential arbitrage opportunities in cross-exchange and triangular trading scenarios, utilizing real-time data fetched from financial APIs like CoinGecko.


---

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Results](#results)

---

## Introduction

This project is designed to explore extensive arbitrage opportunities by leveraging price differentials in both cryptocurrency and forex markets. The main areas of focus are:
- **Cross-Exchange Arbitrage**: Identifying price discrepancies for the same asset across different cryptocurrency exchanges.
- **Cryptocurrency Triangular Arbitrage**: Exploring arbitrage within a single exchange using a triangle of three different cryptocurrencies.
- **Forex Triangular Arbitrage**: Applying triangular arbitrage methods to the forex market to capitalize on currency conversion cycles.
- **Data Utilization**: Demonstrating the use of real-time exchange data and efficient data processing techniques in Python to identify and evaluate arbitrage opportunities.

The project aims to quantify the frequency and profitability of these arbitrage opportunities and showcase the application of financial APIs and Python in complex financial analyses.

---

## Features


- **Real-time Data Fetching:** Pull live cryptocurrency data from the CoinGecko API.
- **Arbitrage Detection:** Algorithmically detect arbitrage opportunities based on fetched prices.
- **Visualization:** Generate and display potential arbitrage paths and their profitability.
- **Logging and Monitoring:** Track and log arbitrage opportunities over time.

---

## Project Structure

```plaintext
📂 Crypto-Arbitrage-Analysis/
├── docs/                        # Documentation related to the project
├── img/                         # Folder containing generated visualizations and plots
├── src/                         # Source code folder containing Python scripts
│   ├── arbitrage.py             # General arbitrage functions
│   ├── bellman_ford.py          # Bellman-Ford algorithm implementation
│   ├── cross_exchange_arbitrage.py # Arbitrage detection for cross-exchange scenarios
│   ├── cryptocurrency_triangular_arbitrage.py # Triangular arbitrage functions for cryptocurrencies
│   ├── forex_triangular_arbitrage.py # Triangular arbitrage functions for forex
│   └── graph.py                 # Graph data structure implementation
├── LICENSE                      # License information for the project
├── README.md                    # Detailed project overview and setup instructions
└── requirements.txt             # List of Python libraries and dependencies required for the project


```

---

## Setup and Installation

Follow these steps to set up and run the project:

### Prerequisites
Ensure you have Python 3.8 or higher installed. You can check your version by running:
```bash
python --version
```
### Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/0xNathaniel/Arbitrage-Detection.git 
cd Arbitrage-Detection
```
### Install Dependencies
Install the required Python libraries using the requirements.txt file:
```bash
pip install -r requirements.txt
```
---

## Usage
Run the following command to execute the forex triangular arbitrage script:
```bash
cd src
python forex_triangular_arbtirage.py
```
Run the following command to execute the cryptocurrency triangular arbitrage script:
```bash
cd src
python cryptocurrency_triangular_arbtirage.py
```
Run the following command to execute the cross exchange arbitrage script:
```bash
cd src
python cross_exchange_arbitrage.py
```

---

## Results
- **Key Insights**
  - abc
  - abc
- **Limitations**
  - abc