from flask import Flask, request, jsonify
from flask_cors import CORS
import line_api
import facebook_api
import json
import firebase_api
from message_handler import message_tokenize

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return "Working"

@app.route('/add', methods=['POST'])
def add():
    req = eval(request.data)
    req_msg = req['req_msg']
    res_msg = req['res_msg']
    req_msg_tokenize = message_tokenize(req['req_msg'])
    res_msg_tokenize = message_tokenize(req['res_msg'])
    payload = {
        'req_msg': req_msg,
        'req_msg_tokenize': req_msg_tokenize,
        'res_msg': res_msg,
        'res_msg_tokenize': res_msg_tokenize
    }
    payload['category'] = 'general' if 'catagory' not in req else req['category']
    payload['mode'] = 1 if 'mode' not in req else req['mode']

    if payload['mode'] == 1:
        firebase_api.addNewMsg(payload)
    if payload['mode'] == 2:
        payload['description'] = '' if 'description' not in req else req['description']
        firebase_api.addNewMsgQA(payload)
    return 'Done'

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
