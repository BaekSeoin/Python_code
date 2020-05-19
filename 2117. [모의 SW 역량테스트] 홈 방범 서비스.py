import sys
sys.stdin = open("input.txt","r")

T = int(input())

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if 0 <= a < n and 0 <= b < n:
        return True
    return False

for i in range(T):
    n, cost_per_house = tuple(map(int, input().rstrip().split()))
    town = [[int(j) for j in input().rstrip().split()] for h in range(n)]
    Max_house = 0

    board = [(0,0)]
    for q in range(1,n+2):
        if q != 1:
            a = len(board)
            for u in range(a):
                pos = board[u]
                for y in direction:
                    nextPos = (pos[0] + y[0], pos[1] + y[1])
                    if nextPos not in board:
                        board.append(nextPos)
        operating_cost = q**2 + (q-1)**2

        for e in range(n):
            for w in range(n):
                count = 0
                for p in board:
                    current = (p[0] + e, p[1] + w)
                    if inRange(current[0],current[1]) and town[current[0]][current[1]] == 1:
                        count += 1
                profit = cost_per_house * count - operating_cost
                if profit >= 0 and count > Max_house:
                    Max_house = count

                if Max_house == operating_cost:
                    break
            if Max_house == operating_cost:
                break

    print('#', end = '')
    print(i+1, end = ' ')
    print(Max_house)