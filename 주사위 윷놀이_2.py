import sys

sys.stdin = open('input.txt','r')

game = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,13,16,19,25,28,27,26,22,24,30,35,0]

visit = [0 for i in range(33)]

predict = [int(i) for i in sys.stdin.readline().rstrip().split()]

index_1 = 0
index_2 = 0
index_3 = 0
index_4 = 0

move = 0

def change(index_x,start_index):
    if (start_index == 5) and (index_x == 5):
        index_x = 21
    elif (start_index == 10) and index_x == 10:
        index_x = 28
    elif (start_index == 15) and index_x == 15:
        index_x = 25
    elif index_x == 27:
        index_x = 24
    elif index_x == 24:
        index_x = 30
    elif index_x == 29:
        index_x = 24
    elif index_x == 31:
        index_x = 20
    elif index_x == 20:
        index_x = 32
    else:
        index_x += 1
    return index_x

def cal(cur_move,index_x, start_index):
    for i in range(cur_move):
        index_x = change(index_x,start_index)
    return index_x

max_point = 0
def dfs(move,point):
    global index_1, index_2, index_3,index_4,max_point

    if move == 10:
        if point > max_point:
            max_point = point
        return

    cur_move = predict[move]

    for i in range(1,5):
        if i == 1:
            if index_1 < 32:
                new_index = cal(cur_move, index_1, index_1)
                if new_index >= 32:
                    new_index = 32
                if (visit[new_index] == 0) or new_index == 32:
                    visit[new_index] = 1
                    visit[index_1] = 0
                    store = index_1
                    index_1 = new_index
                    cur_point = game[index_1]
                    dfs(move+1,point+cur_point)
                    visit[index_1] = 0
                    index_1 = store
                    visit[index_1] = 1
        if i == 2:
            if index_2 < 32:
                new_index = cal(cur_move, index_2,index_2)
                if new_index >= 32:
                    new_index = 32
                if (visit[new_index] == 0) or new_index == 32:
                    visit[new_index] = 2
                    visit[index_2] = 0
                    store = index_2
                    index_2 = new_index
                    cur_point = game[index_2]
                    dfs(move+1,point+cur_point)
                    visit[index_2] = 0
                    index_2 = store
                    visit[index_2] = 2
        if i == 3:
            if index_3 < 32:
                new_index = cal(cur_move, index_3,index_3)
                if new_index >= 32:
                    new_index = 32
                if (visit[new_index] == 0) or new_index == 32:
                    visit[new_index] = 3
                    visit[index_3] = 0
                    store = index_3
                    index_3 = new_index
                    cur_point = game[index_3]
                    dfs(move+1,point+cur_point)
                    visit[index_3] = 0
                    index_3 = store
                    visit[index_3] = 3
        if i == 4:
            if index_4 < 32:
                new_index = cal(cur_move, index_4,index_4)
                if new_index >= 32:
                    new_index = 32
                if (visit[new_index] == 0) or new_index == 32:
                    visit[new_index] = 4
                    visit[index_4] = 0
                    store = index_4
                    index_4 = new_index
                    cur_point = game[index_4]
                    dfs(move+1,point+cur_point)
                    visit[index_4] = 0
                    index_4 = store
                    visit[index_4] = 4


dfs(move,0)
print(max_point)


