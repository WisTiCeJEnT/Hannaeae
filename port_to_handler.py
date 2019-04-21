import message_handler
import firebase_api
import random

def random_out():
    OUT_OF_JOKE = [ 'พอเถอะ',
                    'เลิกๆๆ',
                    'อะไรวะเนี้ย'
                ]
    return OUT_OF_JOKE[random.randint(0, len(OUT_OF_JOKE)-1)]

def get_reply(msg, userid):
    user_data = firebase_api.getUserData(userid)
    if(user_data == None):
        user_data = {
            "mode": 1,
            "state": 0,
            "joke_id": ""
        }
    msg = message_handler.get_answer(msg,
    user_data["joke_id"],
    user_data["mode"], 
    user_data["state"])
    if (msg == None):
        msg = random_out()
        user_data["state"] = 0
    firebase_api.addUserData(userid, user_data)
    return msg

