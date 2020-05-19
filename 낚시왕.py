import sys
import copy
sys.stdin = open("input.txt","r")

R,C,M = tuple(map(int, sys.stdin.readline().rstrip().split()))
board = [[0 for i in range(C)] for j in range(R)]

shark = []

direction = {1:(-1,0), 2:(1,0), 3:(0,1),4:(0,-1)}

def inRange(a,b):
    if 0<=a<R and 0<=b<C:
        return True
    return False

for i in range(M):
    r,c,s,d,z = tuple(map(int, sys.stdin.readline().rstrip().split()))
    shark.append(((r-1,c-1),s,d,z))
    board[r-1][c-1] = (s,d,z)

def shark_move(shark, check):
    shark_2 = []

    for i in shark:
        current = i[0]
        s = i[1]
        d = i[2]
        z = i[3]
        if board[current[0]][current[1]] != 0:
            if board[current[0]][current[1]] == 1:
                board[current[0]][current[1]] = check[current[0]][current[1]]
            else:
                board[current[0]][current[1]] = 0
            dir = direction[d]
            for k in range(s):
                nextPos = (current[0] + dir[0], current[1] + dir[1])
                if inRange(nextPos[0], nextPos[1]):
                    current = nextPos
                else:
                    if d % 2 == 0:
                        d -= 1
                    else:
                        d += 1
                    dir = direction[d]
                    current = (current[0] + dir[0], current[1] + dir[1])
        else:
            continue

        if check[current[0]][current[1]] == 0 and board[current[0]][current[1]]==0:
            check[current[0]][current[1]] = (s,d,z)
            board[current[0]][current[1]] = (s,d,z)
            shark_2.append((current,s,d,z))
        elif check[current[0]][current[1]] == 0 and board[current[0]][current[1]]!=0:
            check[current[0]][current[1]] = (s, d, z)
            board[current[0]][current[1]] = 1
            shark_2.append((current, s, d, z))
        else:
            if z > check[current[0]][current[1]][2]:
                a = check[current[0]][current[1]]
                Remove = (current,a[0],a[1],a[2])
                shark_2.remove(Remove)
                shark_2.append((current,s,d,z))
                check[current[0]][current[1]] = (s, d, z)
                board[current[0]][current[1]] = (s, d, z)

            else:
                continue

    return shark_2

size = 0
check = [[0 for p in range(C)] for q in range(R)]



for j in range(C):
    for i in range(R):
        if board[i][j] !=0:
            size += board[i][j][2]
            board[i][j] = 0
            break
    if j == C-1:
        break
    check_2 = copy.deepcopy(check)
    shark = shark_move(shark, check_2)

print(size)