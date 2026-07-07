from app.llm.llm import llm
from langchain_core.prompts import ChatPromptTemplate


def portfolio_manager(state):

    prompt = ChatPromptTemplate.from_template("""
You are an Expert Portfolio Manager.

You have received the following reports.

========================================
Research Report
========================================
{research}

========================================
Trader Report
========================================
{trader}

========================================
Risk Report
========================================
{risk}

Your responsibility is to make the FINAL investment decision.

Provide:

## Portfolio Allocation (%)

## Recommended Investment Amount

## Number of Shares to Buy
(Assume investment amount if necessary.)

## Diversification Advice

## Investment Horizon
(Short / Medium / Long)

## Final Decision
(BUY / HOLD / SELL)

## Final Reason

## Action
(EXECUTE / WAIT / REJECT)
""")

    chain = prompt | llm

    response = chain.invoke({
        "research": state["research_report"],
        "trader": state["trader_report"],
        "risk": state["risk_report"]
    })

    state["portfolio_report"] = response.content

    return state