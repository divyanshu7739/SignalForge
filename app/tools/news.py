import yfinance as yf
from typing import List, Dict


def get_news(ticker: str) -> List[Dict]:

    stock = yf.Ticker(ticker)

    news = stock.news

    articles = []

    for item in news:
        articles.append(
            {
                "title": item.get("title"),
                "publisher": item.get("publisher"),
                "link": item.get("link"),
            }
        )

    return articles