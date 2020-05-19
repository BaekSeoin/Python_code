import sys
import copy

sys.stdin = open("input.txt", "r")

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(10)]

List = []

pre_lst = {1:[],2:[],3:[],4:[],5:[]}

lst_check = dict()

last_check = []

first =[(0,0)]
second = [(0,0),(0,1),(1,0),(1,1)]
third = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
fourth = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)]
fifth = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(2,2),(2,3),(2,4),
         (3,0),(3,1),(3,2),(3,3),(3,4),(4,0),(4,1),(4,2),(4,3),(4,4)]

def inRange(a,b):
    if (0<=a<10) and (0<=b<10):
        return True
    return False

def check(second,cur):
    ans = []
    for i,j in second:
        curPos = (cur[0] + i, cur[1] + j)
        ans.append(curPos)
        if inRange(curPos[0], curPos[1]) == False or (board[curPos[0]][curPos[1]] != 1):
            return (False, [])
    return (True, tuple(ans))

for i in range(10):
    for j in range(10):
        cur = (i,j)
        a = check(first,cur)
        if a[0]:
            pre_lst[1].append(a[1])
            lst_check[a[1]] = 1
            last_check.append(cur)
        b = check(second, cur)
        if b[0]:
            pre_lst[2].append(b[1])
            lst_check[b[1]] = 2
        c = check(third, cur)
        if c[0]:
            pre_lst[3].append(c[1])
            lst_check[c[1]] = 3
        d = check(fourth, cur)
        if d[0]:
            pre_lst[4].append(d[1])
            lst_check[d[1]] = 4
        e = check(fifth, cur)
        if e[0]:
            pre_lst[5].append(e[1])
            lst_check[e[1]] = 5

for i in range(5,0,-1):
    x = pre_lst[i]
    for j in x:
        List.append(j)


index = 0

min_color = 10000

num = 0
def visit_check(cur):
    for i,j in cur:
        if visit[i][j] == 1:
            return False
    return True


max_index = len(List)

def finish_check(visit__):
    for i,j in last_check:
        if visit__[i][j] != 1:
            return False
    return True


def pick(n, ans_list, index):

    if len(ans_list) == n:
        if finish_check(visit):
            final_list.append(copy.deepcopy(ans_list))
        return

    if index == len(List):
        return

    cur = List[index]
    if visit_check(cur):
        for i, j in cur:
            visit[i][j] = 1
        ans_list.append(cur)
        pick(n,ans_list,index+1)
        ans_list.pop()
        for i, j in cur:
            visit[i][j] = 0

    pick(n,ans_list,index+1)

n = 0
stop = False
Ans = 10000

while n < (len(List)+1):
    n += 1
    final_list = []
    ans_list = []
    visit = [[0 for i in range(10)] for j in range(10)]
    pick(n,ans_list,0)
    print(len(final_list))

    for ans in final_list:
        visit_2 = [[0 for i in range(10)] for j in range(10)]
        color = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        for cur in ans:
            cur_color_num = lst_check[cur]

            if color[cur_color_num] < 5:
                for i, j in cur:
                    visit_2[i][j] = 1
                color[cur_color_num] += 1
            else:
                break
        if finish_check(visit_2):
            Ans = n
            stop = True
            break
    if stop:
        break


"""
def dfs(index,count):
    global min_color, max_index, num

    if finish_check():

        if count < min_color:
            min_color = count
        return

    if count == (min_color-1):
        return

    if index >= max_index:
        return

    cur = List[index]

    cur_color_num = lst_check[cur]

    if color[cur_color_num] < 5:
        if visit_check(cur):
            for i,j in cur:
                visit[i][j] = 1
            color[cur_color_num] += 1
            dfs(index+1,count+1)
            color[cur_color_num] -= 1
            for i,j in cur:
                visit[i][j] = 0

    if count == (min_color-2):
        return

    dfs(index+1,count)


dfs(index,0)
"""

if Ans == 10000:
    print(-1)
else:
    print(Ans)
