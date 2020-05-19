import sys
import copy

sys.stdin = open("input.txt","r")

puyo = [[i for i in sys.stdin.readline().rstrip()] for i in range(12)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if (0 <= a and a < 12) and (0 <= b and b < 6):
        return True
    return False

def dfs(i,j,color,path,puyo_pass):

    puyo_pass[i][j] = 1

    for h in direction:
        nextPos = (i + h[0], j + h[1])
        if inRange(nextPos[0], nextPos[1]) and color == puyo[nextPos[0]][nextPos[1]] and puyo_pass[nextPos[0]][nextPos[1]] != 1:
            path.append(nextPos)
            dfs(nextPos[0], nextPos[1],color,path,puyo_pass)

    return path


def puyo_change(puyo,path):
    path.sort()
    for i in path:
        for j in range(i[0],0,-1):
            puyo[j][i[1]] = puyo[j-1][i[1]]
        puyo[0][i[1]] = '.'
    return puyo

count = 1
result = 0
a = [[0 for i in range(6)] for i in range(12)]

while count > 0:
    final_path = []
    count = 0
    puyo_pass = copy.deepcopy(a)

    for i in range(12):
        for j in range(6):
            color = puyo[i][j]
            if color != '.':
                path = []
                path.append((i,j))

                path = dfs(i,j,color,path,puyo_pass)
                if len(path) >= 4:
                    final_path.append(path)
                    count += 1
    if count > 0:
        result += 1
        for i in final_path:
            puyo_change(puyo,i)


print(result)
print(puyo)