from app.llm.llm import llm
from langchain_core.prompts import ChatPromptTemplate


def research_agent(state):

    prompt = ChatPromptTemplate.from_template("""
You are the Research Manager of a financial investment firm.

You have received reports from multiple expert analysts.

==================================================
NEWS ANALYST REPORT
==================================================
{news}

==================================================
TECHNICAL ANALYST REPORT
==================================================
{technical}

==================================================
FUNDAMENTAL ANALYST REPORT
==================================================
{fundamental}

==================================================
SENTIMENT ANALYST REPORT
==================================================
{sentiment}

==================================================
BULL RESEARCHER REPORT
==================================================
{bull}

==================================================
BEAR RESEARCHER REPORT
==================================================
{bear}

Your responsibilities:

1. Summarize all analyst reports.
2. Compare bullish and bearish arguments.
3. Highlight key opportunities.
4. Highlight major risks.
5. Resolve conflicting opinions logically.
6. Give an unbiased final investment recommendation.

Return your report in the following format:

## Executive Summary

## Bullish Arguments

## Bearish Arguments

## Opportunities

## Risks

## Final Recommendation
(BUY / HOLD / SELL)

## Confidence Score
(0-100)

## Final Reason
""")

    chain = prompt | llm

    response = chain.invoke({

        "news": state["news_report"],

        "technical": state["technical_report"],

        "fundamental": state["fundamental_report"],

        "sentiment": state["sentiment_report"],

        "bull": state["bull_report"],

        "bear": state["bear_report"]

    })

    state["research_report"] = response.content

    return state