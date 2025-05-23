from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"}), 200

@app.route("/about")
def about():
    return jsonify({"version": "1.0", "author": "William Yanez"}), 200

if __name__ == "__main__":
    app.run(debug=True)

# app.py
# This is a simple Flask API with two endpoints: /
# 1. The root endpoint ("/") returns a welcome message.
# 2. The "/about" endpoint returns version and author information.
# To run the API, use the command: python app.py
# The API will be accessible at http://127.0.0.1:5000/

