import sys
sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline().rstrip())
Matrix = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

Matrix_2 = [[0 for i in range(N)] for j in range(N)]

path = dict()

for i in range(N):
    path[i] = []

for i in range(N):
    for j in range(N):
        if Matrix[i][j] == 1:
            path[i].append(j)

def dfs(Matrix_2,row,next,path):

    if path[next] == []:
        return


    for i in path[next]:
        if Matrix_2[row][i] == 1:
            continue
        Matrix_2[row][i] = 1
        if row == i:
            continue
        dfs(Matrix_2,row,i,path)

for i in range(N):
    dfs(Matrix_2,i,i,path)

for i in Matrix_2:
    for j in i:
        print(j, end=' ')
    print()
