import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

shape = [[" " for i in range(4*N-3)] for j in range(4*N-1)]

end = (2*N,2*N-2)

cur = (0,4*N-4)
cur_dir = (0,-1)

dir = {(0,-1):(1,0),(1,0):(0,1),(0,1):(-1,0),(-1,0):(0,-1)}

a = (0,0)
b = (4*N-2,0)
c = (4*N-2,4*N-4)
d = (2,4*N-4)

while cur != end:
    shape[cur[0]][cur[1]] = '*'

    if cur_dir == (0,-1):
        if cur != a:
            cur = (cur[0] + cur_dir[0], cur[1] + cur_dir[1])
        else:
            cur_dir = dir[cur_dir]
            cur = (cur[0] + cur_dir[0], cur[1] + cur_dir[1])
            a = (a[0]+2, a[1]+2)
    elif cur_dir == (1,0):
        if cur != b:
            cur = (cur[0] + cur_dir[0], cur[1] + cur_dir[1])
        else:
            cur_dir = dir[cur_dir]
            cur = (cur[0] + cur_dir[0], cur[1] + cur_dir[1])
            b = (b[0]-2, b[1]+2)
    elif cur_dir == (0,1):
        if cur != c:
            cur = (cur[0] + cur_dir[0], cur[1] + cur_dir[1])
        else:
            cur_dir = dir[cur_dir]
            cur = (cur[0] + cur_dir[0], cur[1] + cur_dir[1])
            c = (c[0]-2, c[1]-2)
    elif cur_dir == (-1,0):
        if cur != d:
            cur = (cur[0] + cur_dir[0], cur[1] + cur_dir[1])
        else:
            cur_dir = dir[cur_dir]
            cur = (cur[0] + cur_dir[0], cur[1] + cur_dir[1])
            d = (d[0]+2, d[1]-2)
shape[end[0]][end[1]] = '*'

if N == 1:
    print('*')
else:
    for i in range(4*N-1):
        print("".join(shape[i]).rstrip())


