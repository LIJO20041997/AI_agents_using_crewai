from crewai import Agent, LLM
from crewai_tools import TavilySearchTool
import os

def get_llm():
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")
    
    return LLM(
        model="gemini/gemini-2.5-flash",
        api_key=api_key,
        temperature=0.3
    )

def get_search_tool():
    return TavilySearchTool()

def create_research_agent():
    return Agent(
        role='Research Agent',
        goal='Search web sources for the latest information on given topics',
        backstory='Expert researcher skilled in finding relevant, up-to-date information from web sources',
        llm=get_llm(),
        tools=[get_search_tool()],
        verbose=True,
        allow_delegation=False
    )

def create_summarizer_agent():
    return Agent(
        role='Summarizer Agent',
        goal='Condense research findings into concise, actionable insights',
        backstory='Expert analyst who excels at distilling complex information into clear, structured summaries',
        llm=get_llm(),
        verbose=True,
        allow_delegation=False
    )

def create_report_generator_agent():
    return Agent(
        role='Report Generator Agent',
        goal='Format research and summaries into structured reports',
        backstory='Professional report writer who creates well-structured, comprehensive documents',
        llm=get_llm(),
        verbose=True,
        allow_delegation=False
    )