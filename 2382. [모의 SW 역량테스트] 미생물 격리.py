#미생물 격리
import sys
from collections import deque
sys.stdin = open("input.txt","r")

T = int(input())
def inRange(a,b):
    if 0<=a < n and 0 <=b <n:
        return True
    return False


def pos_change(check,List):
    result = deque()
    while List:
        a = List.popleft()
        current = a[0]
        numofbug = a[1]
        direction = a[2]

        if direction == 1:
            nextPos = (current[0]-1,current[1])
        elif direction == 2:
            nextPos = (current[0]+1, current[1])
        elif direction == 3:
            nextPos = (current[0], current[1]-1)
        else:
            nextPos = (current[0], current[1]+1)

        if inRange(nextPos[0], nextPos[1]):
            check[nextPos[0]][nextPos[1]].append((numofbug,direction))

    for i in range(n):
        for j in range(n):
            if check[i][j] != []:
                if i == 0 or i == n-1 or j == 0 or j == n-1:
                    sumofbug = check[i][j][0][0]//2
                    direction = check[i][j][0][1]
                    if direction == 1:
                        direction = 2
                    elif direction == 2:
                        direction = 1
                    elif direction ==3:
                        direction = 4
                    elif direction == 4:
                        direction = 3

                else:
                    if len(check[i][j]) == 1:
                        sumofbug = check[i][j][0][0]
                        direction = check[i][j][0][1]
                    else:
                        sumofbug = 0
                        maxindexbug = -1
                        y = 0
                        for u in check[i][j]:
                            sumofbug += u[0]
                            if u[0] > maxindexbug:
                                maxindexbug = u[0]
                                maxindex = y
                                direction = check[i][j][maxindex][1]
                            y += 1

                if sumofbug !=0:
                    result.append(((i,j),sumofbug,direction))
    return result


for i in range(T):
    n, time, k = tuple(map(int, input().rstrip().split()))
    List = deque()
    final = 0

    for j in range(k):
        a,b,c,d = tuple(map(int, input().rstrip().split()))
        List.append(((a,b),c,d))

    for q in range(time):
        check = [[[] for i in range(n)] for j in range(n)]
        List = pos_change(check,List)
    for h in List:
        final += h[1]
    print('#', end='')
    print(i+1, end = ' ')
    print(final)
