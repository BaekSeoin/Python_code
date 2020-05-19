import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

List = [int(i) for i in sys.stdin.readline().rstrip().split()]

check = [None for i in range(n)]

def f(n):
    if check[n] != None:
        return check[n]
    else:
        ans = max(f(n+1) + List[n],List[n])
        check[n] = ans
        return check[n]

check[n-1] = List[n-1]

for j in range(n-1,-1,-1):
    f(j)

print(max(check))