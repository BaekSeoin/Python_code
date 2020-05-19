import sys
import copy
from collections import deque

sys.stdin = open("input.txt", "r")

board = dict()

Input = [int(i) for i in sys.stdin.readline().rstrip().split()]

for index, i in enumerate(Input):
    board[index+1] = i

move = {1:[3,4,17,19,10,9,16,14],2:[1,3,5,7,9,11,24,22],3:[11,12,18,17,6,5,14,13]}
first_check = [(1,9),(9,1),(5,21),(21,5),(13,17),(17,13)]

#type-1,2,3/ dir-오른쪽(1),왼쪽(2)
def turn(type,dir,board):
    side = move[type]
    store = deque()
    for s in side:
        store.append(board[s])

    if dir == 1:
        store.rotate(2)
    elif dir == 2:
        store.rotate(-2)

    for x,y in zip(side,store):
        board[x] = y

def color_check(board):
    List = []
    for r in range(1,22,4):
        if board[r] == board[r+1] == board[r+2] == board[r+3]:
            List.append(r)
    return List

def color_check2(board):
    for r in range(1,22,4):
        if board[r] == board[r+1] == board[r+2] == board[r+3]:
            continue
        else:
            return False
    return True

List = color_check(board)

def second_check(List):
    for a in List:
        for b in List:
            if a!=b:
                if (a,b) in first_check:
                    ans = (a,b)
                    return ans
    ans = (0,0)
    return ans

ans = second_check(List)

if ans != (0,0):
    for n in range(1,3):
        board2 = copy.deepcopy(board)
        if ans[0] == 5:
            turn(1,n,board2)

        elif ans[0] == 13:
            turn(2,n,board2)

        elif ans[0] == 1:
            turn(3,n,board2)

        if color_check2(board2):
            print(1)
            break
        elif n ==1:
            continue
        else:
            print(0)
else:
    print(0)

