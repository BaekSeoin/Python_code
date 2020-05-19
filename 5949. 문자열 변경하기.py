import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def bfs(List):
    end = -1
    while List:
        x = List.popleft()
        current = x[0]
        count=x[1]
        prev_change = x[2]
        for i in range(len(S)-1):
            if i == prev_change:
                continue
            prev = current[:i]
            cur1 = current[i]
            cur2 = current[i+1]
            next = current[i+2:]
            if cur1 == cur2 or cur1 == W[i]:
                continue
            word = prev + cur2 + cur1 + next
            if word==W:
                end = count + 1
                break
            try:
                y = check[word]
            except:
                check[word] = True
                List.append((word,count+1,i))
        if end != -1:
            break
    return end

T = int(input().rstrip())

for test in range(1,T+1):
    S = input().rstrip()
    W = input().rstrip()
    print('#' + str(test), end=' ')
    if S == W:
        print(0)
        continue
    check = dict()
    check[S] = True
    List = deque()
    List.append((S,0,-1))
    ans = str(bfs(List))
    print(ans)