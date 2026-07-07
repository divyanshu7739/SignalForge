from app.agents.news import news_agent
from app.agents.technical import technical_agent
from app.agents.fundamental import fundamental_agent
from app.agents.sentiment import sentiment_agent
from app.agents.bull import bull_agent
from app.agents.bear import bear_agent
from app.agents.research import research_agent
from app.agents.trader import trader_agent
from app.agents.risk import risk_manager
from app.agents.portfolio import portfolio_manager


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

print("Running Bull Researcher...")
state = bull_agent(state)

print("Running Bear Researcher...")
state = bear_agent(state)

print("Running Research Manager...")
state = research_agent(state)

print("Running Trader Agent...")
state = trader_agent(state)

print("Running Risk Manager...")
state = risk_manager(state)

print("Portfolio Manager...")
state = portfolio_manager(state)

print("\n================ FINAL RESULT ================\n")
print(state["portfolio_report"])