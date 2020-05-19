import sys
import copy

sys.stdin = open("input.txt", "r")

N, K = tuple(map(int,sys.stdin.readline().rstrip().split()))

matrix = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

B = [int(i) for i in sys.stdin.readline().rstrip().split()]
C = [int(i) for i in sys.stdin.readline().rstrip().split()]

A_order = []

def dfs(List):
    if len(List) == N:
        A_order.append(copy.deepcopy(List))
    for i in range(1,N+1):
        if i not in List:
            List.append(i)
            dfs(List)
            List.pop()

List = []
dfs(List)

def player_change(player_1, player_2):
    player_list =['a','b','c']

    for player in player_list:
        if player != player_1 and player != player_2:
            return player

def player_order(player_1, player_2):
    if player_1=='a':
        return player_1, player_2
    elif player_1 == 'b':
        if player_2 == 'a':
            return player_2,player_1
        else:
            return player_1, player_2
    else:
        return player_2, player_1

for A in A_order:
    a_index = 0
    b_index = 0
    c_index = 0

    player_1 = 'a'
    player_2 = 'b'
    a_k = 0
    b_k = 0
    c_k = 0

    ans= 0

    while True:

        if player_1 == 'a':
            cur1 = A[a_index]
            a_index +=1
        elif player_1 == 'b':
            cur1 = B[b_index]
            b_index +=1

        if player_2 == 'b':
            cur2 = B[b_index]
            b_index+=1
        elif player_2=='c':
            cur2 = C[c_index]
            c_index+=1

        result = matrix[cur1-1][cur2-1]

        if player_1 == 'a':
            if result == 2:
                a_k+=1
            else:
                if player_2 == 'b':
                    b_k +=1
                else:
                    c_k+=1

        elif player_1 == 'b':
            if result == 2:
                b_k+=1
            else:
                c_k +=1

        if result == 0 or result ==1:
            new_player = player_change(player_1,player_2)
            player_1 = player_2
            player_2 = new_player
        else:
            new_player = player_change(player_1,player_2)
            player_2 = new_player

        player_1,player_2 = player_order(player_1,player_2)

        if a_k == K or b_k ==K or c_k == K:
            if a_k == K:
                ans = 1
            break
        if a_index >= N:
            break
    if ans == 1:
        print(ans)
        break

if ans == 0:
    print(ans)