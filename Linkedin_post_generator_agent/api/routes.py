from flask import Blueprint, render_template, request, jsonify
from crew.crew_manager import LinkedInPostCrew
import os
from datetime import datetime

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return render_template('index.html')

@api.route('/generate_post', methods=['POST'])
def generate_post():
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        tone = data.get('tone', 'professional')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        crew = LinkedInPostCrew()
        result = crew.run_crew(topic, tone)
        
        # Save the generated post
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{topic.replace(' ', '_')}_{timestamp}.md"
        filepath = os.path.join('posts', filename)
        
        os.makedirs('posts', exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(result)
        
        return jsonify({
            'success': True,
            'post': result,
            'filename': filename
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500