import sys

sys.stdin = open('input.txt','r')

T = int(sys.stdin.readline().rstrip())

step = [i for i in sys.stdin.readline().rstrip()]

direction = {1:[(3,0,1),(4,0,-1)],2:[(4,0,-1),(3,0,1)],3:[(2,1,0),(1,-1,0)],4:[(1,-1,0),(2,1,0)]} #1 = 북, 2 = 남, 3 = 동, 4 = 서

cur_pos = (0,0)
cur_direction = 2
cur_dir = (1,0)

min_x = 0
min_y = 0
max_x = 0
max_y = 0

List = []
List.append(cur_pos)

for s in step:

    if s == 'F':
        cur_pos = (cur_pos[0] + cur_dir[0],cur_pos[1] + cur_dir[1])
        List.append(cur_pos)

    elif s == 'R':
        Next = direction[cur_direction][0]
        cur_direction = Next[0]
        cur_dir = (Next[1],Next[2])

    elif s == 'L':
        Next = direction[cur_direction][1]
        cur_direction = Next[0]
        cur_dir = (Next[1],Next[2])

    min_x = min(min_x,cur_pos[0])
    min_y = min(min_y, cur_pos[1])
    max_x = max(max_x, cur_pos[0])
    max_y = max(max_y, cur_pos[1])

board = [[0 for i in range(max_y + abs(min_y)+1)] for j in range(max_x+abs(min_x) + 1)]

for i,j in List:
    board[i+abs(min_x)][j+abs(min_y)] = '.'

for i in range(max_x+abs(min_x) + 1):
    for j in range(max_y + abs(min_y)+1):
        if board[i][j] == '.':
            print(board[i][j],end='')
        else:
            print('#',end='')
    print()
