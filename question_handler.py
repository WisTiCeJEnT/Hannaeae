from firebase_api import getAllMsgQA
import random

def get_random_question():
  question_set = dict(getAllMsgQA())
  keys = list(question_set.keys())
  length = len(keys)

  index = random.randint(0,length-1)
  return {
    'question': question_set[keys[index]]['req_msg'],
    'joke_id': keys[index]

  }
