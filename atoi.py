import re
import text2num

Translations = {
    'a': 'one',
    'dozen': 'twelve',
    'and': '',
}

valid_tokens = set(["hundred"])
#100 is a weird corner case so it's not in above dictionaries
for d in [text2num.Small, text2num.Magnitude, Translations]:
    valid_tokens = valid_tokens.union(set(d.keys()))

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
        #print(tokens[i] + " in valid: " + str(tokens[i] in valid_tokens))
        if tokens[i] in valid_tokens:
            first = i
        else:
            break
    #print('_'.join(tokens[first:]))
    return text2num.text2num(tokens[first:])

def atoi(text):
    tokens = prep(text)
    result = text2num.text2num(tokens)
    return result

#TODO: allow mix of digits and words
