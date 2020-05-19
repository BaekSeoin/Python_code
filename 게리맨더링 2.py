import sys
import copy
sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

def pop_check(x,y,d1,d2):
    first = []
    second = []
    third = []
    fourth = []
    fifth = []
    check = dict()

    for i,j in zip(range(x,x+d1+1), range(y,y-d1-1,-1)):
        fifth.append(board[i][j])
        check[(i,j)] = True

    for i,j in zip(range(x,x+d2+1), range(y,y+d2+1)):
        try:
            a = check[(i,j)]
        except:
            fifth.append(board[i][j])
            check[(i, j)] = True

    for i,j in zip(range(x+d1,x+d1+d2+1), range(y-d1,y-d1+d2+1)):
        try:
            a = check[(i,j)]
        except:
            fifth.append(board[i][j])
            check[(i, j)] = True

    for i,j in zip(range(x+d2,x+d2+d1+1), range(y+d2,y+d2-d1-1,-1)):
        try:
            a = check[(i,j)]
        except:
            fifth.append(board[i][j])
            check[(i, j)] = True
    for i in range(x+1,x+d1+d2):
        count = 0
        for j in range(N):
            try:
                a = check[(i,j)]
                count +=1
                if count == 2:
                    break
            except:
                try:
                    a = check[(i-1,j)]
                    b = check[(i,j-1)]
                    check[(i,j)] = True
                    fifth.append(board[i][j])
                except:
                    continue
    check2 = copy.deepcopy(check)

    for i in range(x+d1):
        for j in range(y+1):
            try:
                a = check[(i,j)]
            except:
                first.append(board[i][j])
                check[(i,j)] = True
    for i in range(x+d2+1):
        for j in range(y,N):
            try:
                a = check[(i,j)]
            except:
                second.append(board[i][j])
                check[(i,j)] = True

    for i in range(x+d1-1,N):
        for j in range(y-d1+d2):
            try:
                a = check[(i,j)]
            except:
                third.append(board[i][j])
                check[(i,j)] = True

    for i in range(x+d2-1,N):
        for j in range(y-d1+d2-2,N):
            try:
                a = check[(i,j)]
            except:
                fourth.append(board[i][j])
                check[(i,j)] = True

    Max = max(sum(first),sum(second),sum(third),sum(fourth),sum(fifth))
    Min = min(sum(first), sum(second), sum(third), sum(fourth), sum(fifth))
    ans = Max - Min
    return ans

def inRange(x,y,d1,d2):
    if d1 >= 1 and d2 >=1 :
        if 0 <= x < x+d1+d2 <N:
            if 0 <= y-d1 < y < y+d2 <N:
                return True
    return False

max_ans = 1000


for x in range(N):
    for y in range(N):
        for d1 in range(1,N):
            for d2 in range(1,N):
                if inRange(x,y,d1,d2):
                    ans = pop_check(x,y,d1,d2)
                    max_ans = min(max_ans,ans)
print(max_ans)