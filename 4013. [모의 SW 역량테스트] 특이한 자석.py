import sys
from collections import deque

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

for test in range(1,T+1):
    K = int(input().rstrip())
    first = deque(int(i) for i in input().rstrip().split())
    second = deque(int(i) for i in input().rstrip().split())
    third = deque(int(i) for i in input().rstrip().split())
    fourth = deque(int(i) for i in input().rstrip().split())

    info = []
    for k in range(K):
        a,b = tuple(map(int, input().rstrip().split()))
        info.append((a,b))

    for i in info:
        if i[0] == 1:
            if i[1] == 1:
                if first[2] != second[6]:
                    if second[2] != third[6]:
                        if third[2] != fourth[6]:
                            q = fourth.popleft()
                            fourth.append(q)
                        z = third.pop()
                        third.appendleft(z)
                    y = second.popleft()
                    second.append(y)
                x = first.pop()
                first.appendleft(x)

            else:
                if first[2] != second[6]:
                    if second[2] != third[6]:
                        if third[2] != fourth[6]:
                            q = fourth.pop()
                            fourth.appendleft(q)
                        z = third.popleft()
                        third.append(z)
                    y = second.pop()
                    second.appendleft(y)
                x = first.popleft()
                first.append(x)
        if i[0] == 2:
            if i[1] == 1:
                if second[6] != first[2]:
                    x = first.popleft()
                    first.append(x)
                if second[2] != third[6]:
                    if third[2] != fourth[6]:
                        q = fourth.pop()
                        fourth.appendleft(q)
                    z = third.popleft()
                    third.append(z)
                y = second.pop()
                second.appendleft(y)
            if i[1] == -1:
                if second[6] != first[2]:
                    x = first.pop()
                    first.appendleft(x)
                if second[2] != third[6]:
                    if third[2] != fourth[6]:
                        q = fourth.popleft()
                        fourth.append(q)
                    z = third.pop()
                    third.appendleft(z)
                y = second.popleft()
                second.append(y)

        if i[0] == 3:
            if i[1] == 1:
                if third[2] != fourth[6]:
                    x = fourth.popleft()
                    fourth.append(x)
                if third[6] != second[2]:
                    if second[6] != first[2]:
                        q = first.pop()
                        first.appendleft(q)
                    z = second.popleft()
                    second.append(z)
                y = third.pop()
                third.appendleft(y)

            if i[1] == -1:
                if third[2] != fourth[6]:
                    x = fourth.pop()
                    fourth.appendleft(x)
                if third[6] != second[2]:
                    if second[6] != first[2]:
                        q = first.popleft()
                        first.append(q)
                    z = second.pop()
                    second.appendleft(z)
                y = third.popleft()
                third.append(y)

        if i[0] == 4:
            if i[1] == 1:
                if fourth[6] != third[2]:
                    if third[6] != second[2]:
                        if second[6] != first[2]:
                            q = first.popleft()
                            first.append(q)
                        z = second.pop()
                        second.appendleft(z)
                    y = third.popleft()
                    third.append(y)
                x = fourth.pop()
                fourth.appendleft(x)

            else:
                if fourth[6] != third[2]:
                    if third[6] != second[2]:
                        if second[6] != first[2]:
                            q = first.pop()
                            first.appendleft(q)
                        z = second.popleft()
                        second.append(z)
                    y = third.pop()
                    third.appendleft(y)
                x = fourth.popleft()
                fourth.append(x)

    Total = 0
    if first[0] == 1:
        Total +=1
    if second[0] == 1:
        Total +=2
    if third[0] == 1:
        Total +=4
    if fourth[0] == 1:
        Total +=8
    print('#' + str(test),end=' ')
    print(Total)