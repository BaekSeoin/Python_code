import sys
import copy

sys.stdin = open('input.txt','r')

N,M,D = tuple(map(int,sys.stdin.readline().rstrip().split()))

enemy2 = []

for i in range(N):
    for j,num in enumerate(sys.stdin.readline().rstrip().split()):
        if int(num) == 1:
            enemy2.append((i,j))

def inRange(a,b):
    if 0<=a<N and 0<=b<M:
        return True
    return False

def distance_check(a,b):
    ans = abs(a[0]-b[0]) + abs(a[1] - b[1])
    return ans

pos = []
List = []

def dfs(List):
    if len(List) == 3:
        pos.append(List.copy())
        return

    for i in range(M):
        if (N,i) not in List:
            List.append((N,i))
            dfs(List)
            List.pop()
dfs(List)
max_die = 0

for curPos in pos:
    die = 0
    enemy = copy.deepcopy(enemy2)
    while True:
        final_list = []
        die_check = []
        for Pos in curPos:
            min_dist = 1000
            kill_check = []
            for en in enemy:
                dist = distance_check(Pos,en)
                if dist <=D:
                    if dist < min_dist:
                        kill_check = []
                        kill_check.append(en)
                        min_dist = dist
                    elif dist == min_dist:
                        kill_check.append(en)
            if len(kill_check) == 1:
                final_list.append(kill_check[0])

            elif len(kill_check) > 1:
                west = (0,M)
                for i in kill_check:
                    if i[1] < west[1]:
                        west = i
                final_list.append(west)
        for i in final_list:
            if i in enemy:
                enemy.remove(i)
                die +=1
        new_enemy = []
        for j in enemy:
            if j[0]+1 < N:
                new_enemy.append((j[0]+1,j[1]))
        if len(new_enemy) == 0:
            break
        else:
            enemy = new_enemy
    if die > max_die:
        max_die = die

print(max_die)