import sys

sys.setrecursionlimit(1500)

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())
A = [int(i) for i in sys.stdin.readline().rstrip().split()]
memo = [-1 for i in range(N)]
last = len(A)

def f(n):
    number = A[n]

    MAX = 0
    for j in range(n+1,last):
        if memo[j] != -1:
            ans = memo[j]
        else:
            ans = f(j)

        if A[j] > number and ans > MAX:
            MAX = ans

    memo[n] = MAX + 1

    return MAX + 1

f(0)

print(max(memo))


