import sys
from collections import deque

sys.stdin = open("input.txt","r")

T = int(sys.stdin.readline().rstrip())

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if (0<=a<h+2) and (0<=b<w+2):
        return True
    return False

def bfs(List):
    global ndoc, maxdoc

    Q = dict()

    while List:

        if ndoc == maxdoc:
            break

        curPos = List.popleft()

        for dir in direction:
            nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])
            if (inRange(nextPos[0],nextPos[1])) and (board[nextPos[0]][nextPos[1]] != '*') and (visit[nextPos[0]][nextPos[1]] == 0):
                x = board[nextPos[0]][nextPos[1]]

                if x == '.':
                    visit[nextPos[0]][nextPos[1]] = 1
                    List.append((nextPos))

                elif x == '$':
                    ndoc += 1
                    visit[nextPos[0]][nextPos[1]] = 1
                    List.append((nextPos))

                else:
                    if x == x.upper():
                        try:
                            p = key[x]
                            visit[nextPos[0]][nextPos[1]] = 1
                            List.append(nextPos)
                        except:
                            try:
                                Q[x].append(nextPos)
                            except:
                                Q[x] = []
                                Q[x].append(nextPos)

                    else:
                        try:
                            p = key[x.upper()]
                            visit[nextPos[0]][nextPos[1]] = 1
                            List.append(nextPos)
                        except:
                            key[x.upper()] = True
                            visit[nextPos[0]][nextPos[1]] = 1
                            List.append(nextPos)

                            try:
                                qList = Q[x.upper()]
                                for i in qList:
                                    visit[i[0]][i[1]] = 1
                                    List.append(i)
                            except:
                                continue

    return ndoc

for test in range(T):
    h,w = map(int, sys.stdin.readline().rstrip().split())
    board = [['.' for i in range(w+2)] for j in range(h+2)]
    ndoc = 0

    for i in range(h):
        for j,k in enumerate(sys.stdin.readline().rstrip()):
            board[i+1][j+1] = k


    key = dict()
    for i in sys.stdin.readline().rstrip():
        if i == '0':
            break
        key[i.upper()] = True

    List = deque()

    maxdoc = 0
    visit = [[0 for j in range(w+2)] for k in range(h+2)]

    for i in range(1,h+1):
        for j in range(1,w+1):
            if board[i][j] == '$':
                maxdoc += 1
            if board[i][j] == '*':
                continue

            if (i == 1) or (i == h):
                if board[i][j] == '.':
                    List.append((i,j))
                    visit[i][j] = 1
                elif board[i][j] == '$':
                    List.append((i,j))
                    ndoc += 1
                    visit[i][j] = 1
                elif (board[i][j] != '.') and (board[i][j] != '$'):
                    if board[i][j] == board[i][j].lower():
                        key[board[i][j].upper()] = True
                        List.append((i, j))
                        visit[i][j] = 1

            if ((j==1) or (j==w)):
                if board[i][j] == '.':
                    if (i,j) not in List:
                        List.append((i,j))
                        visit[i][j] = 1
                elif board[i][j] == '$':
                    if (i,j) not in List:
                        List.append((i,j))
                        ndoc += 1
                        visit[i][j] = 1
                elif (board[i][j] != '.') and (board[i][j] != '$'):
                    if board[i][j] == board[i][j].lower():
                        if (i,j) not in List:
                            key[board[i][j].upper()] = True
                            List.append((i, j))
                            visit[i][j] = 1

    for i in range(1,h+1):
        for j in range(1,w+1):
            if board[i][j] == '*':
                continue
            if (i == 1) or (i == h):
                if (board[i][j] != '.') and (board[i][j] != '$'):
                    if board[i][j] == board[i][j].upper():
                        try:
                            p = key[board[i][j]]
                            if (i,j) not in List:
                                List.append((i, j))
                                visit[i][j] = 1
                        except:
                            continue

            elif ((j == 1) or (j == w)):
                if (board[i][j] != '.') and (board[i][j] != '$'):
                    if board[i][j] == board[i][j].upper():
                        try:
                            p = key[board[i][j]]
                            if (i,j) not in List:
                                List.append((i, j))
                                visit[i][j] = 1
                        except:
                            continue

    print(bfs(List))
