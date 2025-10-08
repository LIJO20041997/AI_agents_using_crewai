from crewai import Crew, Process
from .agents import LinkedInAgents
from .tasks import LinkedInTasks

class LinkedInPostCrew:
    def __init__(self):
        self.agents = LinkedInAgents()
        self.tasks = LinkedInTasks()
    
    def run_crew(self, topic, tone="professional"):
        # Initialize agents
        researcher = self.agents.content_researcher()
        writer = self.agents.linkedin_writer()
        optimizer = self.agents.engagement_optimizer()
        
        # Create tasks
        research_task = self.tasks.research_topic_task(researcher, topic)
        write_task = self.tasks.write_linkedin_post_task(writer, topic, tone)
        optimize_task = self.tasks.optimize_engagement_task(optimizer, topic)
        
        # Create crew
        crew = Crew(
            agents=[researcher, writer, optimizer],
            tasks=[research_task, write_task, optimize_task],
            process=Process.sequential,
            verbose=True
        )
        
        # Execute the crew
        result = crew.kickoff()
        return str(result.raw) if hasattr(result, 'raw') else str(result)