import sys

sys.stdin = open("input.txt", "r")

#문제 수, 문제 난이도의 최대값, 문제 난이도의 최저값, 가장 어려운 문제의 난이도와 쉬운 문제의 난이도의
N, L, R, X = tuple(map(int,sys.stdin.readline().rstrip().split()))

problem = [int(i) for i in sys.stdin.readline().rstrip().split()]
count = 0

def check(List):
    Sum = sum(List)
    Max = max(List)
    Min = min(List)
    if L<=Sum<=R and (Max - Min) >=X:
        return True
    return False

def dfs(index,List):
    global count
    if len(List) >=2:
        if check(List):
            count +=1

    for i in range(index+1,N):
        difficulty = problem[i]
        List.append(difficulty)
        dfs(i, List)
        List.pop()

List = []
dfs(-1,List)
print(count)