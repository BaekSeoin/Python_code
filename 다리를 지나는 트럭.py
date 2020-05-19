from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    passing = [0 for i in range(bridge_length)]
    passing = deque(passing)
    waiting = deque(truck_weights)

    total_weight = 0
    while waiting:
        answer += 1
        x = passing.popleft()
        total_weight -= x

        if total_weight + waiting[0] <= weight:
            y = waiting.popleft()
            passing.append(y)
            total_weight += y
        else:
            passing.append(0)
    answer += len(passing)

    return answer


bridge_length =2
weight =10
truck_weights =[7,4,5,6]

print(solution(bridge_length, weight, truck_weights))