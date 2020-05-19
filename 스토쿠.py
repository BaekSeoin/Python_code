import sys
import copy

sys.stdin = open("input.txt","r")

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(9)]

List = []


for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            List.append((i,j))
check = [0 for k in range(10)]
check[0] = None

def range_check(a,b):
    if 0<=a<=2 and 0<=b<=2:
        row = 2
        col = 2
    elif 0<=a<=2 and 3<=b<=5:
        row = 2
        col = 5
    elif 0<=a<=2 and 6<=b<=8:
        row = 2
        col = 8
    elif 3<=a<=5 and 0<=b<=2:
        row = 5
        col = 2
    elif 3<=a<=5 and 3<=b<=5:
        row = 5
        col = 5
    elif 3<=a<=5 and 6<=b<=8:
        row = 5
        col = 8
    elif 6<=a<=8 and 0<=b<=2:
        row = 8
        col = 2
    elif 6<=a<=8 and 3<=b<=5:
        row = 8
        col = 5
    elif 6<=a<=8 and 6<=b<=8:
        row = 8
        col = 8
    return (row, col)

count = 0

def dfs(List):
    global board_2, count

    if len(List) == 0:
        board_2 = copy.deepcopy(board)
        count +=1
        return

    current = List.pop()
    check_2 = copy.deepcopy(check)
    storage = []

    for i in range(9):
        nextPos = (current[0], i)
        a = board[nextPos[0]][nextPos[1]]
        if check_2[a] ==0 and a != 0:
            check_2[a] = 1

    for j in range(9):
        nextPos = (j, current[1])
        a = board[nextPos[0]][nextPos[1]]
        if check_2[a] ==0 and a != 0:
            check_2[a] = 1

    n,m = range_check(current[0], current[1])

    for k in range(n-2,n+1):
        for h in range(m-2, m+1):
            a = board[k][h]
            if check_2[a] ==0 and a !=0:
                check_2[a] =1
    for y in range(1,10):
        if check_2[y] == 0:
            storage.append(y)

    if len(storage) == 0:
        List.append(current)
        return

    for t in storage:
        board[current[0]][current[1]] = t
        dfs(List)
        if count == 1:
            return
        else:
            board[current[0]][current[1]] = 0

    List.append(current)
    return

dfs(List)

for i in range(9):
    for j in range(9):
        print(board_2[i][j],end=' ')
    print()