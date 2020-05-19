import sys
from collections import deque

sys.stdin = open('input.txt')

N,M = tuple(map(int,sys.stdin.readline().rstrip().split()))
board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]
check = [[0 for i in range(M)] for j in range(N)]

H,W,Sr,Sc,Fr,Fc = tuple(map(int,sys.stdin.readline().rstrip().split()))
Sr,Sc,Fr,Fc = Sr-1,Sc-1,Fr-1,Fc-1

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            for row in range(i - H + 1, i + 1):
                for col in range(j - W + 1, j + 1):
                    try:
                        check[row][col] = 1
                    except:
                        continue

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if 0<=a<N and 0<=b<M:
        return True
    return False

for i in range(N):
    for j in range(M):
        print(check[i][j],end=' ')
    print()

def bfs(List):
    global min_count
    end = 0
    while List:
        x = List.popleft()
        curPos = x[0]
        count = x[1]

        for dir in direction:
            nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])
            if inRange(nextPos[0], nextPos[1]) and check[nextPos[0]][nextPos[1]] == 0 and board[nextPos[0]][nextPos[1]] == 0:
                check[nextPos[0]][nextPos[1]] = 1
                List.append((nextPos,count+1))
                if nextPos == (Fr,Fc):
                    if count + 1 < min_count:
                        min_count = count+1
                    end = 1
                    break
        if end == 1:
            break


min_count = N*M + 1
List = deque()
List.append(((Sr,Sc),0))
check[Sr][Sc] = 1

if (Sr,Sc) == (Fr,Fc):
    min_count = 0
elif (N,M) == (H,W):
    min_count = -1
else:
    bfs(List)
if min_count == N*M + 1:
    print(-1)
else:
    print(min_count)
