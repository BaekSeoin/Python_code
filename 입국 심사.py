def binaySearch(left, right, times, n):
    cnt = 0
    answer = -1

    while left <= right:
        mid = int((left+right)/2)
        cnt = 0
        for time in times:
            cnt += int(mid/time) #각 심사관이 몇 명을 처리할 수 있는지 확인

        if cnt >= n:
            if answer == -1:
                answer = mid
            else:
                answer = min(answer, mid)
            right = mid-1
        elif cnt < n: left = mid+1

    return answer


def solution(n, times):
    times.sort()
    left = 0
    right = times[-1] * n

    answer = binaySearch(left,right, times, n)

    return answer


n = 6
times = [7, 10]
print(solution(n,times))