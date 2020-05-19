import sys

sys.stdin = open("input.txt","r")

n,k = tuple(map(int,sys.stdin.readline().rstrip().split()))

coin = []

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    coin.append(a)

count =0
for money in coin[::-1]:
    if money <= k:
        c = k // money
        d = k % money
        count +=c
        k = d
    if k == 0:
        print(count)
        break
