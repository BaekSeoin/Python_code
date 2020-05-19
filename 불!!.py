import sys
from collections import deque

sys.stdin = open("input.txt", "r")

R,C = tuple(map(int,sys.stdin.readline().rstrip().split()))

board = []

direction = [(-1,0),(1,0),(0,-1),(0,1)]

visited = [[0 for i in range(C)] for j in range(R)]

def inRange(a,b):
    if 0<=a <R and 0<=b<C:
        return True
    return False

List= deque()

def move_fire(fire_list):
    new_fire_list = []
    for fire in fire_list:
        for dir in direction:
            nextPos = (fire[0] + dir[0],fire[1] + dir[1])
            if inRange(nextPos[0],nextPos[1]) and board[nextPos[0]][nextPos[1]] == '.' and nextPos not in new_fire_list:
                new_fire_list.append(nextPos)
                board[nextPos[0]][nextPos[1]] = 'F'
    return new_fire_list

Round =  0
end = 0
def bfs(List):
    global  Round, end
    while List:
        Round +=1
        x = List.popleft()
        current_list = x[0]
        fire_list= x[1]
        new_current_list = []
        new_fire_list = move_fire(fire_list)
        for current in current_list:
            for dir in direction:
                nextPos = (current[0] + dir[0],current[1] + dir[1])
                if not inRange(nextPos[0],nextPos[1]):
                    Round -=1
                    end = 1
                    break
                if inRange(nextPos[0],nextPos[1]) and visited[nextPos[0]][nextPos[1]] == 0 and board[nextPos[0]][nextPos[1]] == '.':
                    if nextPos[0] == 0 or nextPos[0] == (R-1) or nextPos[1] == 0 or nextPos[1] == (C-1):
                        end = 1
                        break
                    new_current_list.append(nextPos)
                    visited[nextPos[0]][nextPos[1]] = 1
            if end == 1:
                break
        if end == 1:
            break
        if len(new_current_list) > 0:
            List.append((new_current_list,new_fire_list))

current_list = []
fire_list = []
for i in range(R):
    new_board = []
    for j,x in enumerate(sys.stdin.readline().rstrip()):
        if x == 'J':
            current_list.append((i,j))
            new_board.append('.')
            visited[i][j] = 1
        elif x == 'F':
            fire_list.append((i,j))
            new_board.append('F')
        else:
            new_board.append(x)
    board.append(new_board)

List.append((current_list,fire_list))
bfs(List)

if end == 1:
    print(Round+1)
else:
    print("IMPOSSIBLE")