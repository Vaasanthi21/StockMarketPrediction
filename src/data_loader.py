import pandas as pd
import yfinance as yf

def fetch_stock_data(ticker="AAPL", start="2020-01-01", end="2024-12-31"):
    data = yf.download(ticker, start=start, end=end)
    return data