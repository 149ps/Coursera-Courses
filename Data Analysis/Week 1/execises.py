import random
#Problem 8

#CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}

"""
def encrypt(word,cipher_dict):
    answer=''
    for letter in word:
        answer+=cipher_dict[letter]
    return answer


print(encrypt("pig",CIPHER_DICT))
"""

#Problem 9
"""
def encrypt(word,cipher_dict):
    answer=''
    for letter in word:
        answer+=cipher_dict[letter]
    return answer


def make_decipher_dict(cipher_dict):
    decipher_dict={}
    for letter in cipher_dict:
        decipher_dict[cipher_dict[letter]]=letter
    return decipher_dict

DECIPHER_DICT = make_decipher_dict(CIPHER_DICT)

print(encrypt("pig",CIPHER_DICT))
print(encrypt(encrypt("pig", CIPHER_DICT), DECIPHER_DICT))
"""

#problem 10
def make_cipher_dict(alphabet):
    cipher_dict={}
    for letter in alphabet:
        cipher_dict[letter]=random.shuffle(letter)
    return cipher_dict

print(make_cipher_dict("cat"))
    






        