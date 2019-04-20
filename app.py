from flask import Flask, request, jsonify
from flask_cors import CORS
import line_api
import facebook_api
import json

from scipy import spatial
import deepcut
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
@app.route('/add', methods=['POST'])
def add():
    req = eval(request.data)
    req_msg = req['req_msg']
    req_msg_tokenize = message_tokenize(req['req_msg'])
    res_msg = res_msg
    return 'Done'

def message_tokenize(message):
    return deepcut.tokenize(message)

def message_comparison(msg1, msg2):
    msg1_tokenize = message_tokenize(msg1)
    msg2_tokenize = message_tokenize(msg2)
    uniq_word = intersection(msg1_tokenize,msg2_tokenize)
    d1 = {i:0 for i in uniq_word}
    d2 = {i:0 for i in uniq_word}
    for i in msg1_tokenize:
        d1[i] += 1
    for i in msg2_tokenize:
        d2[i] += 1

    v1 = [d1[i] for i in uniq_word]
    v2 = [d2[i] for i in uniq_word]
    return 1 - spatial.distance.cosine(v1,v2)

def intersection(msg1, msg2):
    return list(set(msg1+msg2))

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)
