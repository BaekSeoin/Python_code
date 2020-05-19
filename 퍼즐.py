import sys
import copy
from collections import deque

sys.stdin = open('input.txt','r')


board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(3)]

check = '123456780'

direction = [(-1,0),(1,0),(0,1),(0,-1)]

def inRange(a,b):
    if (0<=a<3) and (0<=b<3):
        return True
    return False


for i in range(3):
    for j in range(3):
        if board[i][j] == 0:
            curPos = (i,j)


visit = dict()

def bfs(List):
    global minCount
    while List:
        x = List.popleft()
        curPos = x[0]
        prevPos = x[1]
        count = x[2]
        curBoard = x[3]

        if curBoard == check:
            minCount = count
            return

        for dir in direction:
            nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])
            if (inRange(nextPos[0],nextPos[1])) and (nextPos != prevPos):
                nextBoard = copy.deepcopy(curBoard)
                nextBoard = [[nextBoard[0],nextBoard[1],nextBoard[2]],[nextBoard[3],nextBoard[4],nextBoard[5]],[nextBoard[6],nextBoard[7],nextBoard[8]]]
                nextBoard[curPos[0]][curPos[1]] = nextBoard[nextPos[0]][nextPos[1]]
                nextBoard[nextPos[0]][nextPos[1]] = 0
                nextBoard = "".join(list(map(str,(nextBoard[0] + nextBoard[1] + nextBoard[2]))))
                try:
                    b = visit[nextBoard]
                except:
                    List.append((nextPos,curPos,count + 1,nextBoard))
                    visit[nextBoard] = True
        del curBoard
        del curPos
        del prevPos
        del count

List = deque()

curBoard = "".join(list(map(str,(board[0] + board[1] + board[2]))))
List.append((curPos, (-1,-1),0,curBoard))
minCount = -1
visit[curBoard] = True
bfs(List)

print(minCount)