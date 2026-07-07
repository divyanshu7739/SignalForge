from app.llm.llm import llm
from langchain_core.prompts import ChatPromptTemplate


def bear_agent(state):

    prompt = ChatPromptTemplate.from_template("""
You are a Bearish Equity Researcher.

Your job is to convince investors why this stock is a BAD investment.

You have access to:

News Report:
{news}

Technical Report:
{technical}

Fundamental Report:
{fundamental}

Sentiment Report:
{sentiment}

Instructions:

- Focus ONLY on negative points.
- Ignore bullish arguments unless absolutely necessary.
- Mention risks.
- Mention technical weaknesses.
- Mention fundamental weaknesses.
- Mention negative market sentiment.

Finally provide:

1. Bearish Score (0-100)
2. Why investors should SELL or avoid buying.
""")

    chain = prompt | llm

    response = chain.invoke({
        "news": state["news_report"],
        "technical": state["technical_report"],
        "fundamental": state["fundamental_report"],
        "sentiment": state["sentiment_report"]
    })

    state["bear_report"] = response.content

    return state