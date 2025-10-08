# LinkedIn Post Generator Agent

A CrewAI-powered agent that generates engaging LinkedIn posts using Llama2 and Groq API.

## Features

- **Content Research**: Researches topics and gathers relevant insights
- **Professional Writing**: Creates engaging LinkedIn posts with proper formatting
- **Engagement Optimization**: Optimizes posts for maximum reach and engagement
- **Multiple Tones**: Supports professional, casual, inspirational, and educational tones

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
# Add your Groq API key to .env file
GROQ_API_KEY=your_groq_api_key_here
```

3. Run the application:
```bash
python app.py
```

4. Open http://localhost:5001 in your browser

## Usage

1. Enter a topic for your LinkedIn post
2. Select the desired tone
3. Click "Generate LinkedIn Post"
4. The agent will research, write, and optimize your post

## Generated Posts

All generated posts are saved in the `posts/` directory with timestamps.