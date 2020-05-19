import sys

sys.stdin = open('input.txt','r')

N,M = map(int, sys.stdin.readline().rstrip().split())

number = [int(i) for i in sys.stdin.readline().rstrip().split()]

max_num = 0
def dfs(index,ans,count):
    global max_num

    if count == 3:
        if (ans <= M) and (ans > max_num):
            max_num = ans
        return

    if index >= len(number):
        return

    cur = number[index]
    ans += cur
    dfs(index+1, ans, count+1)
    ans -= cur
    dfs(index+1, ans, count)

dfs(0, 0, 0)
print(max_num)