def key_change(key):
    new_key = []

    for j in range(len(key[0])):
        temp = []
        for i in range(len(key)-1,-1,-1):
            temp.append(key[i][j])
        new_key.append(temp)

    return new_key


def check(startPos, board, key):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(i,j)
            print(startPos[0] + i, startPos[1] + j)
            if (board[i][j] == 1) and (key[startPos[0] + i][startPos[1] + j] == 1):
                return False
            elif (board[i][j] == 0) and (key[startPos[0] + i][startPos[1] + j] == 0):
                return False
    return True


def solution(key, lock):
    answer = False

    max_i, min_i = 0, len(lock) - 1
    max_j, min_j = 0, len(lock) - 1
    List = []

    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                max_i = max(max_i, i)
                min_i = min(min_i, i)
                max_j = max(max_j, j)
                min_j = min(min_j, j)
                List.append((i, j))

    board = []
    for i in range(min_i, max_i + 1):
        new = []
        for j in range(min_j, max_j + 1):
            if (i, j) in List:
                new.append(0)
            else:
                new.append(1)
        board.append(new)

    for i in range(4):
        if i != 0:
            key = key_change(key)

        for i in range(len(key) - len(board) + 1):
            for j in range(len(key[0]) - len(board[0]) + 1):
                startPos = (i, j)
                answer = check(startPos, board, key)
                if answer:
                    break
            if answer:
                break
        if answer:
            break

    return answer


key = [[0,1],[0,0],[0,0]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key,lock))