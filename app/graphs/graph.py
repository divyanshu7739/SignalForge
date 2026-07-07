from langgraph.graph import StateGraph, END

from app.state.state import AgentState

from app.agents.news import news_agent
from app.agents.technical import technical_agent
from app.agents.fundamental import fundamental_agent
from app.agents.research import research_agent
from app.agents.trader import trader_agent


builder = StateGraph(AgentState)

builder.add_node("news", news_agent)
builder.add_node("technical", technical_agent)
builder.add_node("fundamental", fundamental_agent)
builder.add_node("research", research_agent)
builder.add_node("trader", trader_agent)


builder.set_entry_point("news")

builder.add_edge("news", "technical")
builder.add_edge("technical", "fundamental")
builder.add_edge("fundamental", "research")
builder.add_edge("research", "trader")
builder.add_edge("trader", END)


graph = builder.compile()