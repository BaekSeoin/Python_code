import sys

sys.stdin = open('input.txt','r')

time = [int(i) for i in sys.stdin.readline().rstrip().split()]

if time[1] >= 45:
    print(time[0], time[1] - 45)
else:
    if time[0] == 0:
        time[0] = 24
    print(time[0]-1, 60 - (45 - time[1]))