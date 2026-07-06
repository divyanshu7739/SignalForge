from typing import TypedDict


class AgentState(TypedDict):
    ticker: str
    technical_analysis: str
    news_analysis: str
    fundamental_analysis: str
    bull_case: str
    bear_case: str
    final_decision: str