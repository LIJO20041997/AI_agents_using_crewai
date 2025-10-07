# AI Research Assistant Crew

An intelligent research assistant powered by CrewAI that automates research, analysis, and report generation using a team of specialized AI agents.

## 🤖 Agents

- **🔍 Research Agent**: Searches web sources for the latest information using Tavily Search
- **📊 Summarizer Agent**: Condenses research findings into concise, actionable insights  
- **📝 Report Generator Agent**: Formats output into structured reports (Markdown or PDF)

## 🚀 Features

- Automated web research and data collection
- Intelligent content summarization
- Professional report generation
- Support for multiple output formats (Markdown, PDF)
- RESTful API interface
- Web-based user interface

## 🛠️ Tech Stack

- **CrewAI**: Multi-agent orchestration framework
- **LangChain**: LLM integration and tooling
- **Tavily Search**: Web search API for real-time information
- **Google Gemini**: Large language model
- **Flask**: Web framework
- **ReportLab**: PDF generation

## 📦 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Document_Parsing_Agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

4. Run the application:
```bash
python app.py
```

## 🔑 API Keys Required

- **GEMINI_API_KEY**: Get from [Google AI Studio](https://makersuite.google.com/app/apikey)
- **TAVILY_API_KEY**: Get from [Tavily](https://tavily.com/)

## 📖 Usage

### Web Interface
1. Open http://localhost:5000
2. Enter your research topic
3. Select output format (Markdown/PDF)
4. Click "Start Research"

### API Endpoints

#### Research Topic
```bash
POST /research
Content-Type: application/json

{
    "topic": "AI trends in healthcare 2024",
    "format": "markdown"
}
```

#### Health Check
```bash
GET /health
```

#### Research Status
```bash
GET /research/status
```

## 🎯 Use Cases

- **Market Research**: Analyze market trends and competitor landscape
- **Literature Reviews**: Gather and summarize academic research
- **Industry Analysis**: Research industry developments and insights
- **Competitive Intelligence**: Monitor competitor activities and strategies
- **Technology Research**: Stay updated on latest tech trends

## 📁 Project Structure

```
Document_Parsing_Agent/
├── api/
│   └── routes.py          # API endpoints
├── crew/
│   ├── agents.py          # AI agent definitions
│   ├── tasks.py           # Task definitions
│   └── crew_manager.py    # Crew orchestration
├── templates/
│   └── index.html         # Web interface
├── reports/               # Generated reports (auto-created)
├── app.py                 # Flask application
├── requirements.txt       # Dependencies
└── .env.example          # Environment template
```

## 🔧 Configuration

The system uses environment variables for configuration:

- `GEMINI_API_KEY`: Required for LLM functionality
- `TAVILY_API_KEY`: Required for web search capabilities
- `FLASK_ENV`: Development/production mode
- `FLASK_DEBUG`: Enable/disable debug mode

## 📊 Output Examples

### Research Topics
- "Electric vehicle market trends 2024"
- "Artificial intelligence in healthcare"
- "Sustainable energy solutions"
- "Remote work productivity tools"
- "Cryptocurrency market analysis"

### Report Formats
- **Markdown**: Structured text with headers, lists, and formatting
- **PDF**: Professional document with proper layout and styling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.