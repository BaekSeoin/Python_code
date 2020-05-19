import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

shape = [[" " for i in range(4*N-3)] for j in range(4*N-3)]

point = (2*N-2, 2*N-2)
row = (point[0]-2,point[0]+2)
col = (point[1]-2,point[1]+2)

for i in range(N):
    if i == 0:
        shape[point[0]][point[1]] = '*'
    else:
        for r in range(row[0],row[1]+1):
            for c in range(col[0],col[1]+1):
                if (r == row[0]) or (r == row[1]):
                    shape[r][c] = '*'
                elif (c == col[0]) or (c == col[1]):
                    shape[r][c] = '*'
        row = (row[0]-2,row[1]+2)
        col = (col[0]-2,col[1]+2)

for i in range(4*N-3):
    print("".join(shape[i]).rstrip())