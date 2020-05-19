import sys
import heapq

sys.stdin = open("input.txt","r")

T = int(input())

for i in range(T):
    N = int(input())
    name = []
    check = dict()

    for j in range(N):
        a = input().rstrip()
        try:
            if check[a] == True:
                continue
        except:
            heapq.heappush(name,(len(a),a))
            check[a] = True
    print('#'+str(i+1))
    while name:
        A = heapq.heappop(name)
        print(A[1])
