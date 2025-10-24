from flask import Flask, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    @app.route("/api/hello")
    def hello():
        return jsonify({"message": "Hello from backend!"})
    return app
