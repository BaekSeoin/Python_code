from collections import deque

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def inRange(a, b):
    global N
    if (0 <= a < N) and (0 <= b < N):
        return True
    return False


def bfs(List, board):
    global end

    visit = dict()
    visit[(0, 0, 0, 1)] = True

    while List:
        x = List.popleft()
        cur1 = x[0]
        cur2 = x[1]
        cnt = x[2]
        cur_dir = x[3]

        if (cur1 == end) or (cur2 == end):
            return cnt

        for dir in direction:
            next1 = (cur1[0] + dir[0], cur1[1] + dir[1])
            next2 = (cur2[0] + dir[0], cur2[1] + dir[1])
            if (inRange(next1[0], next1[1])) and (inRange(next2[0], next2[1])):
                if (board[next1[0]][next1[1]] == 0) and (board[next2[0]][next2[1]] == 0):
                    a = [next1, next2]
                    a = sorted(a)
                    y = (a[0][0], a[0][1], a[1][0], a[1][1])
                    try:
                        z = visit[y]
                    except:
                        List.append((next1, next2, cnt + 1,cur_dir))
                        visit[y] = True

        if cur_dir == 0:
            next1 = (cur1[0] + 1, cur1[1])
            next2 = (cur2[0] + 1, cur2[1])
            next_dir = 1
        else:
            next1 = (cur1[0], cur1[1]+1)
            next2 = (cur2[0], cur2[1]+1)
            next_dir = 0

        if (inRange(next1[0], next1[1])) and (inRange(next2[0], next2[1])):
            if (board[next1[0]][next1[1]] == 0) and (board[next2[0]][next2[1]] == 0):
                a = [cur1, next1]
                a = sorted(a)
                y = (a[0][0], a[0][1], a[1][0], a[1][1])
                try:
                    z = visit[y]
                except:
                    List.append((cur1, next1, cnt + 1,next_dir))
                    visit[y] = True
                a = [cur2, next2]
                a = sorted(a)
                y = (a[0][0], a[0][1], a[1][0], a[1][1])
                try:
                    z = visit[y]
                except:
                    List.append((cur2, next2, cnt + 1,next_dir))
                    visit[y] = True
        if cur_dir == 0:
            next1 = (cur1[0] - 1, cur1[1])
            next2 = (cur2[0] - 1, cur2[1])
            next_dir = 1
        else:
            next1 = (cur1[0], cur1[1]-1)
            next2 = (cur2[0], cur2[1]-1)
            next_dir = 0

        if (inRange(next1[0], next1[1])) and (inRange(next2[0], next2[1])):
            if (board[next1[0]][next1[1]] == 0) and (board[next2[0]][next2[1]] == 0):
                a = [cur1, next1]
                a = sorted(a)
                y = (a[0][0], a[0][1], a[1][0], a[1][1])
                try:
                    z = visit[y]
                except:
                    List.append((cur1, next1, cnt + 1,next_dir))
                    visit[y] = True
                a = [cur2, next2]
                a = sorted(a)
                y = (a[0][0], a[0][1], a[1][0], a[1][1])
                try:
                    z = visit[y]
                except:
                    List.append((cur2, next2, cnt + 1,next_dir))
                    visit[y] = True

    return -1


def solution(board):
    global N, end
    N = len(board)
    List = deque()
    end = (N - 1, N - 1)
    cur1 = (0, 0)
    cur2 = (0, 1)
    cnt = 0
    List.append((cur1, cur2, cnt,0)) # dir 0 ㄱㅏ로, dir 1 세
    answer = bfs(List, board)

    return answer

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))