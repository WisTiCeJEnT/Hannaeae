import message_handler
import random

def random_out():
    OUT_OF_JOKE = [ 'พอเถอะ',
                    'เลิกๆๆ',
                    'อะไรวะเนี้ย'
                ]
    return OUT_OF_JOKE[random.randint(0, len(OUT_OF_JOKE)-1)]

def get_reply(msg):
    msg = message_handler.get_most_similar_res_msg(msg)
    if (msg == None):
        msg = random_out()
    return msg

