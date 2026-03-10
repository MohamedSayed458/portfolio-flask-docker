# app.py
from flask import Flask, jsonify

app = Flask(__name__)

# Route 1: Main page
@app.route('/')
def hello():
    return jsonify({"message": "Hello from Mohamed!"})

# Route 2: Health check (used by monitoring tools)
@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "portfolio-app"}), 200

# Run the app if this file is executed directly
if __name__ == '__main__':
    # host='0.0.0.0' makes it accessible outside the container
    app.run(host='0.0.0.0', port=5000, debug=True)
