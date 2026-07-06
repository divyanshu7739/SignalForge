import yfinance as yf
from typing import Dict,Any


def get_stock_data(ticker: str):
    """
    Fetch basic stock information from Yahoo Finance.
    """
    stock = yf.Ticker(ticker)
    info = stock.info

    history = stock.history(period="1d")

    current_price = info.get("currentPrice")

    if current_price is None and not history.empty:
        current_price = float(history["Close"].iloc[-1])

    return {
        "company": info.get("longName"),
        "current_price":info.get("currentPrice"),
        "market_cap":info.get("marketCap"),
        "volume":info.get("volume"),
        "sector":info.get("sector")
    }