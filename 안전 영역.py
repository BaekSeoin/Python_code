import sys
import copy
sys.setrecursionlimit(100000)

sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())

area = [[int(i) for i in sys.stdin.readline().rstrip().split()] for i in range(n)]
direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if 0<=a<n and 0<=b<n:
        return True
    return False

check = []
for i in area:
    check.append(max(i))
Max = max(check)

def safety_zone(List_2,board):
    current = List_2.pop()

    for i in direction:
        nextPos = (current[0]+i[0], current[1] + i[1])
        if inRange(nextPos[0], nextPos[1]) and board[nextPos[0]][nextPos[1]] == 1:
            List_2.append(nextPos)
            board[nextPos[0]][nextPos[1]] = 2
            safety_zone(List_2, board)

board = [[1 for i in range(n)] for j in range(n)]
result = []
for i in range(Max+1):
    board_2 = copy.deepcopy(board)
    count = 0

    for k in range(n):
        for u in range(n):
            if area[k][u] <= i:
                board_2[k][u] = 0
    for a in range(n):
        for b in range(n):
            if board_2[a][b] == 1:
                board_2[a][b] = 2
                List_2 = []
                List_2.append((a,b))
                safety_zone(List_2, board_2)
                count +=1
    result.append(count)

print(max(result))