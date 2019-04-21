from firebase_api import getAllMsgQA
import random

def get_random_question():
  question_set = dict(getAllMsgQA())
  keys = question_set.keys()
  length = len(keys)

  index = random.randint(0,l-1)
  return {
    'question': question_set[keys[index]]['req_msg'],
    'joke_id': keys[index]

  }
