from crewai import Crew
from crew.agents import create_research_agent, create_summarizer_agent, create_report_generator_agent
from crew.tasks import create_research_task, create_summarization_task, create_report_task
from datetime import datetime
import os

class ResearchCrewManager:
    def __init__(self):
        self.research_agent = create_research_agent()
        self.summarizer_agent = create_summarizer_agent()
        self.report_agent = create_report_generator_agent()
    
    def research_topic(self, topic: str, format_type: str = "markdown"):
        print(f"Starting AI Research Assistant for: {topic}")
        
        try:
            # Step 1: Research
            research_task = create_research_task(topic, self.research_agent)
            research_crew = Crew(
                agents=[self.research_agent],
                tasks=[research_task],
                verbose=True
            )
            
            print("Running research phase...")
            research_result = research_crew.kickoff()
            research_data = str(research_result)
            
            # Step 2: Summarize
            summary_task = create_summarization_task(research_data, self.summarizer_agent)
            summary_crew = Crew(
                agents=[self.summarizer_agent],
                tasks=[summary_task],
                verbose=True
            )
            
            print("📊 Running summarization phase...")
            summary_result = summary_crew.kickoff()
            summary_data = str(summary_result)
            
            # Step 3: Generate Report
            report_task = create_report_task(summary_data, topic, format_type, self.report_agent)
            report_crew = Crew(
                agents=[self.report_agent],
                tasks=[report_task],
                verbose=True
            )
            
            print("Running report generation phase...")
            report_result = report_crew.kickoff()
            report_content = str(report_result)
            
            # Save report
            filename = self._save_report(report_content, topic, format_type)
            
            print("Research completed successfully!")
            
            return {
                'research_data': research_data[:1000] + "..." if len(research_data) > 1000 else research_data,
                'summary': summary_data[:500] + "..." if len(summary_data) > 500 else summary_data,
                'report': report_content,
                'filename': filename,
                'topic': topic,
                'format': format_type,
                'timestamp': datetime.now().isoformat(),
                'status': 'completed'
            }
            
        except Exception as e:
            print(f"Error in research process: {str(e)}")
            return self._error_response(str(e))
    
    def _save_report(self, content: str, topic: str, format_type: str):
        """Save report to file"""
        try:
            os.makedirs('reports', exist_ok=True)
            safe_topic = "".join(c for c in topic if c.isalnum() or c in (' ', '-', '_')).rstrip()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            if format_type.lower() == "pdf":
                filename = f"reports/{safe_topic}_{timestamp}.pdf"
                self._create_pdf(content, filename)
            else:
                filename = f"reports/{safe_topic}_{timestamp}.md"
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            return filename
        except Exception as e:
            print(f"Error saving report: {str(e)}")
            return None
    
    def _create_pdf(self, content: str, filename: str):
        """Create PDF from markdown content"""
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
            from reportlab.lib.styles import getSampleStyleSheet
            
            doc = SimpleDocTemplate(filename, pagesize=letter)
            styles = getSampleStyleSheet()
            story = []
            
            # Simple text to PDF conversion
            lines = content.split('\n')
            for line in lines:
                if line.strip():
                    if line.startswith('#'):
                        story.append(Paragraph(line.replace('#', '').strip(), styles['Heading1']))
                    else:
                        story.append(Paragraph(line, styles['Normal']))
                    story.append(Spacer(1, 12))
            
            doc.build(story)
        except ImportError:
            # Fallback to markdown if reportlab not available
            with open(filename.replace('.pdf', '.md'), 'w', encoding='utf-8') as f:
                f.write(content)
    
    def _error_response(self, error_msg: str):
        return {
            'research_data': '',
            'summary': '',
            'report': '',
            'filename': None,
            'error': error_msg,
            'status': 'failed',
            'timestamp': datetime.now().isoformat()
        }