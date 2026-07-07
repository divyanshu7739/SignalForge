from app.llm.llm import llm
from langchain_core.prompts import ChatPromptTemplate


def bull_agent(state):

    prompt = ChatPromptTemplate.from_template("""
You are a Bullish Equity Researcher.

Your job is to convince investors why this stock is a GOOD investment.

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

- Focus ONLY on positive points.
- Ignore bearish arguments unless absolutely necessary.
- Mention growth opportunities.
- Mention technical strengths.
- Mention fundamental strengths.
- Mention positive market sentiment.

Finally provide:

1. Bullish Score (0-100)
2. Why investors should BUY.
""")

    chain = prompt | llm

    response = chain.invoke({

        "news": state["news_report"],

        "technical": state["technical_report"],

        "fundamental": state["fundamental_report"],

        "sentiment": state["sentiment_report"]

    })

    state["bull_report"] = response.content

    return state