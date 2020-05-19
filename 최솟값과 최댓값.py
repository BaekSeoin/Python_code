import heapq


def solution(jobs):
    answer = 0
    arr = []
    jobs.sort()
    for i in jobs:
        heapq.heappush(arr, (i[0], i[1]))

    cur_time = 0
    n = 0
    ans = 0
    while arr:
        n += 1
        cur = heapq.heappop(arr)
        cur_request = cur[0]
        cur_spend = cur[1]

        if cur_request >= cur_time:
            cur_time = cur_request + cur_spend
            ans += cur_spend
            print(cur_spend)
            arr2 = []

            while len(arr) > 0:
                x = heapq.heappop(arr)
                next_request = x[0]
                next_spend = x[1]

                if next_request < cur_time:
                    heapq.heappush(arr2, (next_spend, next_request))
                else:
                    heapq.heappush(arr, x)
                    break
            while arr2:
                n += 1
                cur1 = heapq.heappop(arr2)
                cur1_request = cur1[1]
                cur1_spend = cur1[0]

                if cur1_request >= cur_time:
                    cur_time = cur1_request + cur1_spend
                    ans += cur1_spend
                    print(cur1_spend)

                else:
                    cur_time += cur1_spend
                    ans += (cur_time - cur1_request)
                    print(cur_time - cur1_request)
        else:
            cur_time += cur_spend
            ans += (cur_time - cur_request)
            print(cur_time - cur_request)


    answer = int(ans / n)
    return answer

jobs = [[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]
print(solution(jobs))