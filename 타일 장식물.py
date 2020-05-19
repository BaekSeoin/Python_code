def dp(n):
    global memo
    if memo[n] != 0:
        return memo[n]

    x = dp(n - 2)
    y = dp(n - 1)
    ans = x + y
    memo[n] = ans

    return memo[n]


def solution(N):
    global memo
    memo = [0 for i in range(N + 1)]
    if N == 1:
        memo[1] = 4
    elif N > 1:
        memo[1] = 4
        memo[2] = 6
    answer = dp(N)

    return answer

N = 5
print(solution(N))