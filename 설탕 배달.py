import sys

sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline().rstrip())

count = 0
sugar = [N,]
Min = 5000


def cal(N,i):
    global count

    if i == 0:
        N -= 5
        count += 1
        sugar.append(N)

    if i == 1:
        N -= 3
        sugar.append(N)
        count += 1

def dfs(N):
    global count, Min

    if count > Min:
        return

    if N == 0:
        Min = count
        return

    if N < 0:
        return

    for i in range(2):
        cal(sugar[-1],i)
        dfs(sugar[-1])
        sugar.pop()
        count -= 1


dfs(N)

if Min == 5000:
    print(-1)

else:
    print(Min)







