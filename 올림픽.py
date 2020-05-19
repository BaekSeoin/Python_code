import sys

sys.stdin = open("input.txt","r")
a = [int(i) for i in sys.stdin.readline().rstrip().split()]
N = a[0]
K = a[1]
olympic = dict()

for j in range(N):
    Input = [int(i) for i in sys.stdin.readline().rstrip().split()]
    olympic[Input[0]] = Input[1:]

K_gold = olympic[K][0]
K_silver = olympic[K][1]
K_bronze = olympic[K][2]

rank = 1

def ranking(olympic,rank,N):
    for i in range(1,N+1):
        if olympic[i][0] > K_gold:
            rank +=1
        elif olympic[i][0] == K_gold:
            if olympic[i][1] > K_silver:
                rank += 1
            elif olympic[i][1] == K_silver:
                if olympic[i][2] > K_bronze:
                    rank +=1
    return rank

print(ranking(olympic,rank,N))



