import sys

sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline().rstrip())

if N ==4 or N == 7:
    print(-1)
elif N == 3 or N == 5:
    print(1)
elif N == 6:
    print(2)
else:
    if N % 5 == 3:
        count = (N - 3) // 5 + 1
    if N % 5 == 4:
        count = (N- 3*3) // 5 + 3
    if N % 5 == 0:
        count = (N - 3*0) // 5
    if N % 5 == 1:
        count = (N - 3*2)//5 + 2
    if N % 5 == 2:
        count = (N-3*4)//5 + 4
    print(count)