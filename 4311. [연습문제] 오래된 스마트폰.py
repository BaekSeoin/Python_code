import sys
from collections import deque

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())
def initial_check(W):
    for i in str(W):
        if int(i) not in number:
            return False
    return True

def operator_func(cur_num, i, prev_opr):
    if prev_opr == 1:
        ans = cur_num + i
    elif prev_opr == 2:
        ans = cur_num - i
    elif prev_opr == 3:
        ans = cur_num * i
    else:
        ans = cur_num // i
    return ans


def bfs(List):
    global min_num, max_num,W, min_touch_count
    while List:
        current = List.popleft()
        cur_num = current[0] #지금까지 숫자
        next = current[1] #연산해야할 숫자
        prev_opr =current[2] #이전에 했던 연산 (0 이면 숫자고른거, 아니면 이전에 했던 연산)
        opr_count =current[3] #연산 count
        very_prev_opr = current[4]
        touch_count = current[5]

        if touch_count >= min_touch_count:
            return 100000

        if prev_opr == 0:
            for j in operator:
                if opr_count == 1:
                    next_num = operator_func(cur_num,next,very_prev_opr)
                    if next_num == W:
                        return touch_count + 1
                    List.append((next_num,0,j,1,j,touch_count+1))
                else:
                    List.append((cur_num,next,j,opr_count+1,j,touch_count+1))
            for i in number:
                next_num = int(str(next) + str(i))
                if next_num !=0 and min_num < next_num < max_num:
                    List.append((cur_num,next_num,0,opr_count,very_prev_opr,touch_count+1))
        elif prev_opr !=0:
            for i in number:
                next_num = int(str(next) + str(i))
                if next_num !=0 and min_num < next_num < max_num:
                    List.append((cur_num,next_num,0,opr_count,very_prev_opr,touch_count+1))


for test in range(1,T+1):
    #터치가능한 숫자들의 개수, 터치 가능한 연산자들의 개수, 최대 터치가능한 횟수
    N,O,M = tuple(map(int,input().rstrip().split()))
    number =[int(i) for i in input().rstrip().split()] # 터치가능한 숫자들
    operator = [int(i) for i in input().rstrip().split()] #터치가능한 연산자 (+:1,-:2, *:3, /:4)
    W = int(input().rstrip()) #원하는 숫자
    min_num, max_num = -1, 1000
    min_touch_count = M+1

    if initial_check(W):
        min_touch_count =len(str(W))
        print(min_touch_count)
        continue
    else:
        for cur in number:
            List = deque()
            List.append((cur,0,0,0,0,1))
            touch_count = bfs(List)
            if touch_count+1 < min_touch_count:
                min_touch_count = touch_count+1
    if min_touch_count == M+1:
        print(-1)
    else:
        print(min_touch_count)
