import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

triangle = []
board = []
for i in range(n):
    layer = [int(j) for j in sys.stdin.readline().rstrip().split()]
    triangle.append(layer)
    List = []
    for num in range(i+1):
        List.append(-1)
    board.append(List)

board[0][0] = triangle[0][0]

def dp(depth,index):
    if board[depth][index] !=-1:
        return board[depth][index]

    ans = 0
    if index == 0:
        ans += dp(depth-1,index) + triangle[depth][index]
    elif index == depth:
        ans += dp(depth-1,index-1) + triangle[depth][index]
    else:
        ans += max(dp(depth-1,index-1),dp(depth-1,index)) + triangle[depth][index]

    board[depth][index] = ans
    return ans

for depth in range(n):
    for index in range(depth+1):
        dp(depth,index)

print(max(board[n-1]))
