import sys
import copy

sys.stdin = open("input.txt", "r")

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(10)]

visited = [[0 for i in range(10)] for j in range(10)]

first =[(0,0)]
second = [(0,0),(0,1),(1,0),(1,1)]
third = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
fourth = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)]
fifth = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(2,2),(2,3),(2,4),
         (3,0),(3,1),(3,2),(3,3),(3,4),(4,0),(4,1),(4,2),(4,3),(4,4)]

store = {1:first, 2:second,3:third, 4:fourth,5:fifth}

def function(curPos,first,visited):
    for dir in first:
        nextPos = (curPos[0]+dir[0],curPos[1]+dir[1])
        if board[nextPos[0]][nextPos[1]]==1 and visited[nextPos[0]][nextPos[1]]==0:
            continue
        else:
            return False
    for dir in first:
        nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])
        visited[nextPos[0]][nextPos[1]] = 1
    return True

min_ans =100
List =[]
check = []

def dfs(check,index):
    if len(check) == 5:
        check_2 = copy.deepcopy(check)
        List.append(check_2)
        return
    for i in range(1,6):
        if i != index and i not in check:
            check.append(i)
            dfs(check,i)
            check.pop()

dfs(check,0)

def compare(board,visited):
    for i in range(10):
        for j in range(10):
            if board[i][j] != visited[i][j]:
                return False
    return True

for cur_list in List:
    ans = 0
    visited2 = copy.deepcopy(visited)
    color = [0, 0, 0, 0, 0, 0]
    for j in cur_list:
        for row in range(10-j+1):
            for col in range(10-j+1):
                curPos = (row, col)
                if board[curPos[0]][curPos[1]] == 1:
                    if function(curPos, store[j],visited2):
                        if color[j] < 5:
                            color[j] += 1
                            ans += 1
                        elif color[j] == 5:
                            color[j] +=1
                            break
            if color[j] == 6:
                break

    if compare(board, visited2):
        if ans < min_ans:
            min_ans = ans
    else:
        ans = -1

if min_ans == 100:
    if ans == -1:
        print(-1)
    else:
        print(min_ans)
else:
    print(min_ans)

