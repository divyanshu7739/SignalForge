import yfinance as yf

from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator, SMAIndicator, MACD


def get_technical_indicators(ticker: str):

    stock = yf.Ticker(ticker)

    df = stock.history(period="6mo")

    rsi = RSIIndicator(df["Close"]).rsi()

    ema = EMAIndicator(df["Close"]).ema_indicator()

    sma = SMAIndicator(df["Close"]).sma_indicator()

    macd = MACD(df["Close"])

    return {
        "rsi": round(rsi.iloc[-1], 2),
        "ema": round(ema.iloc[-1], 2),
        "sma": round(sma.iloc[-1], 2),
        "macd": round(macd.macd().iloc[-1], 2)
    }