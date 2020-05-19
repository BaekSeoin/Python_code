import sys

sys.stdin = open("input.txt","r")

T = int(input())

def inRange(a,b,N):
    if 0 <= a < N and 0 <= b < N:
        return True
    return False

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def direction_change(dir,triangle):
    if triangle == 1:
        if dir == (0,1):
            dir = (0,-1)
        elif dir == (-1,0):
            dir = (1,0)
        elif dir == (1,0):
            dir = (0,1)
        else:
            dir = (-1,0)
    elif triangle == 2:
        if dir == (0,1):
            dir = (0,-1)
        elif dir == (1,0):
            dir = (-1,0)
        elif dir == (0,-1):
            dir = (1,0)
        else:
            dir = (0,1)
    elif triangle == 3:
        if dir == (0,1):
            dir = (1,0)
        elif dir == (-1,0):
            dir = (0,-1)
        elif dir == (1,0):
            dir = (-1,0)
        else:
            dir = (0,1)
    elif triangle == 4:
        if dir == (0,1):
            dir = (-1,0)
        elif dir == (1,0):
            dir = (0,-1)
        elif dir == (-1,0):
            dir = (1,0)
        else:
            dir = (0,1)
    elif triangle == 5:
        if dir == (0,1):
            dir = (0,-1)
        elif dir == (-1,0):
            dir = (1,0)
        elif dir == (0,-1):
            dir = (0,1)
        else:
            dir = (-1,0)
    return dir

def start(current,dir,game,N):
    start_pos = current
    count = 0
    while True:
        current = (current[0] + dir[0], current[1] + dir[1])

        if inRange(current[0],current[1],N) == False:
            count +=1
            current = (current[0] - dir[0], current[1] - dir[1])
            dir = direction_change(dir,5)

        status = game[current[0]][current[1]]
        if current == start_pos:
            return count
        elif status == 0:
            continue
        elif 1 <= status <=5:
            dir = direction_change(dir,status)
            count +=1
        elif 6 <= status <= 10:
            warm = warmhole[status]
            if current == warm[0]:
                current = warm[1]
            else:
                current = warm[0]
        elif status == -1:
            return count

for test in range(1,T+1):
    N = int(input())
    warmhole = dict()
    game = []
    for i in range(N):
        A = []
        for index,j in enumerate(input().rstrip().split()):
            A.append(int(j))
            if 6<= int(j) <=10:
                try:
                    warmhole[int(j)].append((i,index))
                except:
                    warmhole[int(j)] = [(i,index)]
        game.append(A)

    Max_count = 0
    for x in range(N):
        for y in range(N):
            if game[x][y] == 0:
                #print(x,y)
                for dir in direction:
                    result = start((x,y),dir,game,N)
                    if result > Max_count:
                        Max_count = result
    print('#'+str(test),end=' ')
    print(Max_count)
