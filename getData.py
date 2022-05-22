import time
from turtle import st
import pandas_datareader as data
import pandas as pd
import numpy as np
from yahoo_historical import Fetcher
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from scipy import spatial
import json
import concurrent.futures

data1 = pd.read_csv("./nasdaq.csv")
data2 = pd.read_csv("./nyse.csv")

# List of tickers
Symbols = data1['Symbol'].append(data2['Symbol']).drop_duplicates()

# Calculate time for run
t0 = time.time()

# Create Empty Dataframe
frames = []

# loop through each ticker and download

res = {}


def getData(symbol):
    stock = data.DataReader(symbol, "yahoo", "2021-4-27", "2022-4-27")
    if len(stock) > 0:
        close_values = stock['Close'].to_numpy().tolist()
        res[symbol] = close_values


executor = concurrent.futures.ThreadPoolExecutor()
futures = [executor.submit(getData, t) for t in Symbols]

count = 0
for f in concurrent.futures.as_completed(futures):
    try:
        result = f.result()
        # print(result)
    except Exception as exc:
        print('Error occured: %s' % exc)
    finally:
        count += 1
        print(count)

jsonString = json.dumps(res)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()
