from app.llm.llm import llm
from langchain_core.prompts import ChatPromptTemplate


def research_agent(state):

    prompt = ChatPromptTemplate.from_template("""
You are a Senior Financial Research Analyst.

You have received reports from multiple analysts.

News Report:
{news}

Technical Report:
{technical}

Fundamental Report:
{fundamental}
                                              
Sentiment Report:
{sentiment}


Your task:

1. Summarize all reports.
2. Highlight opportunities.
3. Highlight risks.
4. Give Final Recommendation:
   - BUY
   - SELL
   - HOLD

5. Explain your reasoning.
""")

    chain = prompt | llm

    response = chain.invoke({

        "news": state["news_report"],

        "technical": state["technical_report"],

        "fundamental": state["fundamental_report"],

        "sentiment": state["sentiment_report"]

    })

    state["research_report"] = response.content

    return state