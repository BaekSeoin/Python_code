import sys
from collections import deque
sys.stdin = open("input.txt","r")

T = int(input())

str = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

for i in range(T):
    n,k = tuple(map(int, input().rstrip().split()))
    result = []

    text_len = n // 4
    text = deque(j for j in input().rstrip())

    for r in range(text_len):
        for y in range(4):
            a = 0 + text_len * y
            b = text_len + text_len * y
            word = ''
            for g in range(a,b):
                e = text[g]
                word += e
            if word not in result:
                result.append(word)
        text.rotate(1)
    result.sort(reverse=True)
    final_word = result[k-1]

    count = text_len - 1
    final = 0
    for b in final_word:
        if b in str:
            num = str[b]

        else:
            num = int(b)
        final += num * 16 ** count
        count -= 1
    print('#',end='')
    print(i+1, end=' ')
    print(final)