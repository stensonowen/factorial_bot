#!/usr/bin/python

import re
from math import factorial #gotta save those milliseconds
#from mpmath import pi, e, mpf, sqrt, mp
import mpmath
import praw, info

fact_ptn = re.compile("\d{1,3}(,?\d{3})*!")
text = "the quick brown fox 1,111! jumps over 1!111,111!!1111! the lazy dog"

#set unnecessary precision:
mpmath.mp.dps = 10  #make higher for larger numbers?

def login():
    #pretty sure I read somewhere that praw will auto re-login after expiration
    r = praw.Reddit(info.app_ua)
    r.set_oauth_app_info(info.app_id, info.app_secret, info.app_uri)
    r.refresh_access_information(info.app_refresh)
    return r

def round_off(x):
    #round mp float to nearest ones place
    #probably a better way to do this
    return mpmath.floor(x + mpf(.5))

def stirling(x):
    #uses Stirling's approximation
    #n = mpf(x)
    #c = mpf(2)*pi*n
    #b = n/e
    n = mpmath.mpf(x)
    b = n / mpmath.e
    return mpmath.sqrt(2 * mpmath.pi * n) * b**n
    

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

#matches = findall(fact_ptn, text)
#matches = [extract(m) for m in matches]
#print matches

r = login()
s = r.get_subreddit('gifs')
p = list(s.get_comments(limit=100))
p.reverse()

print p[0].id
