import sys
import math

sys.stdin = open('input.txt','r')

roomNumber = sys.stdin.readline().rstrip()

store = dict()

for i in range(10):
    store[i] = 0

for n in roomNumber:
    num = int(n)
    if num == 6:
        num = 9
    store[num] +=1

ans = 0

for k,v in store.items():
    if k == 9:
        v = int(math.ceil(v/2))
    if v > ans:
        ans = v
print(ans)

