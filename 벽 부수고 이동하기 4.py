import sys

sys.setrecursionlimit(100000)
sys.stdin = open("input.txt", "r")

N,M = tuple(map(int,sys.stdin.readline().rstrip().split()))

board = [[int(i) for i in sys.stdin.readline().rstrip()] for j in range(N)]

visited = [[0 for i in range(M)] for j in range(N)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if 0<=a<N and 0<=b<M:
        return True
    return False

def dfs(visited,curPos,union):
    global count
    for dir in direction:
        nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])
        if inRange(nextPos[0],nextPos[1]) and board[nextPos[0]][nextPos[1]] == 0 and visited[nextPos[0]][nextPos[1]] == 0:
            visited[nextPos[0]][nextPos[1]] = union
            count += 1
            dfs(visited,nextPos,union)

union = 1
ans = dict()

for i in range(N):
    for j in range(M):
        if board[i][j] == 0 and visited[i][j] == 0:
            count = 1
            curPos = (i,j)
            visited[i][j] = union
            dfs(visited,curPos,union)
            ans[union] = count
            union += 1

for row in range(N):
    for col in range(M):
        if board[row][col] !=0:
            List = []
            final_count = 1
            for dir in direction:
                nextPos = (row+dir[0],col + dir[1])
                if inRange(nextPos[0],nextPos[1]) and visited[nextPos[0]][nextPos[1]] !=0:
                    cur_union=visited[nextPos[0]][nextPos[1]]
                    if cur_union not in List:
                        final_count += ans[cur_union]
                        List.append(cur_union)
            board[row][col] = final_count % 10

for row in range(N):
    for col in range(M):
        print(board[row][col],end='')
    print()