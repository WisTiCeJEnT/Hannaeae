import deepcut
def message_tokenize(message):
    return deepcut.tokenize(message)

def message_comparison(msg1, msg2):
    msg1_tokenize = message_tokenize(msg1)
    msg2_tokenize = message_tokenize(msg2)
    uniq_word = intersection(msg1_tokenize,msg2_tokenize)
    d1 = {i:0 for i in uniq_word}
    d2 = {i:0 for i in uniq_word}
    for i in msg1_tokenize:
        d1[i] += 1
    for i in msg2_tokenize:
        d2[i] += 1

    v1 = [d1[i] for i in uniq_word]
    v2 = [d2[i] for i in uniq_word]
    return 1 - spatial.distance.cosine(v1,v2)

def intersection(msg1, msg2):
    return list(set(msg1+msg2))