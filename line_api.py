import os
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
import json
import message_handler

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
    res = message_handler.get_most_similar_res_msg(event.message.text)
    if(res == None):
        res = "GG"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=res))
