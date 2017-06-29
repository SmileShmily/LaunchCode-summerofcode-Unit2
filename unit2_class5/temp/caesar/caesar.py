"""
Example:
>>> cipher = caesar.encipher('Hello, world!', 10)
>>> cipher
'Rovvy, gybvn!'
>>> plain = caesar.decipher(cipher, 10)
>>> plain
'Hello, world!'
"""

import string
import random

def build_translation_table(offset, operation):
    assert operation in ['de', 'en'], "Operation must be either en or de"
    assert 0 <= offset <= 25, "offset must be >= 0, <= 25"

    lwr = string.ascii_lowercase
    upr = string.ascii_uppercase
    new_lwr = new_alpha(lwr, offset)
    new_upr = new_alpha(upr, offset)

    full_alpha = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    new_full_alpha = new_lwr + new_upr + string.digits + string.punctuation + string.whitespace

    if operation == 'en':
        return string.maketrans(full_alpha, new_full_alpha)
    elif operation == 'de':
        return string.maketrans(new_full_alpha, full_alpha)
    else:
        return 0

def new_alpha(alpha, offset):
    new_alpha = ''
    for i in range(len(alpha)):
            new_alpha += alpha[(i + offset) - len(alpha)]
    return new_alpha

def get_words():
    f = open('/usr/share/dict/words', 'r', 0)
    words = []
    for line in f:
        words.append(line.strip().lower())
    f.close()
    return words

def get_cipher_words(cipher):
    cipher_words = []
    word = ''
    for char in cipher:
        if char in string.ascii_letters:
            word += char.lower()
        elif len(word) > 0:
            cipher_words.append(word)
            word = ''
    if len(cipher_words) > 0:
        if cipher_words[-1] != word and word != '':
            cipher_words.append(word)
    elif word != '':
        cipher_words.append(word)
    return cipher_words

def find_key(cipher):
    words = get_words()
    cipher_words = get_cipher_words(cipher)
    for i in range(26):
        if decipher(cipher_words[0], i)in words and decipher(cipher_words[-1], i) in words:
            return i
    return False

def encipher(plain, key=None):
    if key == None:
        keys = range(1, 26)
        random.shuffle(keys)
        key = keys[0]
        print "Will use %d as key" % key
    table = build_translation_table(key, 'en')
    return plain.translate(table)

def decipher(cipher, key=None):
    if key == None:
        key = find_key(cipher)
        if not key:
            print "Key not found."
            return False
    table = build_translation_table(key, 'de')
    return cipher.translate(table)