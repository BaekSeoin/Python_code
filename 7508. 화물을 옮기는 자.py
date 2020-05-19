import sys
sys.stdin = open("input.txt","r")

T = int(input())

for i in range(T):
    n = int(input())
    A = [int(k) for k in input().rstrip().split()]
    m = int(input())
    W = [int(k) for k in input().rstrip().split()]
    check = [0 for k in range(m)]

    A.sort()
    W.sort(reverse=True)
    count = 0
    length = len(W) // len(A)

    while True:
        if A[-1] < W[0]:
            print('#', end='')
            print(i + 1, end=' ')
            print(-1)
            break

        if count >= length and 0 not in check:
            print('#',end='')
            print(i+1, end=' ')
            print(count)
            break

        count += 1
        for q in A:
            for index,p in enumerate(W):
                if check[index] == 0 and q >= p:
                    check[index] = 1
                    break
