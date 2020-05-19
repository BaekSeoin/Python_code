import sys
import copy
from operator import itemgetter
sys.stdin = open("input.txt","r")

T = int(input())

battery = [[0 for i in range(10)] for j in range(10)]

#이동안함,상,우,하,
dir = {0:(0,0),1:(-1,0),2:(0,1),3:(1,0),4:(0,-1)}

def make_board(current,c,p,charger_num):
    #print(current)
    for i in range(10):
        for j in range(10):
            if (abs(i-current[0]) + abs(j-current[1])) <= c:
                if battery_board[i][j] == 0:
                    battery_board[i][j] = [(charger_num,p)]
                else:
                    battery_board[i][j].append((charger_num, p))

def check(pos):
    if battery_board[pos[0]][pos[1]] !=0:
        return battery_board[pos[0]][pos[1]]
    else:
        return [(0,0)]

def compare(A_result,B_result):
    A_result.sort(reverse=True,key = itemgetter(1))
    B_result.sort(reverse=True, key=itemgetter(1))
    #print(A_result,B_result)

    if A_result[0] != B_result[0]:
        return A_result[0][1] + B_result[0][1]
    else:
        if len(A_result) >=2 and len(B_result) >=2:
            compare_max = max(A_result[1][1],B_result[1][1])
            return A_result[0][1]+ compare_max
        elif len(A_result) >=2:
            return A_result[0][1]+ A_result[1][1]

        elif len(B_result) >=2:
            return B_result[0][1]+B_result[1][1]
        elif len(A_result) == 1 and len(B_result) == 1:
            return A_result[0][1]

for test in range(1,T+1):
    battery_board = copy.deepcopy(battery)
    M, BC = tuple(map(int,input().rstrip().split()))
    A = [int(i) for i in input().rstrip().split()]
    B = [int(i) for i in input().rstrip().split()]
    charger_num = 0
    for o in range(BC):
        x,y,c,p = tuple(map(int,input().rstrip().split()))
        current = (y-1,x-1)
        charger_num +=1
        make_board(current,c,p,charger_num) #c=충전범위, p=처리량

    A_pos = (0,0)
    B_pos = (9,9)

    Total = 0
    A_result = check(A_pos)
    B_result = check(B_pos)
    Total += compare(A_result,B_result)
    #print(Total)
    for a,b in zip(A,B):
        A_pos = (A_pos[0] + dir[a][0],A_pos[1] + dir[a][1])
        B_pos = (B_pos[0] + dir[b][0], B_pos[1] + dir[b][1])
        A_result = check(A_pos)
        B_result = check(B_pos)
        Total += compare(A_result,B_result)
        #print(Total)

    print('#'+str(test),end =' ')
    print(Total)