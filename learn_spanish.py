#!/usr/bin/python3

import random
import os

dict_dir = "./Dictionaries/"
training_dict = {}

cb_dict = True
duo_dict = True
german = True

# sorry for not using a common format
def parse_line(input_line):
    if input_line.startswith("#") or input_line.startswith("*") or input_line == "" or ("-" not in input_line):
        return None
    spanish = input_line.split("-")[0].strip()
    translation = input_line.split("-")[1].strip()
    return (spanish, translation)


def read_dictionaries():
    global training_dict

    for f in os.listdir(dict_dir):
        if (not cb_dict and "CB" in f) or (not duo_dict and "DUO" in f) or (not german and "german" in f):
            continue

        with open(os.path.join(dict_dir, f), "r") as f:
            dictionary_lines = f.read().splitlines()
    
        for l in dictionary_lines:
            parsed = parse_line(l)
            if parsed != None:
                training_dict[parsed[0]] = parsed[1]


def pretty_print_dict():
    global training_dict
    
    # find longest spanish phrase
    key_length_longest = 0
    for k in training_dict:
        if len(k) > key_length_longest:
            key_length_longest = len(k)
    
    for k in training_dict:
        padding = " " * (key_length_longest - len(k))
        print(k + padding + " -     " +  training_dict[k])

def clean_word(word):
    replace_list = ["ñ", "ú", "í", "é", " ", "[m]", "[f]", "?", "!", ".", ","]
    word = word.lower()
    for r in replace_list:
        word = word.replace(r, "")
    return word

def train():
    global training_dict

    print("Please translate the following words/phrases:")
    dict_size = len(training_dict)
    for i in range(1000):
        word_index = random.randint(0,dict_size-1)
        # 0: Translate the spanish phrase 
        # 1: Translate the english/germen phrase
        mode = random.randint(0,1)

        test = list(training_dict.items())[word_index]
        question = ""
        correct_answers = ""
        if mode == 0:
            question = test[0]
            correct_answers = test[1].split(",")
        else:
            question = test[1]
            correct_answers = [test[0]]

        print(question)
        
        answer_given = clean_word(input())
        
        # check multiple answeres (separated by comma)
        answered_correctly = False
        for a in correct_answers:
            if answer_given == clean_word(a):
                answered_correctly = True
        
        if answered_correctly:
            print("[+] Correct! \"" + question + "\" translated is: \"" + ",".join(correct_answers) + "\"")
        else:
            print("[-] Not Correct! \"" + question + "\" translated is: \"" + ",".join(correct_answers) + "\"")
        
        print()

    print("Congrats, you trained a lot today!")
    exit()


read_dictionaries()
#pretty_print_dict()
train()