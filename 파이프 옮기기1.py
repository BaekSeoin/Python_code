import sys

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

END = (N-1,N-1)

def inRange(a,b):
    if 0<=a<N and 0<=b<N:
        return True
    return False

def board_check(next2):
    if board[next2[0]][next2[1]] == 0:
        return True
    return False

count = 0

# 방향/ 위치
board2 = {(1,0,0):0,(2,0,0):0,(3,0,0):0,(1,0,1):1,(2,0,1):0,(3,0,1):0}

def dp(current):
    try:
        ans = board2[current]
        return ans
    except:
        if board[current[1]][current[2]] == 1:
            board2[current] = 0
            return 0
        prev1 = (current[1],current[2]-1)#가로
        prev2 = (current[1]-1,current[2])#세로
        prev3 = (current[1]-1,current[2]-1)#대각선
        new1 = 0
        new2 = 0
        new3 = 0
        ans = 0
        if inRange(prev1[0],prev1[1]):
            new1 = (prev1[0],prev1[1])
        if inRange(prev2[0],prev2[1]):
            new2 = (prev2[0],prev2[1])
        if inRange(prev3[0],prev3[1]) and board_check(prev1) and board_check(prev2):
            new3 = (prev3[0],prev3[1])

        if current[0] == 1:
            if new1 != 0:
                ans += dp((1,new1[0],new1[1]))
                ans += dp((3, new1[0], new1[1]))

        elif current[0] ==2:
            if new2 !=0:
                ans += dp((2, new2[0], new2[1]))
                ans += dp((3, new2[0], new2[1]))
        else:
            if new3!=0:
                ans += dp((1, new3[0], new3[1]))
                ans += dp((2, new3[0], new3[1]))
                ans += dp((3, new3[0], new3[1]))

        board2[current] = ans
        return ans

ans =0
ans +=dp((1,N-1,N-1))
ans +=dp((2,N-1,N-1))
ans +=dp((3,N-1,N-1))

print(ans)
