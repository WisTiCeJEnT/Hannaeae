import os
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
import json

last_sender = ""

try: 
    line_bot_api = LineBotApi(os.environ['LINE_CHANNEL_ACCESS_TOKEN'])
    handler = WebhookHandler(os.environ['LINE_YOUR_CHANNEL_SECRET'])   
except:
    print("Line: Get os env var error")

def webhook(flask_request):
    print("LINE_CHANNEL_ACCESS_TOKEN", os.environ['LINE_CHANNEL_ACCESS_TOKEN'])
    print("LINE_YOUR_CHANNEL_SECRET", os.environ['LINE_YOUR_CHANNEL_SECRET'])
    # get X-Line-Signature header value
    signature = flask_request.headers['X-Line-Signature']

    # get request body as text
    body = flask_request.get_data(as_text=True)
    #app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        #abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
"""
    if web_method == 'POST':
        message = data['entry'][0]['messaging'][0]
        sender = message['sender']['id']
        global last_sender
        last_sender = sender
        print(data)
        
        return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

    elif web_method == "GET":
        token = data["hub.verify_token"]
        chal = data["hub.challenge"]
        print(token,chal)
        return chal
    else:
        return "POST me some JSON"
"""
