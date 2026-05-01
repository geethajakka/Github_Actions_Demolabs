"""Flask web application for the calculator service."""
from flask import Flask, request, jsonify
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/')
def home():
    """Home endpoint with API documentation."""
    return {
        "message": "Calculator API",
        "endpoints": {
            "/add": "POST with JSON {'a': number, 'b': number}",
            "/subtract": "POST with JSON {'a': number, 'b': number}",
            "/multiply": "POST with JSON {'a': number, 'b': number}",
            "/divide": "POST with JSON {'a': number, 'b': number}"
        }
    }

@app.route('/add', methods=['POST'])
def add_endpoint():
    """Add two numbers."""
    try:
        data = request.get_json()
        result = add(data['a'], data['b'])
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/subtract', methods=['POST'])
def subtract_endpoint():
    """Subtract two numbers."""
    try:
        data = request.get_json()
        result = subtract(data['a'], data['b'])
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/multiply', methods=['POST'])
def multiply_endpoint():
    """Multiply two numbers."""
    try:
        data = request.get_json()
        result = multiply(data['a'], data['b'])
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/divide', methods=['POST'])
def divide_endpoint():
    """Divide two numbers."""
    try:
        data = request.get_json()
        result = divide(data['a'], data['b'])
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/health')
def health():
    """Health check endpoint."""
    return {'status': 'healthy'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
