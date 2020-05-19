import sys
import numpy as np
from collections import deque

sys.stdin = open('input.txt','r')

T = int(sys.stdin.readline().rstrip())

arr = [True for i in range(10000)]

def check(num):
    for i in range(2,int(np.sqrt(num))+1):
        if (arr[i] == False): # 이미 체크된 수의 배수는 확인하지 않는다
            continue
        for j in range(i + i,num+1,i): #i를 제외한 i의 배수들은 0으로 체크
            arr[j] = False

check(9999)

def bfs(List):
    global b

    while List:
        num,count = List.popleft()

        for i in range(1,10):
            x = str(num)
            if x[0] != str(i):
                x = str(i) + x[1:]
                x = int(x)
                if arr[x] == False:
                    continue

                if x == b:
                    return (count + 1)

                try:
                    a = visit[x]
                except:
                    visit[x] = True
                    List.append((x,count+1))
        for j in range(1,4):
            for i in range(0, 10):
                x = str(num)
                if x[j] != str(i):
                    if j == 1:
                        x = x[0] + str(i) + x[2:]
                    elif j == 2:
                        x = x[:2] + str(i) + x[3]
                    else:
                        x = x[:3] + str(i)

                    x = int(x)
                    if arr[x] == False:
                        continue

                    if x == b:
                        return (count+1)

                    try:
                        a = visit[x]
                    except:
                        visit[x] = True
                        List.append((x,count+1))
    return -1


for t in range(T):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    visit = dict()
    visit[a] = True
    List = deque()
    List.append((a,0))

    if a != b:
        count = bfs(List)
    else:
        count = 0

    if count != -1:
        print(count)
    else:
        print("Impossible")
