import sys

sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())

work = [None]
for i in range(n):
    a,b = tuple(map(int, sys.stdin.readline().rstrip().split()))
    work.append((a,b))

List = [-1 for i in range(n+1)]

def dfs(day):
    if day > n:
        return 0

    if List[day] != -1:
        return List[day]

    current = work[day]
    Ti = current[0]
    Pi = current[1]

    if day+Ti <= n+1:
        R1 = dfs(day+Ti) + Pi
    else:
        R1 = 0

    R2 = dfs(day+1)

    R3 = max(R1,R2)

    List[day] = R3
    return R3

print(dfs(1))
