import sys
import copy
from collections import deque

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

final_point = 0

def dfs(List):
    if len(List) == 9:
        A = copy.deepcopy(List)
        final_list.append(A)
        return

    for i in range(2,10):
        if i not in List:
            if len(List) < 4:
                List.appendleft(i)
                dfs(List)
                List.popleft()
            else:
                List.append(i)
                dfs(List)
                List.pop()


List = deque()
List.append(1)
final_list = []
dfs(List)

index_change = {0:2,1:1,2:0}

def change(ground,action):
    point = 0
    if action == 4:
        for index,i in enumerate(ground):
            if i:
                point+=1
                ground[index] = False
        point +=1

    else:
        for index,i in enumerate(ground[::-1]):
            state = index_change[index]
            if not i:
                continue
            else:
                if state + 1 + action < 4:
                    ground[state+action] = True
                    ground[state] = False
                else:
                    ground[state] = False
                    point +=1
        ground[action-1] = True
    return point,ground

game_round = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

for order in final_list:
    get_point = 0
    for play in game_round:
        out = 0
        ground = [False,False,False]
        while out < 3:
            player = order[0]
            action = play[player-1]
            if action ==0:
                out +=1
            else:
                point,ground = change(ground,action)
                get_point += point
            order.rotate(-1)
    if get_point > final_point:
        final_point = get_point

print(final_point)
