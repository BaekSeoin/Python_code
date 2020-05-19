import sys

sys.stdin = open("input.txt","r")

n,m,row,column,t = tuple(map(int, sys.stdin.readline().rstrip().split()))
Map = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(n)]
direction = [None,(0,1),(0,-1),(-1,0),(1,0)]
order = [int(i) for i in sys.stdin.readline().rstrip().split()]

dice = [[None,[2,0],None],[[4,0],[1,0],[3,0]],[None,[5,0],None],[None,[6,0],None]]

current = (row,column)

def inRange(a,b):
    global n,m
    if 0 <= a < n and 0 <= b < m:
        return True
    return False

def Dice(n,dice):
    a = dice[1][1]
    b = dice[0][1]
    c = dice[1][2]
    d = dice[1][0]
    e = dice[2][1]
    f = dice[3][1]

    if n == 1:
        dice[1][1] = d
        dice[1][2] = a
        dice[1][0] = f
        dice[3][1] = c
    elif n == 2:
        dice[1][1] = c
        dice[1][0] = a
        dice[1][2] = f
        dice[3][1] = d
    elif n == 3:
        dice[1][1] = e
        dice[2][1] = f
        dice[3][1] = b
        dice[0][1] = a
    else:
        dice[1][1] = b
        dice[2][1] = a
        dice[3][1] = e
        dice[0][1] = f

    return dice

for w in order:
    dir = direction[w]
    current = (current[0] + dir[0], current[1] + dir[1])

    if inRange(current[0],current[1]):
        dice = Dice(w, dice)

        if Map[current[0]][current[1]] == 0:
            Map[current[0]][current[1]] = dice[3][1][1]
            print(dice[1][1][1])
        else:
            number = Map[current[0]][current[1]]
            p = dice[3][1]
            dice[3][1] = [p[0],number]
            Map[current[0]][current[1]] = 0
            print(dice[1][1][1])
    else:
        current = (current[0] - dir[0], current[1] - dir[1])
        continue
