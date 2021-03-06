import sys
import copy

sys.stdin = open("input.txt","r")

n,l = tuple(map(int, sys.stdin.readline().rstrip().split()))

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(n)]

CHECK = [[0 for i in range(n)] for j in range(n)]

count = 0

def inRange(a,b):
    if 0<=a <n and 0<=b<n:
        return True
    return False

for i in range(n):
    check = 0
    CHECK_2 = copy.deepcopy(CHECK)
    for j in range(n-1):
        if board[i][j] == board[i][j+1]:
            check +=1
        elif (board[i][j] - board[i][j+1]) == -1:
            past = 0
            for k in range(1,l):
                if inRange(i,j-k) and board[i][j] == board[i][j-k] and CHECK_2[i][j-k] == 0:
                    past +=1
            if past == (l-1):
                for k in range(l):
                    CHECK_2[i][j-k] +=1
                check +=1
            else: continue
        elif (board[i][j] - board[i][j+1]) == 1:
            past = 0
            nextPos = board[i][j+1]
            for k in range(1,l+1):
                if inRange(i,j+k) and board[i][j+k] == nextPos:
                    past +=1
            if past == l:
                if inRange(i,j+l+1) and (board[i][j] == board[i][j+l+1]):
                    continue
                for r in range(1,l+1):
                    CHECK_2[i][j+r] +=1
                check +=1
            else: continue
    if check == n-1:
        count +=1


for j in range(n):
    check = 0
    CHECK_2 = copy.deepcopy(CHECK)
    for i in range(n-1):
        if board[i][j] == board[i+1][j]:
            check +=1
        elif (board[i][j] - board[i+1][j]) == -1:
            past = 0
            for k in range(1,l):
                if inRange(i-k,j) and board[i][j] == board[i-k][j] and CHECK_2[i-k][j] == 0:
                    past +=1
            if past == (l-1):
                for k in range(l):
                    CHECK_2[i-k][j] +=1
                check +=1
            else: continue
        elif (board[i][j] - board[i+1][j]) == 1:
            past = 0
            nextPos = board[i+1][j]
            for k in range(1,l+1):
                if inRange(i+k,j) and board[i+k][j] == nextPos:
                    past +=1
            if past == l:
                if inRange(i+l+1,j) and (board[i][j] == board[i+l+1][j]):
                    continue
                for r in range(1,l+1):
                    CHECK_2[i+r][j] +=1
                check +=1
            else: continue
    if check == n-1:
        count +=1
print(count)