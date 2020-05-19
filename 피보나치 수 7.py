import sys
sys.setrecursionlimit(100000)
sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())

memo = [-1 for i in range(n+1)]
pivo_0 = 0
pivo_1 = 1
memo[0] = 0
memo[1] = 1

def pivo(n):

    if n == 0:
        return memo[0]
    elif n == 1:
        return memo[1]
    else:
        if memo[n-1] != -1:
            pivo_n_1 = memo[n-1]
        else:
            pivo_n_1 = pivo(n-1)

        if memo[n-2] != -1:
            pivo_n_2 = memo[n-2]
        else:
            pivo_n_2 = pivo(n-2)

        pivo_n = pivo_n_1 + pivo_n_2
        memo[n] = pivo_n

        return pivo_n

print(pivo(n)%1000000007)

