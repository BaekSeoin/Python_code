import sys

sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())

memo = [-1 for i in range(n+1)]

if n != 0:
    memo[0] = 0
    memo[1] = 1
else:
    memo[0] =0


def Pivo(n):

    if memo[n-1] != -1:
        A = memo[n-1]
    else:
        A = Pivo[n-1]
    if memo[n-2] != -1:
        B = memo[n-2]
    else:
        B = Pivo[n-2]

    R = (A + B) % 1000000007

    memo[n] = R

    return R

for i in range(2,n+1):
    Pivo(i)

ans = memo[-1]
print(ans)