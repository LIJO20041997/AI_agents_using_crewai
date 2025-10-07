from flask import Blueprint, request, jsonify, render_template
import os
import json
from werkzeug.utils import secure_filename

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "AI Research Assistant"})

@api.route('/research', methods=['POST'])
def research_topic():
    try:
        print("📥 Received research request")
        
        data = request.get_json()
        if not data or 'topic' not in data:
            return jsonify({"error": "No topic provided"}), 400
        
        topic = data['topic']
        format_type = data.get('format', 'markdown')
        
        print(f"🔍 Topic: {topic}, Format: {format_type}")
        
        # Process research with CrewAI
        from crew.crew_manager import ResearchCrewManager
        crew_manager = ResearchCrewManager()
        result = crew_manager.research_topic(topic, format_type)
        
        print(f"✅ Research complete: {result.get('status')}")
        
        return jsonify({
            "status": "success",
            "topic": topic,
            "format": format_type,
            "result": result
        })
    
    except Exception as e:
        print(f"💥 Error in research: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@api.route('/research/status', methods=['GET'])
def research_status():
    """Get available research formats and capabilities"""
    return jsonify({
        "formats": ["markdown", "pdf"],
        "capabilities": [
            "Web search and data collection",
            "Content summarization",
            "Report generation",
            "Market research",
            "Competitor analysis",
            "Literature reviews"
        ],
        "agents": [
            "Research Agent - Web search specialist",
            "Summarizer Agent - Content analysis expert", 
            "Report Generator - Document formatting specialist"
        ]
    })