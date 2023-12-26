from flask import Flask, request, jsonify
from flask_cors import CORS

import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/run_python_code', methods=['POST'])
def run_python_code():
    code = request.json.get('code', '')
    print(code)
    try:
        result = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT, text=True)
        return jsonify({'output': result.strip()})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.output.strip()})

if __name__ == '__main__':
    app.run(debug=True)