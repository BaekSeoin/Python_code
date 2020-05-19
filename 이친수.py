import sys

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())

memo = [0 for i in range(N+1)]

if N <2:
    memo[1] = 1
else:
    memo[1] = 1
    memo[2] = 1

def find(N):
    if memo[N] !=0:
        return memo[N]
    else:
        ans = find(N-1) + find(N-2)
        memo[N] = ans
        return ans

print(find(N))