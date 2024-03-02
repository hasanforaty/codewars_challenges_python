import string


def decode(code, key):
    key_index = 0
    key_string = f'{key}'
    key_length = len(key_string)-1
    result = ""
    for i in range(0, len(code)):
        if key_index > key_length:
            key_index = 0
        index = code[i]-int(key_string[key_index])-1
        key_index += 1
        result += string.ascii_letters[index]
    return result


var = decode([20, 12, 18, 30, 21], 1939) == "scout"
va = decode([14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8], 1939) == "masterpiece"
print(var, va)
