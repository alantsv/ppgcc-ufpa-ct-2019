#!/usr/bin/env python3

def split_with_whitespace(string):
    res = [i for j in string.split() for i in (j, ' ')][:-1] 

    return res

def indices_pattern(text, pattern):
    # text_splited = text.split()
    text_splited = split_with_whitespace(text)
    indices = [index for index, word in enumerate(text_splited) if word == pattern]
    # indices = [index for index, word in enumerate(text_splited) if pattern in word]

    return indices

#if __name__ == "__main__":

text = open("demo_text.txt", "r").read()

pattern = "computador"

indices = indices_pattern(text, pattern)

print(indices)
