import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

card = [0]
for i in sys.stdin.readline().rstrip().split():
    card.append(int(i))

memo = [0 for i in range(N+1)]
memo[1] = card[1]

def dp(n):
    if memo[n] !=0:
        return memo[n]
    else:
        ans = 0
        for i in range(1,n//2+1):
            a = dp(i)
            b = dp(n-i)
            ans = max(ans,a+b)
        ans = max(ans,card[n])
        memo[n] = ans
        return memo[n]

print(dp(N))

