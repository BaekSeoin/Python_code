import sys
import copy

sys.stdin = open("input.txt", "r")

N,M,K = tuple(map(int,sys.stdin.readline().rstrip().split()))

A = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

info = []

for i in range(K):
    r,c,s = sys.stdin.readline().rstrip().split()
    info.append([int(r)-1,int(c)-1,int(s)])

def check_row(A):
    min_ans = 100*M
    for row in range(N):
        ans = 0
        for col in range(M):
            ans += A[row][col]
        if ans < min_ans:
            min_ans = ans
    return min_ans

def turn(A,r,c,s):
    first = []
    second = []
    third = []
    fourth = []

    for j in range(c-s,c+s+1):
        first.append(A[r-s][j])
    for i in range(r-s,r+s+1):
        second.append(A[i][c+s])
    for j in range(c-s,c+s+1):
        third.append(A[r+s][j])
    for i in range(r-s,r+s+1):
        fourth.append(A[i][c-s])

    for num, j in zip(first[:-1],range(c-s+1,c+s+1)):
        A[r-s][j] = num
    for num, i in zip(second[:-1],range(r-s+1,r+s+1)):
        A[i][c+s] = num
    for num, j in zip(third[1:],range(c-s,c+s)):
        A[r+s][j] = num
    for num,i in zip(fourth[1:],range(r-s,r+s)):
        A[i][c-s] = num

LEN = len(info)

order = []

List = []
def dfs(List):
    if len(List) == LEN:
        order.append(copy.deepcopy(List))
        return

    for i in range(LEN):
        if i not in List:
            List.append(i)
            dfs(List)
            List.pop()
dfs(List)

Min_Ans = 100*M
for x in order:
    A_2 = copy.deepcopy(A)
    for y in x:
        current = info[y]
        for z in range(1,current[2]+1):
            turn(A_2,current[0],current[1],z)
    ans = check_row(A_2)
    if ans < Min_Ans:
        Min_Ans = ans

print(Min_Ans)