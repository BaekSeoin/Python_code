import sys

from collections import deque

sys.stdin = open("input.txt","r")

N,M = tuple(map(int,sys.stdin.readline().rstrip().split()))
board = [[int(i) for i in sys.stdin.readline().rstrip()] for j in range(N)]

direction = [(-1,0),(1,0),(0,1),(0,-1)]

def inRange(a,b):
    if 0<=a<N and 0<=b<M:
        return True
    return False

def bfs(List):
    global min_count
    while List:
        x = List.popleft()
        curPos = x[0]
        count = x[1]
        break_or_not = x[2]

        if curPos == (N - 1, M - 1):
            if count < min_count:
                min_count = count
            return

        if break_or_not == 0:

            for dir in direction:
                nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])
                if inRange(nextPos[0], nextPos[1]):
                    if board[nextPos[0]][nextPos[1]] == 0 and visited[0][nextPos[0]][nextPos[1]] == 0:
                        visited[0][nextPos[0]][nextPos[1]] = 1
                        List.append((nextPos, count + 1, break_or_not))
                    elif board[nextPos[0]][nextPos[1]] == 1 and visited[1][nextPos[0]][nextPos[1]] == 0:
                        visited[1][nextPos[0]][nextPos[1]] = 1
                        List.append((nextPos, count + 1, 1))
        else:
            for dir in direction:
                nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])
                if inRange(nextPos[0], nextPos[1]) and visited[1][nextPos[0]][nextPos[1]] == 0 and board[nextPos[0]][nextPos[1]] == 0:
                    visited[1][nextPos[0]][nextPos[1]] = 1
                    List.append((nextPos, count + 1, break_or_not))

List = deque()
count = 1
visited = [[[0 for i in range(M)] for j in range(N)] for k in range(2)]
visited[0][0][0] = 1
min_count = 1000**5
List.append(((0,0),count,0))
bfs(List)

if min_count == 1000**5:
    print(-1)
else:
    print(min_count)