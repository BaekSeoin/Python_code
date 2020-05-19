import sys

sys.stdin = open("input.txt","r")

R,C = tuple(map(int,sys.stdin.readline().rstrip().split()))

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(R)]
check = [[1 for i in range(C)] for j in range(R)]
movement = [[(-1,-1) for _ in range(C)] for j in range(R)]

direction = [(-1,0),(1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]

def inRange(a,b):
    if 0<=a<R and 0<=b <C:
        return True
    return False

def find_min(curPos,cur_value):
    min_pos = curPos
    min_value = 300000
    for dir in direction:
        nextPos = (curPos[0] + dir[0],curPos[1]+dir[1])
        if inRange(nextPos[0],nextPos[1]):
            next_value = board[nextPos[0]][nextPos[1]]
            if next_value > cur_value:
                continue
            else:
                if next_value < min_value:
                    min_value = next_value
                    min_pos = nextPos
    return min_pos

visited = [[0 for i in range(C)] for j in range(R)]

def dfs(curPos,cur_value):
    if visited[curPos[0]][curPos[1]] !=0:
        return movement[curPos[0]][curPos[1]]
    nextPos = find_min(curPos,cur_value)
    if nextPos != curPos:
        next_value = board[nextPos[0]][nextPos[1]]
        ans = dfs(nextPos,next_value)
        visited[curPos[0]][curPos[1]] = 1
        movement[curPos[0]][curPos[1]] = ans
        return ans
    else:
        visited[curPos[0]][curPos[1]] = 1
        movement[curPos[0]][curPos[1]] = curPos
        return curPos

for i in range(R):
    for j in range(C):
        curPos = (i,j)
        cur_value = board[curPos[0]][curPos[1]]
        dfs(curPos,cur_value)

for i in range(R):
    for j in range(C):
        value = check[i][j]
        nextPos = movement[i][j]

        check[i][j] -= value
        check[nextPos[0]][nextPos[1]] += value

for i in range(R):
    for j in range(C):
        print(check[i][j],end=' ')
    print()
