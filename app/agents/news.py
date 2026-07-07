from app.tools.news import get_news
from app.llm.llm import llm
from langchain_core.prompts import ChatPromptTemplate


def news_agent(state):

    news = get_news(state["ticker"])

    prompt = ChatPromptTemplate.from_template("""
You are a financial news analyst.

Summarize the following news.

News:
{news}
""")

    chain = prompt | llm

    response = chain.invoke({
        "news": news
    })

    state["news_report"] = response.content

    return state