import yfinance as yf


def get_stock_data(ticker: str):

    stock = yf.Ticker(ticker)

    info = stock.info

    history = stock.history(period="1d")

    current_price = info.get("currentPrice")

    if current_price is None and not history.empty:
        current_price = float(history["Close"].iloc[-1])

    return {

        "company": info.get("longName"),

        "symbol": ticker.upper(),

        "current_price": current_price,

        "previous_close": info.get("previousClose"),

        "market_cap": info.get("marketCap"),

        "volume": info.get("volume"),

        "average_volume": info.get("averageVolume"),

        "sector": info.get("sector"),

        "industry": info.get("industry"),

        "country": info.get("country"),

        "currency": info.get("currency"),

        "pe_ratio": info.get("trailingPE"),

        "forward_pe": info.get("forwardPE"),

        "eps": info.get("trailingEps"),

        "book_value": info.get("bookValue"),

        "dividend_yield": info.get("dividendYield"),

        "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),

        "fifty_two_week_low": info.get("fiftyTwoWeekLow")

    }