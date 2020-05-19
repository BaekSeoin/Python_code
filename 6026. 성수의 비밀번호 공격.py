import sys

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

def function_P(a,b):
    ans = 1
    for i in range(a,b-1,-1):
        ans *=i
    return ans

for test in range(1,T+1):
    M,N = tuple(map(int,input().rstrip().split()))
    case = function_P(N-M,M)
    print(case)

