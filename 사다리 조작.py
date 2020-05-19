import sys

sys.stdin = open("input.txt","r")

N,M,H= tuple(map(int,sys.stdin.readline().rstrip().split()))

board = [[0 for i in range(N)] for j in range(H+1)]

num = 1
for _ in range(M):
    a,b = tuple(map(int,sys.stdin.readline().rstrip().split()))
    board[a-1][b-1] = num
    board[a-1][b] = num
    num +=1

min_count = 10000

def game_play(start_point):
    current= start_point
    check = False
    while True:
        if current[0] == H:
            break
        if board[current[0]][current[1]] != 0 and check == False:
            try:
                if board[current[0]][current[1]] == board[current[0]][current[1]+1]:
                    current = (current[0], current[1] + 1)
                else:
                    current = (current[0], current[1] - 1)
            except:
                current = (current[0],current[1]-1)
            check = True
        else:
            current = (current[0] + 1, current[1])
            check = False
    if current[1] == start_point[1]:
        return True
    return False

def dfs(use,curPos):
    global min_count, num
    if use > 3:
        return
    play_count = 0
    for col in range(N):
        start_point = (0,col)
        if game_play(start_point):
            play_count +=1
        else:
            break
    if play_count == N:
        if use < min_count:
            min_count = use
            return

    for i in range(curPos[0],H):
        for j in range(N-1):
            if board[i][j] ==0 and board[i][j+1] == 0:
                board[i][j] = num
                board[i][j+1]= num
                num +=1
                dfs(use+1,(i,j))
                if min_count == 1:
                    return
                board[i][j] = 0
                board[i][j+1] = 0
                num -=1
dfs(0,(0,-1))

if min_count > 3:
    print(-1)
else:
    print(min_count)