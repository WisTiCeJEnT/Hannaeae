import deepcut

listFront = ['ใ', 'ไ', 'เ', 'แ']
listRLV = ['ร', 'ล']
list_of_word = []


def puan_kum(word):
    full_word = ''
    middle = ''
    list_of_word = deepcut.tokenize(word, custom_dict=['สวี', 'สวัส', 'ดี', 'อะ', 'ไร', 'ทำ', 'เรอ', 'เบลอ', 'ละ', 'ฟัน'])
    first_word = list_of_word[0]
    # print(first_word)
    last_word = list_of_word[-1]
    # print(last_word)

    first_alpha, f_start, f_end = find_alpha(first_word)
    # print(find_alpha(first_word))
    last_alpha, l_start, l_end = find_alpha(last_word)
    # print(find_alpha(last_word))

    new_first_word_list = list(last_word)
    # print(new_first_word_list)
    new_last_word_list = list(first_word)
    # print(new_last_word_list)

    if l_end - l_start == 2:
        del new_first_word_list[l_end - 1]
    new_first_word_list[l_start] = first_alpha

    if f_end - f_start == 2:
        del new_last_word_list[f_end - 1]
    new_last_word_list[f_start] = last_alpha

    for i in range(1, len(list_of_word) - 1):
        middle = middle + list_of_word[i]

    full_word = ''.join(new_first_word_list) + middle
    full_word = full_word + ''.join(new_last_word_list)
    return full_word


def find_alpha(word):
    first_char = word[0]
    if is_alpha(first_char):
        if word[0:2] == "อย":
            return "ย", 0, 2
        if(len(word) > 2):
            if (is_alpha(word[1]) and (not is_alpha(word[2]))) or (word[1] in listRLV):
                return word[0:2], 0, 2
        return word[0:1], 0, 1

    elif first_char in listFront:
        if is_alpha(word[1]):
            if word[1:3] == "อย":
                return "ย", 1, 3
            if (len(word) > 3):
                if (is_alpha(word[2]) and (word[2] != 'อ') and (not is_alpha(word[3]))) or (word[2] in listRLV):
                    return word[1:3], 1, 3
            elif (len(word) > 2):
                if (is_alpha(word[2]) and (word[1] == 'ห')) or (word[2] in listRLV):
                        return word[1:3], 1, 3
            return word[1:2], 1, 2

    return '-', None


def is_alpha(c):
    return (ord(c) <= 3630) and (ord(c) >= 3585)


# while 0==0:
#     word = input("word: ")
#     calculate(word)


