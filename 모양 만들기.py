import sys

sys.setrecursionlimit(10000)
sys.stdin = open("input.txt","r")

N,M = tuple(map(int,sys.stdin.readline().rstrip().split()))
board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]
visited = [[0 for i in range(M)] for j in range(N)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if 0<=a<N and 0<=b<M:
        return True
    return False

def dfs(curPos,union):
    global count
    for dir in direction:
        nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])
        if inRange(nextPos[0],nextPos[1]) and visited[nextPos[0]][nextPos[1]] ==0 and board[nextPos[0]][nextPos[1]] == 1:
            visited[nextPos[0]][nextPos[1]] = union
            count +=1
            dfs(nextPos,union)
union = 1
union_dict = dict()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and visited[i][j] == 0:
            count = 1
            visited[i][j] = union
            dfs((i,j),union)
            union_dict[union] = count
            union +=1

max_count = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            List = []
            for dir in direction:
                nextPos = (i+dir[0],j+dir[1])
                if inRange(nextPos[0],nextPos[1]):
                    if visited[nextPos[0]][nextPos[1]] !=0 and visited[nextPos[0]][nextPos[1]] not in List:
                        List.append(visited[nextPos[0]][nextPos[1]])

            ans = 1
            for union in List:
                ans += union_dict[union]
            if ans > max_count:
                max_count = ans
print(max_count)