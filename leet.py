#! /usr/bin/evn python3

import random

ALPHA = {
    'a': ["@", "/-\\", "/\\", "aye", "/=\\", "ae"],
    'b': ["|3", "13", "l3", "]3", "|o", "1o", "lo", "]3", "|8", "l8", "18", "]8"],
    'c': ["(", "<", "[", "{", "see"],
    'd': ["l]", "|)", "1)", "[)", "|]", "1}", "])", "i>", "l>", "ol", "Ð"],
    'e': ["[-", "(-"],
    'f': ["|=", "]=", "ʃ"],
    'g': ["6", "9", "(_+", "gee", "cj", "(_-"],
    'h': ["|-|", "]-[", ")-(", "}{", "}-{"],
    'i': ["!", "|", "ai"],
    'j': ["_|", "_/", "]", "</", "_)", "_l", "u|", "(/"],
    'k': ["|<", "|{", "/<", "\\<", "kay"],
    'l': ["7", "|_", "1_", "el"],
    'm': ["|\\/|", "|v|", "nn", "(\\//)", "/|/|", "/V\\", "]\\/["],
    'n': ["|\\|", "{\\}", "]\\[", "in"],
    'o': ["0", "()", "*", "[]", "{}", "oh"],
    'p': ["|*", "|>", "1>", "?", "9", "|7", "l7", "|d", "|º", "þ", "pee"],
    'q': ["0,", "o,", "(,)", "<|", "cue", "9"],
    'r': ["|2", "l2", "lz", "[z", "Я", "|?", "l?", "1?"],
    's': ["5", "$", "z", "es"],
    't': ["7", "~|~", '"|"'],
    'u': ["|_|", "(_)", "[_]", "{_}", "\\_/", "/_/", "yuu"],
    'v': ["\\/", "√"],
    'w': ["\\/\\/", "vv", "\\x/", "\\_l_/", "\\_:_/", "uu", "1/1/"],
    'x': ["%", "><", "}{", ")("],
    'y': ["`/", "'/", "\\-/", "wai"],
    'z': ["2", "~/_", "7_", "ʒ_", "≥", ],
    '_': ['_']
}


def __replacer(text):
    random_place = random.randrange(len(text))

    while text[random_place].isnumeric():
        random_place = random.randrange(len(text))

    new_values = ALPHA[text[random_place].lower()]
    new_value = new_values[random.randrange(len(new_values))]

    text = text.replace(text[random_place], new_value, 1)
    return random_place, text, new_value


def changer(text):
    if "and" in text:
        if random.randint(0, 1) == 1:
            text = text.replace("and", "@", 1)
            return text

    return __replacer(text)
