import sys

sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline().rstrip())

path = [[int(i) for i in sys.stdin.readline().rstrip().split()] for i in range(N)]

path_dict = dict()

for i in range(N):
    path_dict[i] = []

for i in range(N):
    for j in range(N):
        if path[i][j] == 1:
            path_dict[i].append(j)


def find_way(path, path_dict, i):
    if len(path_dict[i]) == 0:
        return False
    else:
        return True


def dfs(path, path_dict,a):

    if len(path_dict[a]) == 0:
        return
    else:
        for i in path_dict[a]:
            path[a][i] = 1
            dfs(path, path_dict, i)
        return

dfs(path, path_dict, 0)













