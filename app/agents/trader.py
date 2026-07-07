from app.llm.llm import llm
from langchain_core.prompts import ChatPromptTemplate


def trader_agent(state):

    prompt = ChatPromptTemplate.from_template("""
You are an Expert Stock Trader.

Based on the research report, make a final trading decision.

Research Report:

{report}

Return:

1. Decision (BUY / SELL / HOLD)

2. Confidence (0-100)

3. Entry Strategy

4. Exit Strategy

5. Risk Level

6. Final Reason
""")

    chain = prompt | llm

    response = chain.invoke({

        "report": state["research_report"]

    })

    state["trader_report"] = response.content

    return state