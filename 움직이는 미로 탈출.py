import sys
import copy
from collections import deque

sys.stdin = open("input.txt", "r")

board = [[i for i in sys.stdin.readline().rstrip()] for j in range(8)]

start = (7,0)
end = (0,7)

direction = [(0,0),(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]

def inRange(a,b):
    if 0<=a<8 and 0<=b<8:
        return True
    return False

wall = []

for i in range(7,-1,-1):
    for j in range(8):
        if board[i][j] == '#':
            wall.append((i,j))

def wall_move(wall,board,next_list):
    new_wall = []
    new_next_list = []
    for row,col in wall:
        board[row][col] = '.'
        if inRange(row+1,col):
            board[row+1][col] = '#'
            new_wall.append((row+1,col))
    for next in next_list:
        if next not in new_wall:
            new_next_list.append(next)
    return new_wall,new_next_list

List = deque()

final_ans = 0

def bfs(List):
    global  final_ans
    while List:
        x = List.popleft()
        current_List = x[0]
        cur_board = x[1]
        cur_wall = x[2]
        next_list = []

        for current in current_List:
            for dir in direction:
                nextPos = (current[0]+dir[0],current[1] + dir[1])
                if (inRange(nextPos[0],nextPos[1])) and (cur_board[nextPos[0]][nextPos[1]] == '.') and (nextPos not in next_list):
                    next_list.append(nextPos)
        new_wall, new_next_list = wall_move(cur_wall,cur_board,next_list)
        if end in new_next_list:
            final_ans = 1
            break
        if len(new_next_list) > 0:
            List.append((new_next_list,cur_board,new_wall))

List.append(([start],board,wall))
bfs(List)

print(final_ans)