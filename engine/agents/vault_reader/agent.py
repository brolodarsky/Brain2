"""
agent.py — Core ReAct agent logic for the Vault Reader.
Uses LangGraph to orchestrate a tool-calling loop that navigates the local Vault filesystem.
"""
import os
import sys
from typing import TypedDict, Annotated, Sequence
import operator
from pathlib import Path

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langgraph.graph import StateGraph, END, START
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI

from core.constants import AI_MODEL
from tools.vault_tools import read_toc, read_note, search_vault
from agents.vault_reader.prompts import SYSTEM_PROMPT

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]

tools = [read_toc, read_note, search_vault]
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

def run_ask_brain(query: str, filters: dict = None) -> str:
    """
    Entry point for the vault reader agent. Returns a string response.
    """
    try:
        final_state = execute_vault_query(query)
        last_message = final_state["messages"][-1]
        return last_message.content
    except Exception as e:
        return f"❌ Agent encountered an error: {e}"

def execute_vault_query(query: str, thread_id: str = None):
    """
    Executes a query against the vault reader agent and returns the final state.
    This is designed to be called by programmatic interfaces like the Telegram bot.
    """
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=query)
    ]
    
    config = {}
    if thread_id:
        config = {"configurable": {"thread_id": thread_id}}
        
    return app.invoke({"messages": messages}, config=config)
