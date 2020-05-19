import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

shape = [[" " for i in range(2*N-1)] for j in range(N)]

cur_1 = (N-1,0)
cur_2 = (N-1,2*N-2)

for i in range(N):
    shape[cur_1[0]][cur_1[1]] = '*'
    shape[cur_2[0]][cur_2[1]] = '*'
    cur_1 = (cur_1[0]-1,cur_1[1]+1)
    cur_2 = (cur_2[0]-1, cur_2[1]-1)

for i in range(N):
    print("".join(shape[i]).rstrip())