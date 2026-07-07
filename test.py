from app.agents.news import news_agent
from app.agents.technical import technical_agent
from app.agents.fundamental import fundamental_agent
from app.agents.sentiment import sentiment_agent
from app.agents.research import research_agent
from app.agents.trader import trader_agent
from app.agents.bull import bull_agent


state = {
    "ticker": "AAPL"
}

print("Running News Agent...")
state = news_agent(state)

print("Running Technical Agent...")
state = technical_agent(state)

print("Running Fundamental Agent...")
state = fundamental_agent(state)

print("Running Sentiment Agent...")
state = sentiment_agent(state)

print("Running Bull Agent...")
state = bull_agent(state)
print("Running Research Agent...")


state = research_agent(state)

print("Running Trader Agent...")
state = trader_agent(state)

print("\n================ FINAL RESULT ================\n")
print(state["trader_report"])