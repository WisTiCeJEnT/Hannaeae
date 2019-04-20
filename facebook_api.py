import requests as rq
import os
import message_handler

def send(recipientId, message):
    page_access_token = os.environ.get("PAGE_ACCESS_TOKEN")
    message = message_handler.get_most_similar_res_msg(message)
    if(message == None):
        message = "GG"
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
