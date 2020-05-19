import sys

sys.stdin = open('input.txt','r')

year = int(sys.stdin.readline().rstrip())

if year % 4 == 0:
    if (year % 100 != 0) or (year % 400 == 0):
        print(1)
    else:
        print(0)
else:
    print(0)

