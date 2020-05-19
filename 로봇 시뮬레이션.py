import sys

sys.stdin = open("input.txt", "r")

A,B = tuple(map(int,sys.stdin.readline().rstrip().split()))
N,M = tuple(map(int,sys.stdin.readline().rstrip().split()))

def inRange(a,b):
    if 0<=a<B and 0<=b<A:
        return True
    return False

direction = {'N':(-1,0),'E':(0,1),'S':(1,0),'W':(0,-1)}

direction_change_L= {'N':'W','W':'S','S':'E','E':'N'}
direction_change_R = {'N':'E','E':'S','S':'W','W':'N'}

board = [[0 for i in range(A)] for j in range(B)]

robot = dict()

y_change = dict()
for i,j in zip(range(1,B+1),range(B,0,-1)):
    y_change[i] = j
    y_change[j] = i

for i in range(N):
    x,y,dir = tuple(map(str,sys.stdin.readline().rstrip().split()))
    y = y_change[int(y)]
    robot[i+1] = [y-1,int(x)-1,dir]
    board[y-1][int(x)-1] = i+1

count = 0
for i in range(M):
    robot_num,typeOforder,repeat = tuple(map(str,sys.stdin.readline().rstrip().split()))
    robot_num = int(robot_num)
    repeat = int(repeat)
    current_robot = robot[robot_num]
    currentPos = (current_robot[0],current_robot[1])
    dir = current_robot[2]
    dir_move = direction[dir]
    board[currentPos[0]][currentPos[1]] = 0
    for j in range(repeat):
        if typeOforder == 'L':
            dir = direction_change_L[dir]
        elif typeOforder == 'R':
            dir = direction_change_R[dir]
        elif typeOforder == 'F':
            currentPos = (currentPos[0] + dir_move[0],currentPos[1]+dir_move[1])
            if not inRange(currentPos[0],currentPos[1]):
                print("Robot",str(robot_num), "crashes into the wall")
                count +=1
                break
            elif board[currentPos[0]][currentPos[1]] !=0:
                print("Robot",str(robot_num), "crashes into robot",str(board[currentPos[0]][currentPos[1]]))
                count +=1
                break

    if count >0:
        break

    robot[robot_num] = [currentPos[0],currentPos[1],dir]
    board[currentPos[0]][currentPos[1]] = robot_num

    if i == M-1:
        print("OK")