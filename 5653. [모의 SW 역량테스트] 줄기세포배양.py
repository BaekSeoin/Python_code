import sys

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

#상/하/좌/우
direction = [(-1,0),(1,0),(0,-1),(0,1)]

def change(spread):
    new = dict()
    for key, value in spread.items():
        if value[0] !=2:
            if value[1] > value[2]+1:
                new[key] = [value[0], value[1], value[2]+1]
            elif value[1] == value[2]+1:
                new[key] = [value[0] + 1, value[1], 0]
            if value[0] == 1:
                for dir in direction:
                    nextPos = (key[0]+dir[0], key[1] + dir[1])
                    try:
                        b = die[nextPos]
                    except:
                        try:
                            a = spread[nextPos]
                        except:
                            try:
                                new[nextPos].append([0, value[1], 0])
                            except:
                                new[nextPos] = []
                                new[nextPos].append([0,value[1],0])
        if value[0] == 2:
            die[key] = 1

    for k,v in new.items():
        try:
            a = spread[k]
        except:
            mx = 0
            for c in v:
                #print(v)
                if c[1] >mx:
                    mx = c[1]
            new[k] = [0,mx,0]
    return new

for test in range(1,T+1):
    N,M,K = tuple(map(int,input().rstrip().split()))
    spread = dict()
    for i in range(N):
        for j,cell in enumerate(input().rstrip().split()):
            #비활성/활성/죽음(0,1,2) & cell 시간 & 현재 상태 지속 시간
            if int(cell) !=0:
                spread[(i,j)] = [0,int(cell),0]
    die = dict()

    for time in range(K):
        spread = change(spread)
    count = 0
    for key, value in spread.items():
        if value[0] !=2:
            count +=1
    print('#'+str(test),end = ' ')
    print(count)