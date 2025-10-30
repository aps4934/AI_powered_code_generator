from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from .generator import generate_code

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['GET'])
def serve_frontend():
    return send_from_directory('../frontend', 'index.html')

@app.route('/index.html', methods=['GET'])
def serve_index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/generator.html', methods=['GET'])
def serve_generator():
    return send_from_directory('../frontend', 'generator.html')

@app.route('/style.css', methods=['GET'])
def serve_css():
    return send_from_directory('../frontend', 'style.css')

@app.route('/script.js', methods=['GET'])
def serve_js():
    return send_from_directory('../frontend', 'script.js')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    requirement = data.get('requirement', '')
    language = data.get('language', 'python')

    if not requirement:
        return jsonify({'error': 'Requirement is required'}), 400

    if not language:
        return jsonify({'error': 'Language is required'}), 400

    generated_code = generate_code(requirement, language)
    return jsonify({'generated_code': generated_code})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
