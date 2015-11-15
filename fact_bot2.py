#!/usr/bin/python

import re
from math import factorial

fact_ptn = re.compile("\d{1,3}(,?\d{3})*!")
text = "the quick brown fox 1,111! jumps over 1!111,111!!1111! the lazy dog"

def extract(text):
    #all matches will end in exclamation marks
    #some will contain commas every three digits
    #different lines for ease of debugging errors
    text = text[:-1]
    text = text.replace(',', '')
    text = int(text)
    return text

def findall(pattern, text):
    #re.findall() does not return the same results as re.search()
    #I suspect it's because the regex is kinda repetitive?
    #This should emulate the functionality with next to no performance hit
    matches = []
    offset = 0
    m = pattern.search(text)
    while m:
        matches.append(m.group())
        offset = m.end()
        m = pattern.search(text, offset)
    return matches

matches = findall(fact_ptn, text)
matches = [extract(m) for m in matches]
print matches
