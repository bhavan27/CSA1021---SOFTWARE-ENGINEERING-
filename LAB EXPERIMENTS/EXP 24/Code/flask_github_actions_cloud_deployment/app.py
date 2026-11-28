from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Flask CI/CD Demo</h1>
    <p>Deployed automatically through GitHub Actions.</p>
    <p><a href='/health'>Health Check</a></p>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy", application="Flask CI/CD Demo")

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
