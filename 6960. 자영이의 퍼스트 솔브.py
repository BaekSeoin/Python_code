import sys

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

for test in range(1,T+1):
    N = int(input().rstrip())
    problem = dict()
    collect = []
    max_prob = 0
    total_time = 0
    time_pass = 0
    for i in range(N):
        s,f = tuple(map(int,input().rstrip().split()))
        if f < s:
            N-=1
            continue
        problem[f] = s
        collect.append(f)
        total_time += s
    collect = sorted(collect)
    while collect:
        current = collect.pop()
        if current > total_time:
            max_prob +=1
            total_time -= problem[current]
            time_pass += problem[current]
        else:
            if time_pass+ problem[current] <= total_time:
                max_prob+=1
                total_time -= problem[current]
                time_pass += problem[current]

    print('#'+str(test),end=' ')
    print(max_prob)
