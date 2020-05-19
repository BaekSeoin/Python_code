#말이 되고픈 원숭이
import sys
from collections import deque
sys.stdin = open("input.txt","r")

k = int(sys.stdin.readline().rstrip())
column, row = tuple(map(int, sys.stdin.readline().rstrip().split()))

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for i in range(row)]

discovered = [[[(-1, "None") for i in range(column)] for j in range(row)] for h in range(k+1)]

horse_direction = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
monkey_direction = [(-1,0),(0,1),(1,0),(0,-1)]

List = deque()
dist = 0
k_check = 0


List.append(((0,0),dist,k_check,"start"))
discovered[k_check][0][0] = (dist,"start")

for h in range(k+1):
    List.append(((row-1, column-1), dist, h,"end"))
    discovered[h][row-1][column-1] = (dist,"end")

ans = -1

while List:
    a = List.popleft()
    current = a[0]
    dist = a[1]
    k_check = a[2]
    point = a[3]

    """count = 0

    for i in range(0,k_check):
        if discovered[i][current[0]][current[1]] != -1:
            count +=1
            break
    if count ==1:
        continue

    if current == (row-1, column - 1):
        break"""

    if point == "start":
        if k_check < k:

            for i in horse_direction:
                nextPos = (current[0] + i[0], current[1] + i[1])
                if (0 <= nextPos[0] < row and 0 <= nextPos[1] < column) and board[nextPos[0]][nextPos[1]] != 1 and discovered[k_check + 1][nextPos[0]][nextPos[1]][1] != "start":
                    if discovered[k_check + 1][nextPos[0]][nextPos[1]][1] == "end":
                        ans = discovered[k_check + 1][nextPos[0]][nextPos[1]][0] + dist + 1
                        break
                    List.append(((nextPos[0], nextPos[1]), dist + 1, k_check + 1, "start"))
                    discovered[k_check + 1][nextPos[0]][nextPos[1]] = (dist + 1,"start")
            if discovered[k_check + 1][nextPos[0]][nextPos[1]][1] == "end":
                break

        for j in monkey_direction:
            nextPos = (current[0] + j[0], current[1] + j[1])
            if (0 <= nextPos[0] < row and 0 <= nextPos[1] < column)and board[nextPos[0]][nextPos[1]] != 1 and discovered[k_check][nextPos[0]][nextPos[1]][1] != "start":
                if discovered[k_check][nextPos[0]][nextPos[1]][1] == "end":
                    ans = discovered[k_check][nextPos[0]][nextPos[1]][0] + dist + 1
                    break
                List.append(((nextPos[0], nextPos[1]), dist + 1, k_check,"start"))
                discovered[k_check][nextPos[0]][nextPos[1]] = (dist + 1, "start")
        if discovered[k_check][nextPos[0]][nextPos[1]][1] == "end":
            break

    if point == "end":
        if k_check > 0:
            for i in horse_direction:
                nextPos = (current[0] + i[0],current[1] + i[1])
                if (0 <= nextPos[0] < row and 0 <= nextPos[1] < column) and board[nextPos[0]][nextPos[1]] != 1 and discovered[k_check-1][nextPos[0]][nextPos[1]][1] != "end":
                    if discovered[k_check-1][nextPos[0]][nextPos[1]][1] == "start":
                        ans = discovered[k_check-1][nextPos[0]][nextPos[1]][0] + dist + 1
                        break
                    List.append(((nextPos[0], nextPos[1]), dist + 1, k_check-1,"end"))
                    discovered[k_check-1][nextPos[0]][nextPos[1]] = (dist +1 , "end")
            if discovered[k_check - 1][nextPos[0]][nextPos[1]][1] == "start":
                break
        for j in monkey_direction:
            nextPos = (current[0] + j[0], current[1] + j[1])
            if (0 <= nextPos[0] < row and 0 <= nextPos[1] < column)and board[nextPos[0]][nextPos[1]] != 1 and discovered[k_check][nextPos[0]][nextPos[1]][1] != "end":
                if discovered[k_check][nextPos[0]][nextPos[1]][1] == "start":
                    ans = discovered[k_check][nextPos[0]][nextPos[1]][0] + dist + 1
                    break
                List.append(((nextPos[0], nextPos[1]), dist + 1, k_check,"end"))
                discovered[k_check][nextPos[0]][nextPos[1]] = (dist + 1, "end")
        if discovered[k_check][nextPos[0]][nextPos[1]][1] == "start":
            break
print(ans)