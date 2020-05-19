import sys
from collections import deque

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())


final = [[' ' for i in range(2*N-1)] for j in range(N)]

cur = [[' ',' ','*',' ',' '],[' ','*',' ','*',' '],['*','*','*','*','*']]

List = deque()

def make(x,y):
    for i in range(3):
        for j in range(5):
            final[x+i][y+j] = cur[i][j]
            if (i ==0) and (j == 2):
                List.append((x+i,y+j))

for i in range(0,2*N-1,6):
    make(N-3,i)

if N != 3:
    while True:
        a = List.popleft()
        b = List.popleft()

        for i in range(a[1]+1,b[1],6):
            make(a[0]-3,i)

        if len(List) ==1:
            break


for i in range(N):
    ans = "".join(final[i])
    print(ans)
