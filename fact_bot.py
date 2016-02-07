#!/usr/bin/python

from math import factorial #gotta save those milliseconds
import mpmath
import praw, info, sqlite3
import atoi

fact_ptn = re.compile("\d{1,3}(,?\d{3})*!")

#set unnecessary precision:
#mpmath.mp.dps = 10000  #make higher for larger numbers?

def login():
    #pretty sure I read somewhere that praw will auto re-login after expiration
    r = praw.Reddit(info.app_ua)
    r.set_oauth_app_info(info.app_id, info.app_secret, info.app_uri)
    r.refresh_access_information(info.app_refresh)
    return r

#def round_off(x):
    #round mp float to nearest ones place
    #probably a better way to do this
    #return mpmath.floor(x + mpf(.5))
#just use mpmath.nint(x)

def shorten(x):
    #returns tuple (a,b) such that x = a * 10**b
    b = mpmath.floor(mpmath.log(x)/mpmath.log(10)) - 1
    return (x/mpmath.power(10,b), b)

def stirling(x):
    #uses Stirling's approximation
    # x**y = e**(y log x) in essentially constant time
    n = mpmath.mpf(x)
    coeff = mpmath.sqrt(2 * mpmath.pi * n)
    expon = mpmath.power(n/mpmath.e, n) 
    return coeff * expon
    
def findall(comment):
    numbers = []
    start = 0
    while True:
        end = comment.find(start, '!')
        if i == -1:
            return numbers
        result = atoi.extract(comment[start:end])
        if result is not None:
            numbers.append(result)
        start = end + 1
    return numbers
        

def get_comments(r, cur):
    #return comments that haven't been seen before
    #requires praw handle, sql cursor handle
    all_comments = list(r.get_comments('all'))
    for comment in all_comments:
        comment.created_utc
        #if timestamp can be used to track posts, maybe sql db is unnecessary


def main():
    #init db if absent
    sql = sqlite3.connect('history.db')
    cur = sql.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS history(id TEXT)')




#matches = findall(fact_ptn, text)
#matches = [extract(m) for m in matches]
#print matches

'''r = login()
s = r.get_subreddit('all')
p = list(s.get_comments(limit=100))
p.reverse()

print p[0].replies'''
