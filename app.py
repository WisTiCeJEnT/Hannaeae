from flask import Flask, request, jsonify
from flask_cors import CORS
import line_api

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return "Working"

@app.route('/lineWebhook', methods = ['GET', 'POST'])
def lineWebhook():
    return line_api.webhook(request)

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)
