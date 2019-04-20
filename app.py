from flask import Flask, request, jsonify
from flask_cors import CORS
import line_api
import facebook_api
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return "Working"

@app.route('/lineWebhook', methods = ['GET', 'POST'])
def lineWebhook():
    return line_api.webhook(request)

@app.route('/facebookWebhook', methods = ['GET', 'POST'])
def facebookWebhook():
    if request.method == 'POST':
        data = request.get_json()
        message = data['entry'][0]['messaging'][0]
        sender = message['sender']['id']
        text = message['message']['text']
        print(data)
        try:
            result = text
        except:
            result = "ผมไม่เข้าใจคุณ"
        facebook_api.send(sender, result)
        return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

    elif request.method == "GET":
        token = request.args.get("hub.verify_token")
        chal = request.args.get("hub.challenge")
        print(token,chal)
        return chal
    else:
        return "POST me some JSON"

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)
