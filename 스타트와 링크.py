import sys
import copy

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())

num = N // 2

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

final_List = []

def dfs(List,index):
    if len(List) == num:
        final_List.append(copy.deepcopy(List))
        return

    for i in range(index+1,N+1):
        if i not in List:
            List.append(i)
            dfs(List,i)
            List.pop()
List = []
dfs(List,0)

def other_team(team):
    second_team = []
    for i in range(1,N+1):
        if i not in team:
            second_team.append(i)
    return second_team

min_difference = 100*(N**2)

def calculate(team):
    ans = 0
    for i in team:
        for j in team:
            if i !=j:
                ans += board[i-1][j-1]
    return ans

for first_team in final_List:
    second_team = other_team(first_team)

    first_team_point = calculate(first_team)
    second_team_point = calculate(second_team)

    ans = abs(first_team_point-second_team_point)

    if ans < min_difference:
        min_difference = ans
print(min_difference)


