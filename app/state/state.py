from typing import TypedDict


class AgentState(TypedDict):
    ticker: str

    news_report: str

    technical_report: str

    fundamental_report: str

    sentiment_report: str

    research_report: str

    trader_report: str

    bull_report: str