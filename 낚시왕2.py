import sys

sys.stdin = open("input.txt", "r")

R,C,M = tuple(map(int, sys.stdin.readline().rstrip().split()))

ocean = dict()

for i in range(R):
    for j in range(C):
        ocean[(i,j)] = []

direction = {1:(-1,0),2:(1,0),3:(0,1),4:(0,-1)}
dir_change = {1:2,2:1,3:4,4:3}

def inRange(a,b):
    if 0<=a <R and 0<=b<C:
        return True
    return False

def move(ocean):
    new_ocean = dict()
    for i in range(R):
        for j in range(C):
            new_ocean[(i, j)] = []
    for key, value in ocean.items():
        if len(value) == 0:
            continue
        current = value[0]
        currentPos = key
        dir = current[1]
        d = direction[dir]
        for speed in range(current[0]):
            currentPos = (currentPos[0]+d[0],currentPos[1] + d[1])
            if not inRange(currentPos[0],currentPos[1]):
                currentPos = (currentPos[0]-d[0],currentPos[1] - d[1])
                dir = dir_change[dir]
                d = direction[dir]
                currentPos = (currentPos[0] + d[0], currentPos[1] + d[1])
        new_ocean[currentPos].append((current[0],dir,current[2]))
    return new_ocean

def remove(ocean):
    for key, value in ocean.items():
        if len(value) > 1:
            Max_size =0
            for shark in value:
                if shark[2] > Max_size:
                    Max_size = shark[2]
                    Max_shark= shark
            ocean[key] = [Max_shark]

for i in range(M):
    r,c,speed, dir, size = tuple(map(int, sys.stdin.readline().rstrip().split()))
    ocean[(r-1,c-1)].append((speed,dir,size))

point = 0
for col in range(C):
    for row in range(R):
        current = ocean[(row,col)]
        if len(current) > 0:
            point += current[0][2]
            ocean[(row,col)] = []
            break
    ocean = move(ocean)
    remove(ocean)
print(point)