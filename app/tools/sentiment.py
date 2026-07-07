from app.tools.news import get_news


def get_sentiment_data(ticker: str):

    news = get_news(ticker)

    headlines = []

    for article in news:
        if article.get("title"):
            headlines.append(article["title"])

    return headlines