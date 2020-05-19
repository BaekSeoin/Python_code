import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

direction = {(1,1):(-1, 1),(-1, 1):(1,1),(1,-1):(-1, -1),(-1, -1):(1,-1)}

if N >=2:
    shape = [[' ' for i in range(8*2**(N-2)-3)] for j in range(4*2**(N-2)-1)]

    if N%2 == 0:
        start_1 = (0,0)
        start_2 = (0,8*2**(N-2)-4)
        dir_1 = (1,1)
        dir_2 = (1,-1)

    else:
        start_1 = (4*2**(N-2)-2,0)
        start_2 = (4*2**(N-2)-2,8*2**(N-2)-4)
        dir_1 = (-1, 1)
        dir_2 = (-1, -1)

    for n in range(N,1,-1):
        move_1 = start_1
        move_2 = start_2

        for i in range(start_1[1],start_2[1]+1):
            shape[start_1[0]][i] = '*'

        turn = 4*2**(n-2)-2
        half = int(turn/2)

        if dir_1 == (1,1):
            ans =  half + move_1[0]
        else:
            ans = move_1[0] - half

        for i in range(turn):
            move_1 = (move_1[0] + dir_1[0], move_1[1]+dir_1[1])
            move_2 = (move_2[0] + dir_2[0], move_2[1] + dir_2[1])
            #print(move_1,move_2)
            shape[move_1[0]][move_1[1]] = '*'
            shape[move_2[0]][move_2[1]] = '*'
            if move_1[0] == ans:
                start_1 = (move_1[0],move_1[1]+1)
                start_2 = (move_2[0], move_2[1] - 1)

        dir_1 = direction[dir_1]
        dir_2 = direction[dir_2]

    shape[move_1[0]-1][move_1[1]] = '*'

    for i in range(4*2**(N-2)-1):
        print("".join(shape[i]).rstrip())

else:
    print("*")