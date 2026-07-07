from app.llm.llm import llm
from langchain_core.prompts import ChatPromptTemplate


def risk_manager(state):

    prompt = ChatPromptTemplate.from_template("""
You are an Expert Risk Manager at a hedge fund.

You have received:

========================================
Research Report
========================================
{research}

========================================
Trader Recommendation
========================================
{trader}

Your job is to evaluate the risks before any investment is executed.

Analyze:

1. Market Risk
2. Technical Risk
3. Fundamental Risk
4. News Risk
5. Sentiment Risk

Then provide:

## Overall Risk Level
(Low / Medium / High)

## Risk Score
(0-100)

## Position Size Recommendation
(10%, 25%, 50%, 75%, 100%)

## Stop Loss Recommendation

## Take Profit Recommendation

## Major Risks

## Final Approval

(APPROVED / REJECTED)

Explain every decision.
""")

    chain = prompt | llm

    response = chain.invoke({
        "research": state["research_report"],
        "trader": state["trader_report"]
    })

    state["risk_report"] = response.content

    return state