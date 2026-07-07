from app.tools.technical import get_technical_indicators
from app.llm.llm import llm
from langchain_core.prompts import ChatPromptTemplate


def technical_agent(state):

    indicators = get_technical_indicators(state["ticker"])

    prompt = ChatPromptTemplate.from_template("""
You are a technical stock analyst.

Analyze these indicators.

Indicators:
{indicators}
""")

    chain = prompt | llm

    response = chain.invoke({
        "indicators": indicators
    })

    state["technical_report"] = response.content

    return state