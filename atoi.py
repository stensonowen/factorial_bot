# This library is a simple implementation of a function to convert textual
# numbers written in English into their integer representations.
#
# This code is open source according to the MIT License as follows.
#
# Copyright (c) 2008 Greg Hewgill
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import re

Small = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90
}

Magnitude = {
    'thousand':     1000,
    'million':      1000000,
    'billion':      1000000000,
    'trillion':     1000000000000,
    'quadrillion':  1000000000000000,
    'quintillion':  1000000000000000000,
    'sextillion':   1000000000000000000000,
    'septillion':   1000000000000000000000000,
    'octillion':    1000000000000000000000000000,
    'nonillion':    1000000000000000000000000000000,
    'decillion':    1000000000000000000000000000000000,
}

Translations = {
    'a': 'one',
    'dozen': 'twelve',
    'and': '',
}

valid_tokens = set("hundred")
#100 is a weird corner case so it's not in above dictionaries
for d in [Small, Magnitude, Translations]:
    valid_tokens = valid_tokens.union(set(d.keys()))
print("hundred" in valid_tokens)

class NumberException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

def prep(text):
    #format for conversion
    #ignore invalid chars, translate synonyms
    text = re.sub("[\W_]", ' ', text)
    '''tokens = [Translations[t] 
            if t in Translations and Translations[t] not None else t 
            for t in text.split()]'''
    tokens = []
    for token in text.split():
        tr = Translations.get(token)
        if tr is not None and tr is not '':
            tokens.append(Translations[token])
        elif tr is None:
            tokens.append(token)
    return tokens

def extract(text):
    tokens = prep(text)
    first = len(tokens)
    for i in range(len(tokens))[::-1]:
        print(tokens[i] + " in valid: " + str(tokens[i] in valid_tokens))
        if tokens[i] in valid_tokens:
            first = i
        else:
            break
    print('_'.join(tokens[first:]))
    return text2num(tokens[first:])

def atoi(text):
    tokens = prep(text)
    result = text2num(tokens)
    return result

def text2num(tokens):
    n = 0
    g = 0
    for w in tokens:
        x = Small.get(w, None)
        if x is not None:
            g += x
        elif w == "hundred" and g != 0:
            g *= 100
        else:
            x = Magnitude.get(w, None)
            if x is not None:
                n += g * x
                g = 0
            else:
                raise NumberException("Unknown number: "+w)
    return n + g
    
if __name__ == "__main__":
    assert 1 == atoi("one")
    assert 12 == atoi("twelve")
    assert 72 == atoi("seventy two")
    assert 300 == atoi("three hundred")
    assert 1200 == atoi("twelve hundred")
    assert 12304 == atoi("twelve thousand three hundred four")
    assert 6000000 == atoi("six million")
    assert 6400005 == atoi("six million four hundred thousand five")
    assert 123456789012 == atoi("one hundred twenty three billion four hundred fifty six million seven hundred eighty nine thousand twelve")
    assert 4000000000000000000000000000000000 == atoi("four decillion")
