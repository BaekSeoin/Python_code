def dfs(start, end, idx, routes):
    global answer

    if idx == len(routes):
        return

    cur = routes[idx]

    if cur[0] <= end:
        nextStart = max(start, cur[0])
        nextEnd = min(end, cur[1])
        dfs(nextStart, nextEnd, idx+1, routes)
    else:
        answer+=1
        dfs(cur[0], cur[1], idx + 1, routes)


def solution(routes):
    global answer
    answer = 0
    routes.sort()

    cur = routes[0]
    start = cur[0]
    end = cur[1]
    answer += 1
    dfs(start, end, 1, routes)

    return answer



routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))