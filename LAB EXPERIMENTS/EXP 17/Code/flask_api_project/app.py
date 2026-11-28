from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Flask API is running!",
        "status": "success",
        "container": "Docker",
        "deployment": "Kubernetes"
    })

@app.route("/api/hello")
def hello():
    return jsonify({
        "message": "Hello from the Flask API",
        "status": "success"
    })

@app.route("/api/info")
def info():
    return jsonify({
        "application": "Experiment 17 Flask API",
        "version": "1.0",
        "framework": "Flask"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
