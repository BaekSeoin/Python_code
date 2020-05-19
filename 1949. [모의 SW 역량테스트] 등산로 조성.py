import sys

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if 0<=a < N and 0<=b<N:
        return True
    return False


def dfs(current,depth,UseorNot):
    global Max_depth, K
    count = 0
    value = Map[current[0]][current[1]]
    for dir in direction:
        nextPos = (current[0] + dir[0], current[1] + dir[1])
        if inRange(nextPos[0],nextPos[1]) and visited[nextPos[0]][nextPos[1]] == 0:
            if Map[nextPos[0]][nextPos[1]] < value:
                visited[nextPos[0]][nextPos[1]] = 1
                dfs(nextPos,depth+1,UseorNot)
                visited[nextPos[0]][nextPos[1]] = 0
            elif Map[nextPos[0]][nextPos[1]] >= value and UseorNot == 1:
                if (Map[nextPos[0]][nextPos[1]] - K) < value:
                    UseorNot = 0
                    C = Map[nextPos[0]][nextPos[1]]
                    Map[nextPos[0]][nextPos[1]] = value-1
                    visited[nextPos[0]][nextPos[1]] = 1
                    dfs(nextPos,depth+1,UseorNot)
                    Map[nextPos[0]][nextPos[1]] = C
                    visited[nextPos[0]][nextPos[1]] = 0
                    UseorNot = 1
                else:
                    count +=1
            else:
                count +=1
        else:
            count +=1
    if count == 4:
        if depth > Max_depth:
            Max_depth = depth
        return

for test in range(1,T+1):
    N,K = tuple(map(int,input().rstrip().split()))
    start = []
    Map = []
    Max = 0
    Max_depth = 0
    visited = [[0 for g in range(N)] for w in range(N)]
    for i in range(N):
        A = [int(j) for j in input().rstrip().split()]
        Map.append(A)
        b = max(A)
        if Max < b:
            start = []
            Max = b
        for index,u in enumerate(A):
            if u == Max:
                start.append((i,index))
    for A in start:
        visited[A[0]][A[1]] = 1
        dfs(A,1,1)
        visited[A[0]][A[1]] = 0
    print('#'+str(test),end=' ')
    print(Max_depth)