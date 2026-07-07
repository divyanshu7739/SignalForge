from app.tools.sentiment import get_sentiment_data
from app.llm.llm import llm
from langchain_core.prompts import ChatPromptTemplate


def sentiment_agent(state):

    headlines = get_sentiment_data(state["ticker"])

    prompt = ChatPromptTemplate.from_template("""
You are an expert Financial Sentiment Analyst.

Analyze the sentiment of these news headlines.

Headlines:
{headlines}

Return:

1. Overall Sentiment (Bullish / Bearish / Neutral)

2. Sentiment Score (0-100)

3. Positive Factors

4. Negative Factors

5. Short Summary
""")

    chain = prompt | llm

    response = chain.invoke({
        "headlines": headlines
    })

    state["sentiment_report"] = response.content

    return state