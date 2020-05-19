import sys

sys.stdin = open("input.txt", "r")

N,M = tuple(map(int,sys.stdin.readline().rstrip().split()))

def inRange(a,b):
    if 0<=a<N and 0<=b<M:
        return True
    return False

check = [[(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,0),(2,0),(3,0)],
         [(0,0),(0,1),(1,0),(1,1)],
         [(0,0),(1,0),(2,0),(2,1)],[(0,0),(0,1),(0,2),(-1,2)],[(0,0),(-1,0),(-2,0),(-2,-1)],[(0,0),(0,-1),(0,-2),(1,-2)],
         [(0,0),(1,0),(1,1),(2,1)],[(0,0),(0,1),(-1,1),(-1,2)],[(0,0),(-1,0),(-1,-1),(-2,-1)],[(0,0),(0,-1),(1,-1),(1,-2)],
         [(0,0),(0,1),(0,2),(1,1)],[(0,0),(-1,0),(-2,0),(-1,1)],[(0,0),(0,-1),(0,-2),(-1,-1)],[(0,0),(1,0),(2,0),(1,-1)],
         [(0,0),(1,0),(2,0),(2,-1)],[(0,0),(0,1),(0,2),(1,2)],[(0,0),(-1,0),(-2,0),(-2,1)],[(0,0),(0,-1),(0,-2),(-1,-2)],
         [(0,0),(1,0),(1,-1),(2,-1)],[(0,0),(0,-1),(-1,-1),(-1,-2)],[(0,0),(-1,0),(-1,1),(-2,1)],[(0,0),(1,0),(1,1),(1,2)]]

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

def function(row,col):
    max_ans = 0
    for form in check:
        ans = 0
        end = 0
        for dir in form:
            nextPos = (row + dir[0],col+dir[1])
            if inRange(nextPos[0],nextPos[1]):
                ans += board[nextPos[0]][nextPos[1]]
            else:
                end = 1
                break
        if end == 1:
            continue
        if ans > max_ans:
            max_ans = ans
    return max_ans

final_max_ans = 0

for row in range(N):
    for col in range(M):
        ans= function(row,col)
        if ans > final_max_ans:
            final_max_ans = ans
print(final_max_ans)
