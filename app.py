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

