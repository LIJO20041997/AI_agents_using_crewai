from crewai import Agent
from langchain_groq import ChatGroq
import os

class LinkedInAgents:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0.7,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="groq/llama-3.1-8b-instant"
        )
    
    def content_researcher(self):
        return Agent(
            role="LinkedIn Content Researcher",
            goal="Research and gather relevant information about the given topic for LinkedIn content",
            backstory="You are an expert content researcher who specializes in finding trending topics, statistics, and insights for professional LinkedIn posts.",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def linkedin_writer(self):
        return Agent(
            role="LinkedIn Content Writer",
            goal="Create engaging and professional LinkedIn posts that drive engagement",
            backstory="You are a skilled LinkedIn content writer who knows how to craft posts that resonate with professional audiences, using proper formatting, hashtags, and call-to-actions.",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def engagement_optimizer(self):
        return Agent(
            role="LinkedIn Engagement Optimizer",
            goal="Optimize LinkedIn posts for maximum engagement and reach",
            backstory="You are an expert in LinkedIn algorithm and engagement strategies. You know how to structure posts, use hashtags, and create compelling hooks to maximize visibility.",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )