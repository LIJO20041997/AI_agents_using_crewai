from flask import Flask
import os
from api.routes import api

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
    
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    app.register_blueprint(api)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)