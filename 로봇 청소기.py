import sys

sys.stdin = open("input.txt","r")

n,m = tuple(map(int,sys.stdin.readline().rstrip().split()))
r,c,d = tuple(map(int,sys.stdin.readline().rstrip().split()))
current = (r,c)

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(n)]
check = [[0 for i in range(m)] for j in range(n)]

direction = {0:[(0,-1),(1,0),(0,1),(-1,0)],
             1:[(-1,0),(0,-1),(1,0),(0,1)],
             2:[(0,1),(-1,0),(0,-1),(1,0)],
             3:[(1,0),(0,1),(-1,0),(0,-1)]}

direction_change = {0:3,1:0,2:1,3:2}

clean = 0
end = 0

def inRange(a,b):
    if 0<=a <n and 0<=b<m:
        return True
    return False

def method_1(board, check,current,d):
    global clean, end
    clean += 1
    check[current[0]][current[1]] = clean

    method_2(board,check, current,d)
    if end == 1:
        return

def method_2(board, check, current,d):
    global end
    dir = direction[d]
    count = 0
    d_2 = d
    for i in dir:
        if end == 1:
            return
        nextPos = (current[0] + i[0], current[1] + i[1])
        if inRange(nextPos[0], nextPos[1]) and board[nextPos[0]][nextPos[1]] == 0 and check[nextPos[0]][nextPos[1]] == 0:
            d = direction_change[d]
            method_1(board, check, nextPos,d)

        else:
            d = direction_change[d]
            count +=1

    if count == 4:
        nextPos = (current[0] + dir[1][0], current[1] + dir[1][1])
        if inRange(nextPos[0], nextPos[1]) and board[nextPos[0]][nextPos[1]] == 0:
            method_2(board, check, nextPos,d_2)
            if end == 1:
                return
        else:
            print(clean)
            end = 1
            return

method_1(board, check, current, d)