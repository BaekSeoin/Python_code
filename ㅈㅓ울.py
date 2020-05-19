from collections import deque


def solution(weight):
    global length, stop, weight2, check

    length = len(weight)
    weight2 = sorted(weight)

    List = deque()
    List.append(0)

    num = 1
    for n in weight2:
        k = len(List)
        List.append(n)
        for i in range(k):
            x = List.popleft()
            y = n + x
            if y == num:
                num += 1
                List.append(y)
            else:
                return num


weight = [1, 1, 1, 1, 1, 1, 1]

print(solution(weight))