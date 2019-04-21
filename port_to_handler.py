import message_handler
import firebase_api
import random
import question_handler

def random_out():
    OUT_OF_JOKE = [ 'พอเถอะ',
                    'เลิกๆๆ',
                    'อะไรวะเนี้ย',
                    'ไม่คุยด้วยล่ะ',
                    'ไปเล่นตรงนู้นเลยไป',
                    'เขาไล่มาใช่มั้ยเนี่ย',
                    'ไปหัดมาใหม่ไป',
                    'เสียงแอร์ดังเชียวว',
                    'มีอันอื่นอีกมั้ย',
                    'ไปเตรียมมุกมาใหม่!!',
                    'แถไปเรื่อยยยยย',
                    'ดึงสติหน่อยสิ',
                    'พยายามเนอะ',
                    'ก็แล้วแต่...',
                    'ไม่พบสมองในแชทนี้',
                    'ไหว้ล่ะ',
                    'ไม่พบสาระ',
                ]
    return OUT_OF_JOKE[random.randint(0, len(OUT_OF_JOKE)-1)]
def random_change_state(res_message_lists):
    return res_message_lists[random.randint(0, len(res_message_lists)-1)]

def get_reply(msg, userid):
    user_data = firebase_api.getUserData(userid)
    if(user_data == None):
        user_data = {
            "mode": 1,
            "state": 0,
            "joke_id": ""
        }
    if("ผวน" in msg):
        msg = random_change_state(["อยากผวนคำก็จัดมา", "ผวนเก่งละสิ", "อยากหัดผวนสินะ", "ผวนไม่เป็นก็บอก"])
        user_data["mode"] = 3
    elif("กูชง" in msg):
        msg = random_change_state(["ชงมาเลย!","ก็มาดิค้าบ","เริ่มได้", "เปิดเลย", "ฮันแน่!! เหงาสิท่า"])
        user_data["mode"] = 1
    elif("มึงชง" in msg):
        user_data["mode"] = 2
        q_data = question_handler.get_random_question()
        user_data["joke_id"] = q_data["joke_id"]
        msg = q_data["question"]
    elif("ช่วยด้วย" in msg):
         msg = "เลื่อนไปดูข้างบนดิสัส"
    else:
        if(user_data["mode"] == 2 and user_data["joke_id"] != ""):
            msg = message_handler.get_answer(msg,
            user_data["joke_id"],
            user_data["mode"],
            user_data["state"])
            user_data["joke_id"] = ""
            user_data["mode"] = 1
        else:
            msg = message_handler.get_answer(msg,
            user_data["joke_id"],
            user_data["mode"],
            user_data["state"])
    if (msg == None):
        msg = random_out()
        user_data["state"] = 0
    firebase_api.addUserData(userid, user_data)
    return msg

