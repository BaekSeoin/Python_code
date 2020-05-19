import sys
import copy

sys.stdin = open('input.txt','r')

game = [[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40],[0,13,16,19,25,26,27,28,30],
        [0,22,24,25,30,35,40],[0,28,27,26,25,19,16,13,10]]

turn = [int(i) for i in sys.stdin.readline().rstrip().split()]

List = []
lst = []


def dfs(lst):
    if len(lst) == 10:
        List.append(copy.deepcopy(lst))
        print(lst)
        return
    for i in range(10):
        if i not in lst:
            lst.append(i)
            dfs(lst)
            lst.pop()

#dfs(lst)

game_num = 0
index = 0
point = 0
for i in turn:
    index += i
    if (game_num == 0) and index >= 20:
        point += 40
        break
    elif (game_num == 0) and (index % 5 != 0):
        point += game[game_num][index]
    elif (game_num == 0) and (index % 5 == 0):
        point += game[game_num][index]
        game_num = index // 5
        index = 0
    elif (game_num == 1) and (index < 4):
        point += game[game_num][index]
    elif (game_num == 1) and (index >= 4):
        game_num = 2
        index = 3 + abs(4-index)
        try:
            point += game[game_num][index]
        except:
            point += game[game_num][6]
            break
    elif (game_num == 2) and index < 6:
        point += game[game_num][index]
    elif (game_num == 2) and index >= 6:
        point += game[game_num][6]
        break
    elif (game_num == 3) and (index < 4):
        point += game[game_num][index]
    elif (game_num == 3) and (index >= 4):
        game_num = 2
        index = 3 + abs(4-index)
        try:
            point += game[game_num][index]
        except:
            point += game[game_num][6]
            break


print(point)