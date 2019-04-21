import deepcut

listFront = ['ใ', 'ไ', 'เ', 'แ']
listRLV = ['ร', 'ล']
list_vowel = ['ใ', 'ไ', 'เ', 'แ', 'ะ', 'า', 'ิ', 'ี', 'ึ', 'ื', 'ุ', 'ู', 'ำ', '่', '้', '๊', '๋']
list_of_word = []


def puan_kum(word):
    full_word = ''
    middle = ''
    list_of_word = deepcut.tokenize(word, custom_dict=['สวี', 'สวัส', 'ดี', 'อะ', 'ไร', 'ทำ', 'เรอ', 'เบลอ', 'ละ', 'ฟัน', 'นะ'])
    first_word = list_of_word[0]
    # print(first_word)
    last_word = list_of_word[-1]
    # print(last_word)
    
    f_spliter_word1, f_spliter_word2 = check_spliter(first_word)
    l_spliter_word1, l_spliter_word2 = check_spliter(last_word)
    if (f_spliter_word1 == l_spliter_word1) and (f_spliter_word2 == l_spliter_word2) and (f_spliter_word1 is not None):
        list_of_word = [f_spliter_word1, f_spliter_word2]
        first_word = f_spliter_word1
        last_word = l_spliter_word2
    else:
        if f_spliter_word1 is not None:
            del list_of_word[0]
            list_of_word = [f_spliter_word1, f_spliter_word2] + list_of_word
            first_word = f_spliter_word1

        if l_spliter_word1 is not None:
            del list_of_word[-1]
            list_of_word = list_of_word + [l_spliter_word1, l_spliter_word2]
            last_word = l_spliter_word2
    
    if len(list_of_word) == 1:
        return word

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
    if len(word) <= 1:
        return '-', 0, 1
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

    return '-', None, None


def is_alpha(c):
    return (ord(c) <= 3630) and (ord(c) >= 3585)


def check_spliter(word):
    if len(word) <= 4:
        return None, None
    if 'ี้ย' in word or 'ี่ย' in word or 'ี๊ย' in word or 'ี๋ย' in word:
        return None, None
    for i in range(0, len(word)):
        if word[i] in list_vowel and (i+1 < len(word)-1):
            if word[i+1] in list_vowel:
                return word[0:i+1], word[i+1:len(word)]
            if i+2 < len(word):
                if word[i+2] in list_vowel:
                    return word[0:i+1], word[i+1:len(word)]
            if i+3 < len(word):
                if word[i+3] in list_vowel:
                    return word[0:i+2], word[i+2:len(word)]
    return None, None


while 0==0:
    word = input("word: ")
    print(puan_kum(word))


