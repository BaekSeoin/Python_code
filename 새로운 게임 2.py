import sys

sys.stdin = open('input.txt','r')

N,K = tuple(map(int,sys.stdin.readline().rstrip().split()))

#우/좌/상/
direction = {1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)}

def inRange(a,b):
    if 0<=a<N and 0<=b<N:
        return True
    return False

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

cur_pos = dict()
pos = dict()

for i in range(1,K+1):
    r,c,dir = tuple(map(int,sys.stdin.readline().rstrip().split()))

    cur_pos[i] = (r-1,c-1,dir)
    try:
        pos[(r-1,c-1)].append(i)
    except:
        pos[(r-1,c-1)] = []
        pos[(r - 1, c - 1)].append(i)

turn = 0
stop = False
while turn < 1000:
    turn +=1

    for i in range(1,K+1):
        cur = cur_pos[i]
        curPos = (cur[0],cur[1])
        dir = cur[2]
        nextdir = direction[dir]

        together_k = pos[curPos]
        cur_index = together_k.index(i)

        pos[curPos] = together_k[:cur_index]
        together = together_k[cur_index:]

        nextPos = (curPos[0] + nextdir[0], curPos[1] + nextdir[1])

        if inRange(nextPos[0],nextPos[1]):
            #흰색
            if board[nextPos[0]][nextPos[1]] == 0:
                for j in together:
                    a = cur_pos[j][2]
                    del cur_pos[j]
                    cur_pos[j] = (nextPos[0],nextPos[1],a)
                    try:
                        pos[nextPos].append(j)
                    except:
                        pos[nextPos]=[]
                        pos[nextPos].append(j)
            #빨간
            elif board[nextPos[0]][nextPos[1]] == 1:
                for j in together[::-1]:
                    a = cur_pos[j][2]
                    del cur_pos[j]
                    cur_pos[j] = (nextPos[0],nextPos[1],a)
                    try:
                        pos[nextPos].append(j)
                    except:
                        pos[nextPos] = []
                        pos[nextPos].append(j)
        if (inRange(nextPos[0],nextPos[1]) == False) or (board[nextPos[0]][nextPos[1]] == 2):
            nextPos = (curPos[0]-nextdir[0],curPos[1]-nextdir[1])
            if inRange(nextPos[0],nextPos[1]):
                if board[nextPos[0]][nextPos[1]] == 0:
                    for j in together:
                        a = cur_pos[j][2]
                        if j == i:
                            if a % 2 == 0:
                                a -= 1
                            else:
                                a += 1
                        del cur_pos[j]
                        cur_pos[j] = (nextPos[0], nextPos[1], a)
                        try:
                            pos[nextPos].append(j)
                        except:
                            pos[nextPos] = []
                            pos[nextPos].append(j)
                # 빨간
                elif board[nextPos[0]][nextPos[1]] == 1:
                    for j in together[::-1]:
                        a = cur_pos[j][2]
                        if j == i:
                            if a % 2 == 0:
                                a -= 1
                            else:
                                a += 1
                        del cur_pos[j]
                        cur_pos[j] = (nextPos[0], nextPos[1], a)
                        try:
                            pos[nextPos].append(j)
                        except:
                            pos[nextPos] = []
                            pos[nextPos].append(j)
            if (inRange(nextPos[0],nextPos[1]) == False) or (board[nextPos[0]][nextPos[1]] == 2):
                for j in together:
                    a = cur_pos[j][2]
                    if j == i:
                        if a % 2 == 0:
                            a -= 1
                        else:
                            a += 1
                    del cur_pos[j]
                    cur_pos[j] = (curPos[0], curPos[1], a)
                    try:
                        pos[curPos].append(j)
                    except:
                        pos[curPos] = []
                        pos[curPos].append(j)

        for k, v in pos.items():

            if len(v) >= 4:
                print(turn)
                stop = True

        if stop:
            break
    if stop:
        break

if stop == False:
    print(-1)

