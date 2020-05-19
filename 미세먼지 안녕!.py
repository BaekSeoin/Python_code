import sys

sys.stdin = open("input.txt","r")

R,C,T = tuple(map(int, sys.stdin.readline().rstrip().split()))

house = [[[int(i)] for i in sys.stdin.readline().rstrip().split()] for j in range(R)]

dust = []
direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if 0<=a<R and 0<=b<C:
        return True
    return False

for i in range(R):
    if house[i][0][0] == -1:
        dust.append((i,0))
        if len(dust) == 2:
            break

def DUST(house):
    move = []
    for i in range(R):
        for j in range(C):
            if house[i][j][0] != 0 and house[i][j][0] != -1:
                move.append((i,j))

    for k in move:
        count = 0
        point = house[k[0]][k[1]][0]
        for n in direction:
            nextPos = (k[0] + n[0], k[1]+n[1])
            if inRange(nextPos[0],nextPos[1]) and (nextPos not in dust):
                count +=1
                house[nextPos[0]][nextPos[1]].append(point//5)
        house[k[0]][k[1]][0] = point - (point//5) * count

    for i in range(R):
        for j in range(C):
            Sum = sum(house[i][j])
            house[i][j] = [Sum]

def WIND(house):
    first = dust[0]
    # 위쪽 공기청정기
    for i in range(first[0]-1,-1,-1):
        a = house[i][0]
        if i+1 != first[0]:
            house[i+1][0] = a
    for j in range(C):
        a = house[0][j]
        if j == 0:
            house[1][0] = a
        else:
            house[0][j-1] = a
    for i in range(first[0]+1):
        a = house[i][C-1]
        if i == 0:
            house[0][C-2] = a
        else:
            house[i-1][C-1] = a
    for j in range(C-1,0,-1):
        a = house[first[0]][j]
        if j == C-1:
            house[first[0]-1][C-1] = a
        else:
            house[first[0]][j+1] = a

    second = dust[1]
    # 아래쪽 공기청정기
    for i in range(second[0]+1,R):
        a = house[i][0]
        if i-1 != second[0]:
            house[i-1][0] = a
    for j in range(C):
        a = house[R-1][j]
        if j == 0:
            house[R-2][0] = a
        else:
            house[R-1][j-1] = a
    for i in range(R-1,second[0]-1,-1):
        a = house[i][C-1]
        if i == R-1:
            house[R-1][C-2] = a
        else:
            house[i+1][C-1] = a
    for j in range(C-1,0,-1):
        a = house[second[0]][j]
        if j == C-1:
            house[second[0]+1][j] = a
        else:
            house[second[0]][j+1] = a
    house[first[0]][1] = [0]
    house[second[0]][1] = [0]

for t in range(T):
    DUST(house)
    #print(house)
    WIND(house)
    #print(house)

result = 2
for i in range(R):
    for j in range(C):
        result += house[i][j][0]

print(result)