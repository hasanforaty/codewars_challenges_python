import string


def encode(message, key):
    cypher_list = [string.ascii_letters.index(char)+1 for char in message]
    key_string = f'{key}'
    key_length = len(key_string)-1
    key_offset = 0
    for i in range(0, len(cypher_list)):
        if key_offset > key_length:
            key_offset = 0
        cypher_list[i] = cypher_list[i]+int(key_string[key_offset])
        key_offset += 1
    return cypher_list


var = encode("scout", 1939) == [20, 12, 18, 30, 21]
va = encode("masterpiece", 1939) == [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]

print(var, va)
