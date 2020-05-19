import sys

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if 0<=a < N and 0<=b <N:
        return True
    return False

def line_check(board):
    ans = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 3:
                ans +=1
    return ans

def range_check(i,j):
    if i !=0 and i != (N-1) and j !=0 and j != (N-1):
        return True
    return False

def dfs(board,depth,num_of_core):
    global Max_core, num_of_line
    count = 0

    for do in range(1,3):
        if do == 1:
            if depth + 1 < len(core):
                dfs(board,depth+1, num_of_core)
            else:
                if (num_of_core + 1) > Max_core:
                    Max_core = num_of_core
                    num_of_line = line_check(board)
                elif num_of_core  == Max_core:
                    ans = line_check(board)
                    if ans < num_of_line:
                        num_of_line = ans
        else:
            for dir in direction:
                current = core[depth]
                while True:
                    current = (current[0] + dir[0], current[1] + dir[1])
                    if inRange(current[0],current[1]) and board[current[0]][current[1]] != 0:
                        count +=1
                        while True:
                            current = (current[0] - dir[0], current[1] - dir[1])
                            if board[current[0]][current[1]] == 1:
                                break
                            board[current[0]][current[1]] = 0
                        break
                    elif inRange(current[0],current[1]) and board[current[0]][current[1]] == 0:
                        board[current[0]][current[1]] = 3
                    elif (inRange(current[0],current[1]) == False):
                        if (depth + 1 < len(core)):
                            dfs(board,depth+1,num_of_core + 1)
                        elif (depth + 1 == len(core)):
                            if (num_of_core + 1) > Max_core:
                                Max_core = num_of_core + 1
                                num_of_line = line_check(board)
                            elif (num_of_core + 1) == Max_core:
                                ans = line_check(board)
                                if ans < num_of_line:
                                    num_of_line = ans
                        while True:
                            current = (current[0] - dir[0], current[1] - dir[1])
                            if board[current[0]][current[1]] == 1:
                                break
                            board[current[0]][current[1]] = 0
                        break

            if count == 4:
                if depth > Max_core:
                    Max_core = num_of_core
                    num_of_line = line_check(board)
                elif num_of_core == Max_core:
                    ans = line_check(board)
                    if ans < num_of_line:
                        num_of_line = ans
                return

for test in range(1,T+1):
    N = int(input().rstrip())
    board = [[0 for i in range(N)] for j in range(N)]
    core = []

    for i in range(N):
        for j,num in enumerate(input().rstrip().split()):
            if (int(num) == 1) and range_check(i,j):
                core.append((i,j))
                board[i][j] = 1
            elif (int(num) == 1) and range_check(i,j) == False:
                board[i][j] = 2

    Max_core = 0
    num_of_line = 100
    dfs(board,0,0)
    print('#' + str(test),end=' ')
    print(num_of_line)