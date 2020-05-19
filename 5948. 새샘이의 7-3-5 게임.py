import sys
sys.stdin = open("input.txt","r")

T = int(input())

def dfs(i,List,Sum):
    if len(List) == 3:
        Sum.add(sum(List))
        return

    for j in range(i,7):
        a = number[j]
        List.append(a)
        dfs(j+1, List, Sum)
        List.pop()

for i in range(T):
    number = [int(j) for j in input().split()]
    Sum = set()
    List = []

    for k in range(6):
        dfs(k,List,Sum)
    result = []
    for w in Sum:
        result.append(w)
    result.sort(reverse=True)
    print('#',end='')
    print(i+1,end=' ')
    print(result[4])