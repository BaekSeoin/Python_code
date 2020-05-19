import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

drink = [int(sys.stdin.readline().rstrip()) for i in range(n)]

count0 = [(0,0)]
count1 = [(1,drink[0])]
count2 = [(2,-1)]

def dp(index):
    Max_0 = []
    Max_1 = []
    Max_2 = []

    #count ==0
    prev_0 = count0[index-1]
    Max_0.append(prev_0)
    add = (prev_0[0] + 1, prev_0[1] + drink[index])
    Max_1.append(add)

    #count ==1
    prev_1 = count1[index-1]
    Max_0.append((0, prev_1[1]))
    add = (prev_1[0] + 1, prev_1[1] + drink[index])
    Max_2.append(add)

    #count ==2
    prev_2 = count2[index-1]
    if prev_2 != (2,-1):
        add = (0,prev_2[1])
        Max_0.append(add)
    Max_0 = sorted(Max_0, key=lambda x: x[1], reverse=True)
    Max_1 = sorted(Max_1, key=lambda x: x[1], reverse=True)
    Max_2 = sorted(Max_2, key=lambda x: x[1], reverse=True)

    count0.append(Max_0[0])
    count1.append(Max_1[0])
    count2.append(Max_2[0])

for i in range(1,n):
    dp(i)

print(max(count0[-1][1],count1[-1][1], count2[-1][1]))