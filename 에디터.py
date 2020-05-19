import sys
from collections import deque

sys.stdin = open("input.txt","r")


a = sys.stdin.readline().rstrip()

text = deque()

for i in a:
    text.append(i)

N = int(sys.stdin.readline().rstrip())
pos = len(text)

for j in range(N):
    b = tuple(sys.stdin.readline().rstrip().split())
    length = len(text)

    if b[0] == 'L':
        if pos == 0:
            continue
        else:
            pos -= 1
            text.rotate(1)
    elif b[0] == 'D':
        if pos == length:
            continue
        else:
            pos += 1
            text.rotate(-1)
    elif b[0] == 'B':
        if pos == 0:
            continue
        text.pop()
        pos -= 1

    elif b[0] == 'P':
        word = b[1]
        """if pos == 0:
            text.appendleft(word)"""


        text.append(word)
        pos += 1

text.rotate(pos)

print(text)