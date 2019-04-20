import deepcut
import firebase_api
import random
from scipy import spatial
import random
def message_tokenize(message):
    return deepcut.tokenize(message)

def message_comparison(msg1, msg2):
    uniq_word = intersection(msg1,msg2)
    d1 = {i:0 for i in uniq_word}
    d2 = {i:0 for i in uniq_word}
    for i in msg1:
        d1[i] += 1
    for i in msg2:
        d2[i] += 1

    v1 = [d1[i] for i in uniq_word]
    v2 = [d2[i] for i in uniq_word]
    return 1 - spatial.distance.cosine(v1,v2)

def intersection(msg1, msg2):
    return list(set(msg1+msg2))

def get_most_similar_res_msg(req_msg):
  response = dict(firebase_api.getAllMsg())
  req_msg_tokenize = message_tokenize(req_msg)
  answer = []
  sum_score = 0
  for i in response:
      if 'req_msg_tokenize' not in response[i]:
          continue
      tokenize = response[i]['req_msg_tokenize']
      score = message_comparison(req_msg_tokenize, tokenize)
      if score > 0.5:
          previous_score = sum_score
          sum_score+=score
          answer.append((previous_score, sum_score, response[i]['res_msg']))
      ran_val = random.uniform(0, sum_score)
  for i in answer:
    if ran_val < i[1] and ran_val > i[0]:
      return i[2]



