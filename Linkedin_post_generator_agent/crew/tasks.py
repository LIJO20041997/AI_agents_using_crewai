from crewai import Task

class LinkedInTasks:
    def research_topic_task(self, agent, topic):
        return Task(
            description=f"""
            Research the topic: {topic}
            
            Your task is to:
            1. Gather current trends and insights about {topic}
            2. Find relevant statistics, facts, or recent developments
            3. Identify key talking points that would interest LinkedIn professionals
            4. Look for angles that would make the content engaging and valuable
            
            Provide a comprehensive research summary with key points, statistics, and insights.
            """,
            agent=agent,
            expected_output="A detailed research summary with key insights, statistics, and talking points about the topic"
        )
    
    def write_linkedin_post_task(self, agent, topic, tone):
        return Task(
            description=f"""
            Create an engaging LinkedIn post about: {topic}
            Tone: {tone}
            
            Your task is to:
            1. Write a compelling LinkedIn post using the research provided
            2. Use the specified tone: {tone}
            3. Include a strong hook in the first line
            4. Structure the post with proper formatting (line breaks, emojis if appropriate)
            5. Add relevant hashtags (5-10 hashtags)
            6. Include a call-to-action to encourage engagement
            7. Keep the post between 150-300 words for optimal engagement
            
            The post should be professional, engaging, and valuable to LinkedIn audience.
            """,
            agent=agent,
            expected_output="A complete LinkedIn post with proper formatting, hashtags, and call-to-action"
        )
    
    def optimize_engagement_task(self, agent, topic):
        return Task(
            description=f"""
            Optimize the LinkedIn post for maximum engagement about: {topic}
            
            Your task is to:
            1. Review the written post and enhance it for better engagement
            2. Ensure the hook is compelling and attention-grabbing
            3. Optimize hashtag selection for reach and relevance
            4. Improve the call-to-action to encourage comments and shares
            5. Add engagement-driving elements like questions or polls if appropriate
            6. Ensure proper LinkedIn formatting and best practices
            
            Provide the final optimized LinkedIn post ready for publishing.
            """,
            agent=agent,
            expected_output="A final, optimized LinkedIn post with maximum engagement potential"
        )