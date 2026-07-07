from app.tools.stock_data import get_stock_data
from app.llm.llm import llm
from langchain_core.prompts import ChatPromptTemplate


def fundamental_agent(state):

    stock = get_stock_data(state["ticker"])

    prompt = ChatPromptTemplate.from_template("""
You are an expert Fundamental Stock Analyst.

Analyze the following company information.

Company Data:

{stock}

Give:

1. Company Overview
2. Financial Strength
3. Valuation
4. Risks
5. Overall Fundamental Rating (Bullish / Neutral / Bearish)
""")

    chain = prompt | llm

    response = chain.invoke({
        "stock": stock
    })

    state["fundamental_report"] = response.content

    return state