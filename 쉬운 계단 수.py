import sys

sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline().rstrip())

store = [[0 for j in range(10)] for i in range(N+1)]

for j in range(1,10):
    store[1][j] = 1

def make(n):

    for j in range(10):
        if j ==9:
            cur = store[n - 1][j - 1] % 1000000000
        elif j == 0:
            cur = store[n-1][j+1] % 1000000000
        else:
            cur = store[n - 1][j - 1]%1000000000 + store[n - 1][j + 1]%1000000000

        store[n][j] = cur

for n in range(2,N+1):
    make(n)
ans = 0
for i in range(10):
    ans = (ans + store[N][i]) % 1000000000

print(ans)