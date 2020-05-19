import sys

sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())
work = [None]
for i in range(n):
    a,b = tuple(map(int, sys.stdin.readline().rstrip().split()))
    work.append((a,b))

Max_profit = 0

def dfs(i,profit):
    global Max_profit,n
    if i <=n:
        current = work[i]
        day = current[0]
        pay = current[1]

        if (len(work) - i) < day:
            i +=1
            dfs(i,profit)
            i-=1
        else:
            for k in range(2):
                if k == 0:
                    i += day
                    profit +=pay
                    dfs(i,profit)
                    i -=day
                    profit -=pay
                else:
                    i += 1
                    dfs(i,profit)
                    i -= 1
    else:
        if profit > Max_profit:
            Max_profit = profit
        return
dfs(1,0)
print(Max_profit)