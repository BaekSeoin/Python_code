import sys

sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())
stairs = []
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    stairs.append(a)

#안밟음/밟음
List = [[0,0] for i in range(n)]

List[0][1] = stairs[0]
List[1][0] = stairs[0]
List[1][1] = stairs[0] + stairs[1]

def dp(index):
    List[index][0] = List[index-1][1]
    List[index][1] = max(List[index-2][0]+stairs[index-1] + stairs[index], List[index-2][1]+stairs[index])

for j in range(2,n):
    dp(j)
print(List[-1][1])