import sys
import copy
from collections import OrderedDict

sys.stdin = open("input.txt", "r")

N,K = tuple(map(int,sys.stdin.readline().rstrip().split()))

text = OrderedDict()
text['a'] = True
text['n'] = True
text['t'] = True
text['i'] = True
text['c'] = True

new_text = OrderedDict()

words = []

for i in range(N):
    word = sys.stdin.readline().rstrip()
    words.append(word)

for word in words:
    for i in word:
        try:
            a = text[i]
        except:
            new_text[i] = True

length = len(new_text)

def word_check(word,text):
    for x in word:
        try:
            b = text[x]
        except:
            return False
    return True

def dfs(depth,new_text):
    global Max_count, length
    if K-5 > length:
        if depth == length:
            count = 0
            for word in words:
                if word_check(word,text):
                    count +=1
            if count > Max_count:
                Max_count = count
            return
    else:
        if depth == (K-5):
            count = 0
            for word in words:
                if word_check(word, text):
                    count += 1
            if count > Max_count:
                Max_count = count
            return
        if len(new_text) < (K-5-depth):
            return

    new_text_2 = copy.deepcopy(new_text)
    for current in new_text:
        text[current] = True
        del new_text_2[current]
        dfs(depth+1,new_text_2)
        if Max_count == N:
            return
        del text[current]

Max_count = 0
dfs(0,new_text)

if K < 5:
    print(0)
else:
    print(Max_count)