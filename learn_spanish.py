#!/usr/bin/python3

import random

spanish_german_dict = {}

# sorry for not using a common format
def parse_line(input_line):
    if input_line.startswith("#") or input_line.startswith("*") or input_line == "" or ("-" not in input_line):
        return None
    spanish = input_line.split("-")[0].strip()
    translation = input_line.split("-")[1].strip()
    return (spanish, translation)


def read_dictionary():
    global spanish_german_dict
    with open("./Dictionaries/spanish_german.txt", "r") as f:
        dictionary_lines = f.read().splitlines()
    
    for l in dictionary_lines:
        parsed = parse_line(l)
        if parsed != None:
            spanish_german_dict[parsed[0]] = parsed[1]


def pretty_print_dict():
    global spanish_german_dict
    
    # find longest spanish phrase
    key_length_longest = 0
    for k in spanish_german_dict:
        if len(k) > key_length_longest:
            key_length_longest = len(k)
    
    for k in spanish_german_dict:
        padding = " " * (key_length_longest - len(k))
        print(k + padding + " -     " +  spanish_german_dict[k])

def clean_word(word):
    replace_list = ["ñ", "ú", " ", "[m]", "[f]", "?", "!", ".", ","]
    word = word.lower()
    for r in replace_list:
        word = word.replace(r, "")
    return word

def train():
    global spanish_german_dict

    print("Please translate the following words/phrases:")
    dict_size = len(spanish_german_dict)
    for i in range(1000):
        word_index = random.randint(0,dict_size-1)
        # 0: Translate the spanish phrase 
        # 1: Translate the english/germen phrase
        mode = random.randint(0,1)

        test = list(spanish_german_dict.items())[word_index]
        question = ""
        answer = ""
        if mode == 0:
            question = test[0]
            answer = test[1]
        else:
            question = test[1]
            answer = test[0]
        
        print(question)

        answer_clean = clean_word(answer)
        answer_given = clean_word(input())

        if answer_clean == answer_given:
            print("[+] Correct! \"" + question + "\" translated is: \"" + answer + "\"")
        else:
            print("[-] Not Correct! \"" + question + "\" translated is: \"" + answer + "\"")
        
        print()

    print("Congrats, you trained a lot today!")
    exit()


read_dictionary()

#pretty_print_dict()

train()