import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

final = [[' ' for i in range(N)] for j in range(N)]


def recursive(n,x,y):
    if n == 3:
        for i in range(x,x+3):
            for j in range(y,y+3):
                if (i == x+1) and (j == y+1):
                    continue
                final[i][j] = '*'
        return

    next_n = int(n / 3)
    for k in range(x,x+n,next_n):
        for v in range(y,y+n,next_n):
            if (k == x+next_n) and (v == y+next_n):
                continue
            recursive(next_n,k,v)


recursive(N,0,0)

for i in range(N):
    for j in range(N):
        print(final[i][j],end='')
    print()