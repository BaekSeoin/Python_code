import sys
sys. setrecursionlimit(10000)
sys.stdin = open("input.txt")

n, l, r = tuple(map(int, sys.stdin.readline().rstrip().split()))

country = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(n)]

check = [[0 for i in range(n)]for j in range(n)]
direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if 0<=a <n and 0<=b<n:
        return True
    return False

def dir_check(i,j):
    for k in direction:
        nextPos = (i+k[0], j+k[1])
        if inRange(nextPos[0],nextPos[1]) and check[nextPos[0]][nextPos[1]] == 0 and (l <= abs(country[i][j] - country[nextPos[0]][nextPos[1]])<= r):
            return True
    return False


def dfs(i,j,List,union):
    global population
    current = (i,j)

    for i in direction:
        nextPos = (current[0]+i[0], current[1]+i[1])
        if inRange(nextPos[0],nextPos[1]) and check[nextPos[0]][nextPos[1]]==0 and (l<= abs(country[current[0]][current[1]]-country[nextPos[0]][nextPos[1]])<=r):
            check[nextPos[0]][nextPos[1]] = union
            List.append(nextPos)
            population += country[nextPos[0]][nextPos[1]]
            dfs(nextPos[0],nextPos[1],List,union)

count = 0
while True:
    union = 1
    check = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0 and dir_check(i,j):
                List = [(i,j)]
                check[i][j] = union
                population = country[i][j]
                dfs(i,j,List,union)
                people = population // len(List)
                union +=1
                for k in List:
                    country[k[0]][k[1]] = people
    if union != 1:
        count +=1

    else:
        break

print(count)