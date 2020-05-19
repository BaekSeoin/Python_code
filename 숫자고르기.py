import sys
import heapq

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

List = []

for i in range(N):
    a = int(sys.stdin.readline().rstrip())
    List.append(a)

num = len(set(List))

def check(top_list, bottom_list):
    global count, final_list
    a = set(top_list)
    b = set(bottom_list)

    if a == b:
        if count < len(a):
            count = len(a)
            final_list = []
            for i in a:
                heapq.heappush(final_list, i)

def dfs(top_list,bottom_list ,n):
    global count, num

    if (n == N) or (count == num):
        return

    if len(top_list) != 0:
        check(top_list, bottom_list)

    if (n+1) in List:
        top_list.append(n+1)
        bottom_list.append(List[n])
        dfs(top_list,bottom_list,n+1)
        top_list.pop()
        bottom_list.pop()

    dfs(top_list, bottom_list, n+1)

count = 0
top_list = []
bottom_list = []
final_list = []
dfs(top_list, bottom_list,0)
print(count)

for i in range(count):
    print(heapq.heappop(final_list))