import sys
import copy
sys.stdin = open("input.txt","r")

R, C = map(int,sys.stdin.readline().rstrip().split())

board_str = [sys.stdin.readline().rstrip() for i in range(R)]

direction = [(-1,0),(0,1),(1,0),(0,-1)]

Dict = [False for i in range(26)]

Max = 0


board = []
def make_board():
    for n in range(R):
        tmp = []
        for m in range(C):
            tmp.append(ord(board_str[n][m]) - ord('A'))
        board.append(tmp)

def InRange(b):
    if 0<= b[0] and b[0] < R and 0 <= b[1] and b[1] < C:
        return True
    False

def dfs(Dict, a):
    global Max

    maxi = 1
    for i in direction:
        nextPos = (a[0]+i[0], a[1]+i[1])
        if InRange(nextPos) and Dict[board[nextPos[0]][nextPos[1]]] == False:
            Dict[board[nextPos[0]][nextPos[1]]] = True
            tmp = 1 + dfs(Dict,nextPos)
            if maxi < tmp:
                maxi = tmp
            Dict[board[nextPos[0]][nextPos[1]]] = False

    return maxi

make_board()
Dict[board[0][0]] = True
print(dfs(Dict, (0,0)))
Dict[board[0][0]] = False

