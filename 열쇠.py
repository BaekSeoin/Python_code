import sys
import copy
from collections import deque

sys.stdin = open("input.txt","r")

T = int(sys.stdin.readline().rstrip())

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if (0<=a<h+2) and (0<=b<w+2):
        return True
    return False


def bfs(List):
    global ndoc, find, maxdoc

    while List:
        if ndoc == maxdoc:
            break

        x = List.popleft()
        curPos = x[0]
        curState = x[1]

        for dir in direction:
            nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])
            if (inRange(nextPos[0],nextPos[1])) and (board[nextPos[0]][nextPos[1]] != '*'):
                x = board[nextPos[0]][nextPos[1]]

                if x == '.':
                    try:
                        y = visit[nextPos[0]][nextPos[1]][tuple(curState)]
                    except:
                        visit[nextPos[0]][nextPos[1]][tuple(curState)] = True
                        List.append((nextPos,copy.deepcopy(curState)))
                elif x == '$':
                    try:
                        y = find[nextPos]
                    except:
                        ndoc += 1
                        find[nextPos] = True
                    try:
                        y = visit[nextPos[0]][nextPos[1]][tuple(curState)]
                    except:
                        visit[nextPos[0]][nextPos[1]][tuple(curState)] = True
                        List.append((nextPos,copy.deepcopy(curState)))
                else:
                    if x == x.upper():
                        try:
                            y = dimension[x]

                            if curState[y] == 1:
                                try:
                                    z = visit[nextPos[0]][nextPos[1]][tuple(curState)]
                                except:
                                    visit[nextPos[0]][nextPos[1]][tuple(curState)] = True
                                    List.append((nextPos, copy.deepcopy(curState)))
                        except:
                            continue
                    else:
                        y = dimension[x.upper()]
                        nextState = copy.deepcopy(curState)
                        nextState[y] = 1
                        try:
                            z = visit[nextPos[0]][nextPos[1]][tuple(nextState)]
                        except:
                            visit[nextPos[0]][nextPos[1]][tuple(nextState)] = True
                            List.append((nextPos,nextState))

    try:
        del curState
        del curPos
    except:
        pass

    return ndoc


for test in range(T):
    h,w = map(int, sys.stdin.readline().rstrip().split())
    board = [['.' for i in range(w+2)] for j in range(h+2)]
    ndoc = 0
    find = dict()
    for i in range(h):
        for j,k in enumerate(sys.stdin.readline().rstrip()):
            board[i+1][j+1] = k


    key = dict()
    for i in sys.stdin.readline().rstrip():
        if i == '0':
            break
        key[i.upper()] = True

    List = []
    dimension = dict()
    cnt = 1
    maxdoc = 0
    for i in range(1,h+1):
        for j in range(1,w+1):
            if board[i][j] == '$':
                maxdoc += 1

            if (i == 1) or (i == h):
                if board[i][j] == '.':
                    List.append((i,j))
                elif board[i][j] == '$':
                    List.append((i,j))
                    ndoc += 1
                    find[(i,j)] = True
                elif (board[i][j] != '.') and (board[i][j] != '$'):
                    if board[i][j] == board[i][j].upper():
                        try:
                            p = key[board[i][j]]
                            List.append((i,j))
                        except:
                            continue
            if ((j==1) or (j==w)):
                if board[i][j] == '.':
                    if (i,j) not in List:
                        List.append((i,j))
                elif board[i][j] == '$':
                    if (i,j) not in List:
                        List.append((i,j))
                        ndoc += 1
                        find[(i,j)] = True
                elif (board[i][j] != '.') and (board[i][j] != '$'):
                    if board[i][j] == board[i][j].upper():
                        try:
                            p = key[board[i][j]]
                            if (i,j) not in List:
                                List.append((i,j))
                        except:
                            continue
            if (board[i][j] != '.') and (board[i][j] != '*') and (board[i][j] != '$'):
                try:
                    x = dimension[board[i][j].upper()]
                except:
                    dimension[board[i][j].upper()] = cnt
                    cnt +=1

    for i in range(1,h+1):
        for j in range(1,w+1):
            if (i == 1) or (i == h):
                if (board[i][j] != '.') and (board[i][j] != '.') and (board[i][j] != '$'):
                    if board[i][j] == board[i][j].lower():
                        key[board[i][j].upper()] = True
                        List.append((i,j))
            elif ((j == 1) or (j == w)):
                if (board[i][j] != '.') and (board[i][j] != '.') and (board[i][j] != '$'):
                    if board[i][j] == board[i][j].lower():
                        key[board[i][j].upper()] = True
                        if (i,j) not in List:
                            List.append((i,j))


    keyState = [0 for i in range(cnt)]
    for i,j in dimension.items():
        try:
            x = key[i]
            keyState[j] = 1
        except:
            continue

    visit = [[dict() for j in range(w+2)] for k in range(h+2)]

    newList = deque()

    for i in List:
        newList.append((i,keyState))

    print(bfs(newList))

