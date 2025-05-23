from flask import Flask, jsonify
from datetime import UTC, datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"}), 200

@app.route("/about")
def about():
    return jsonify({"version": "1.0", "author": "William Yanez"}), 200

@app.route('/datetime', defaults={'format': 'local'})
@app.route('/datetime/<string:format>')
def current_datetime(format):
    """return the current date and time in the specified format"""
    if format.lower() == "utc":
        now = datetime.now(UTC).isoformat()
    else:
        now = datetime.now().isoformat()
    
    return jsonify({"datetime": now, "format": format}), 200

if __name__ == "__main__":
    app.run(debug=True)

# app.py
# This is a simple Flask API with two endpoints: /
# 1. The root endpoint ("/") returns a welcome message.
# 2. The "/about" endpoint returns version and author information.
# 3. The "/datetime" endpoint returns the current date and time in either UTC or local format.
# To run the API, use the command: python app.py
# The API will be accessible at http://127.0.0.1:5000/

