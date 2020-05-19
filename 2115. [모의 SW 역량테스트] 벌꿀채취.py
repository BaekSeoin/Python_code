import sys
from collections import deque

sys.stdin = open('input.txt','r')

T = int(input())
direction = [(0,1)]

def inRange(a,b):
    if 0<=a<n and 0<=b<n:
        return True
    return False

def make():
    for i in range(n):
        begin = 0
        for j in range(m-1,n):
            end = (i, j)
            if inRange(end[0], end[1]):
                a = [(i,k) for k in range(begin,j+1)]
                check.append(a)
                begin += 1

def move(current):
    Return = []

    for i in check:
        final_count = []
        if i != current and current[-1] not in i:
            a = []
            b = []
            count_a = 0
            count_b = 0

            for j in current:
                if board[j[0]][j[1]] <= c:
                    a.append(board[j[0]][j[1]])
            a.sort(reverse=T)
            for index,k in enumerate(a):
                if len(a) >=3 and index == 0 and k + a[index+1] > c and k + a[index+2] > c:
                    s = k ** 2
                    t = a[index+1] **2 + a[index+2] **2
                    if a[index+1] + a[index+2] <= c and t > s:
                        final_count.append(a[index+1])
                        final_count.append(a[index+2])
                        break
                    elif count_a + k <= c:
                        count_a += k
                        final_count.append(k)
                elif count_a + k <= c:
                    count_a += k
                    final_count.append(k)
            for h in i:
                if board[h[0]][h[1]] <= c:
                    b.append(board[h[0]][h[1]])
            b.sort(reverse=T)
            for index,q in enumerate(b):
                if len(b) >= 3 and index == 0 and q + b[index+1] > c and q + b[index+2] > c:
                    s = q ** 2
                    t = b[index+1] **2 + b[index+2] **2
                    if b[index+1] + b[index+2] <= c and t > s:
                        final_count.append(b[index+1])
                        final_count.append(b[index+2])
                        break
                    elif count_b + q <= c:
                        count_b += q
                        final_count.append(q)
                elif count_b + q <= c:
                    count_b += q
                    final_count.append(q)
        return_value = 0
        for p in final_count:
            return_value += p**2
        Return.append(return_value)
    return Return

for i in range(1,T+1):

    n, m, c = tuple(map(int, input().rstrip().split()))
    board = [[int(j) for j in input().rstrip().split()] for k in range(n)]
    check = deque()
    make()
    final = []
    Len = len(check)

    for w in range(Len):
        current = check[0]
        Return = move(current)
        check.popleft()
        for o in Return:
            final.append(o)
    print('#',end='')
    print(i, end= ' ')
    print(max(final))