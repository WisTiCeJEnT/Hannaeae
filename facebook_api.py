import requests as rq
import os
import message_handler
import port_to_handler

def send(recipientId, message):
    page_access_token = os.environ.get("PAGE_ACCESS_TOKEN")
    message = port_to_handler.get_reply(message)
    fbData = {
      "recipient": {
        "id": recipientId
      },
      "message": {
        "text": message
      }
    }
    res = rq.post("https://graph.facebook.com/v2.6/me/messages?access_token="+page_access_token, json = fbData)
    return res
