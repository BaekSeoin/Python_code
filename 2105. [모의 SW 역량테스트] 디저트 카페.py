import sys

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

#direction = [(-1,-1),(-1,1),(1,1),(1,-1)]
dir_change = {(-1,-1):[(-1,-1),(-1,1)],(-1,1):[(-1,1),(1,1)],(1,1):[(1,1),(1,-1)],(1,-1):[(1,-1),(-1,-1)]}

def inRange(a,b):
    if 0<=a<N and 0<=b<N:
        return True
    return False

def dessert(start,current,List,count,dir):
    global Max_sum
    if count == 4 and current == start:
        S = sum(List)
        if S > Max_sum:
            Max_sum = S
        return

    for d in dir_change[dir]:
        nextPos = (current[0] + dir[0], current[1] + dir[1])
        if inRange(nextPos[0], nextPos[1]) and List[board[nextPos[0]][nextPos[1]]] ==0:
            num = board[nextPos[0]][nextPos[1]]
            if d != dir and count <4:
                count +=1
            elif d != dir and count ==4:
                continue
            List[num] = 1
            dessert(start,nextPos,List,count,d)
            List[num] = 0
            if d != dir and count <4:
                count -=1

for test in range(1,T+1):
    N = int(input().rstrip())
    board = [[int(i) for i in input().rstrip().split()] for j in range(N)]
    Max_sum = 0

    for i in range(N):
        for j in range(N):
            current = (i,j)
            for dir in dir_change:
                List = [0 for u in range(101)]
                dessert(current,current,List,1,dir)
    print('#' +str(test),end=' ')
    if Max_sum > 0:
        print(Max_sum)
    else:
        print(-1)