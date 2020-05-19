import sys
import copy
from collections import deque

sys.stdin = open("input.txt","r")

T = int(sys.stdin.readline().rstrip())

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if 0<=a<5 and 0<=b<9:
        return True
    return False

def bfs(List):
    global Min_pin, Min_count
    while List:
        x = List.popleft()
        collect = x[0]
        board = x[1]
        count = x[2]

        for j in collect:
            current = j
            for i in direction:
                nextPos = (current[0]+i[0], current[1]+i[1])
                next_nextPos = (current[0]+i[0]*2, current[1]+i[1]*2)
                if inRange(nextPos[0],nextPos[1]) and inRange(next_nextPos[0],next_nextPos[1]) and \
                        board[nextPos[0]][nextPos[1]] == 'o' and board[next_nextPos[0]][next_nextPos[1]] == '.':
                    board_2 = copy.deepcopy(board)
                    collect_2 = []
                    board_2[current[0]][current[1]] = '.'
                    board_2[nextPos[0]][nextPos[1]] = '.'
                    board_2[next_nextPos[0]][next_nextPos[1]] = 'o'
                    c = 0
                    for k in range(5):
                        for y in range(9):
                            if board_2[k][y] == 'o':
                                collect_2.append((k,y))
                                c +=1

                    if c <= Min_pin:
                        Min_pin = c
                        Min_count = count + 1
                        #print(Min_pin, Min_count)
                        collect_3 = copy.deepcopy(collect_2)
                        List.append((collect_3,board_2,count+1))



for t in range(T):
    board = [[i for i in sys.stdin.readline().rstrip()] for j in range(5)]
    a = sys.stdin.readline().rstrip()
    count = 0
    List = deque()
    collect = []
    for i in range(5):
        for j in range(9):
            if board[i][j] == 'o':
                collect.append((i,j))
    board_2 = copy.deepcopy(board)
    Min_pin = len(collect)
    Min_count = 0

    List.append((collect, board_2, count))
    bfs(List)
    print(Min_pin, Min_count)