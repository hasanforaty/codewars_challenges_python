import string


def check_repeat(list, start):
    index = 0
    for i in range(start, len(list)):
        if not list[index] == list[i]:
            return False
        index += 1
    return True


def find_repeat(list):
    possible_key = [list[0]]
    for i in range(1, len(list)):
        if list[i] == possible_key[0]:
            if check_repeat(list, i):
                return possible_key
        possible_key.append(list[i])
    return possible_key


def find_the_key(message, code):
    temp_list = []
    for i in range(len(message)):
        index = string.ascii_letters.index(message[i]) + 1
        temp_list.append(code[i] - index)
    key_list = find_repeat(temp_list)
    key_str = ""
    for key in key_list:
        key_str += str(key)

    return int(key_str)


test1 = find_the_key("scout", [20, 12, 18, 30, 21]) == 1939
test2 = find_the_key("masterpiece", [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]) == 1939
test3 = find_the_key("nomoretears", [15, 17, 14, 17, 19, 7, 21, 7, 2, 20, 20]) == 12

print(test3, test2, test1)
