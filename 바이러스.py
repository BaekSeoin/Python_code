import sys

sys.stdin = open('input.txt','r')

numOfComputer = int(sys.stdin.readline().rstrip())

numOfNetwork = int(sys.stdin.readline().rstrip())

network = dict()

for i in range(1,numOfComputer+1):
    network[i] = []

for i in range(numOfNetwork):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    network[a].append(b)
    network[b].append(a)

visit = [0 for i in range(numOfComputer+1)]

def dfs(curComputer):

    visit[curComputer] = 1
    nextComputers = network[curComputer]

    for nextComputer in nextComputers:
        if visit[nextComputer] == 0:
            dfs(nextComputer)

dfs(1)

print(sum(visit)-1)