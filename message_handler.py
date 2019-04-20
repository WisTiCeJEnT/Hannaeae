import deepcut
import firebase_api
import random
from scipy import spatial

response_correct_message = ['', '']
response_incorrect_message = ['', '']

def get_prefix_answer(is_correct_answer):
    if is_correct_answer:
        index = random.randint(0,len(response_correct_message) - 1)
        return response_correct_message[index]
    index = random.randint(0,len(response_incorrect_message) - 1)
    return response_incorrect_message[index]

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

def get_answer(mode=1, state=0, message, joke_id):
    if mode == 1:
        return get_most_similar_res_msg(message)
    if mode == 2:
        return get_result_from_qa(message, joke_id)

def get_result_from_qa(msg,joke_id):
    # response = dict(firebase_api.getAllMsg())
    joke = dict(firebase_api.getMsgQA(joke_id))
    req_msg_tokenize = message_tokenize(msg)
    tokenize = joke['res_msg_tokenize']
    score = message_comparison(tokenize, req_msg_tokenize)
    is_correct_answer = False
    if score > 0.5:
        is_correct_answer = True
    response_prefix_message = get_prefix_answer(is_correct_answer)
    description_answer = '' if 'description' in joke else joke['description']
    response_message = "{0} {1}".format(response_prefix_message, description_answer)
    return response_message


def get_most_similar_res_msg(msg):
    response = dict(firebase_api.getAllMsg())
    req_msg_tokenize = message_tokenize(msg)
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