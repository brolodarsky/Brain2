"""
agent.py — Core ReAct agent logic for the Email Agent.
Uses LangGraph to orchestrate a tool-calling loop that queries the IMAP mailbox.
"""
import os
import sys
from typing import TypedDict, Annotated, Sequence
import operator

# Add engine root to sys.path for internal imports
ENGINE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if ENGINE_ROOT not in sys.path:
    sys.path.insert(0, ENGINE_ROOT)

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langgraph.graph import StateGraph, END, START
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI

from core.constants import AI_MODEL
from agents.email.tools import fetch_email_by_uid, list_recent_emails, search_emails
from agents.email.prompts import EMAIL_SYSTEM_PROMPT

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]

tools = [fetch_email_by_uid, list_recent_emails, search_emails]
tool_node = ToolNode(tools)

llm = ChatOpenAI(model=AI_MODEL, temperature=0.0)
llm_with_tools = llm.bind_tools(tools)

def call_model(state: AgentState):
    messages = state['messages']
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

workflow = StateGraph(AgentState)
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", tools_condition)
workflow.add_edge("tools", "agent")

app = workflow.compile()

def fetch_emails(query: str, thread_id: str = None) -> str:
    """
    Entry point for the Email Agent.
    Accepts a natural language query, runs the agent to fetch/search emails,
    and returns a structured JSON array of the results.
    """
    messages = [
        SystemMessage(content=EMAIL_SYSTEM_PROMPT),
        HumanMessage(content=query)
    ]
    
    config = {}
    if thread_id:
        config = {"configurable": {"thread_id": thread_id}}
        
    try:
        final_state = app.invoke({"messages": messages}, config=config)
        last_message = final_state["messages"][-1]
        return last_message.content
    except Exception as e:
        return f"[]"  # Return empty array on error to keep JSON parsing safe in Router
