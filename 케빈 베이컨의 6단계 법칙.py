import sys
sys.stdin = open("input.txt","r")

N, numOfcase = tuple(map(int, sys.stdin.readline().rstrip().split()))

friends = {}

for i in range(numOfcase):
    a,b = tuple(map(int, sys.stdin.readline().rstrip().split()))
    if a not in friends:
        friends[a] = [b]
    else:
        friends[a].append(b)
    if b not in friends:
        friends[b] = [a]
    else:
        friends[b].append(a)


def find_kebin(w,List,kebin_check):
    x = List.pop()
    a = x[0]
    dist = x[1]
    a_values = friends[a]

    for i in a_values:
        if w != i:
            if kebin_check[i] == 0 or kebin_check[i] > dist+1:
                List.append((i, dist+1))
                kebin_check[i] = dist+1
                find_kebin(w, List, kebin_check)

    return kebin_check

ans = 10000000000


for i in range(1,N+1):
    kebin_check = [0 for i in range(N+1)]
    dist = 0
    List = []
    List.append((i,dist))
    result = find_kebin(i, List, kebin_check)

    if sum(result) < ans:
        ans = sum(result)
        ans_people = i

print(ans_people)