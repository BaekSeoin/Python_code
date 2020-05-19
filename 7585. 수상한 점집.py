import sys

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

def find(A,B,N,K):
    count = 0

    a = []
    b = []

    for i in range(1,K+1):
        x = i ** A % K
        y = i ** B % K
        if x not in a:
            a.append(x)
        if y not in b:
            b.append(y)

    for i in range(N):
        for j in range(N):
            if i != j:
                i_change = i % K
                j_change = j % K
                ans = (a[i_change] + b[j_change]) % K
                if ans == 0:
                    count +=1

    return count % 1000000007


for test in range(1,T+1):
    A,B,N,K = tuple(map(int,input().rstrip().split()))
    print('#' + str(test),end=' ')
    print(find(A,B,N,K))