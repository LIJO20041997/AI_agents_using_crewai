from crewai import Task

def create_research_task(topic, agent):
    return Task(
        description=f"""
        Research the topic: {topic}
        
        Search for:
        - Latest information and trends
        - Key statistics and data
        - Expert opinions and insights
        - Recent developments
        - Market analysis (if applicable)
        
        Focus on finding credible, up-to-date sources.
        """,
        expected_output="Comprehensive research findings with sources, key data points, and recent developments",
        agent=agent
    )

def create_summarization_task(research_data, agent):
    return Task(
        description=f"""
        Analyze and summarize the research findings:
        
        Research Data: {research_data}
        
        Create:
        - Executive summary
        - Key insights and findings
        - Important statistics
        - Trends and patterns
        - Actionable recommendations
        """,
        expected_output="Structured summary with key insights, statistics, and actionable recommendations",
        agent=agent
    )

def create_report_task(summary_data, topic, format_type, agent):
    return Task(
        description=f"""
        Create a structured report on: {topic}
        
        Summary Data: {summary_data}
        Format: {format_type}
        
        Include:
        - Title and executive summary
        - Key findings section
        - Data and statistics
        - Conclusions and recommendations
        - Sources and references
        """,
        expected_output=f"Well-formatted {format_type} report with all sections properly structured",
        agent=agent
    )