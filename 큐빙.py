import sys
from collections import deque

sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())

#위/오/아래/왼

cube_move = {'U':[[(11,3),(11,4),(11,5)],[(3,8),(3,7),(3,6)],[(3,5),(3,4),(3,3)],[(3,2),(3,1),(3,0)]],
             'D':[[(5,3),(5,4),(5,5)],[(5,6),(5,7),(5,8)],[(9,5),(9,4),(9,3)],[(5,0),(5,1),(5,2)]],
             'F':[[(2,3),(2,4),(2,5)],[(3,6),(4,6),(5,6)],[(6,5),(6,4),(6,3)],[(5,2),(4,2),(3,2)]],
             'B':[[(8,3),(8,4),(8,5)],[(5,8),(4,8),(3,8)],[(0,5),(0,4),(0,3)],[(3,0),(4,0),(5,0)]],
             'L':[[(0,3),(1,3),(2,3)],[(3,3),(4,3),(5,3)],[(6,3),(7,3),(8,3)],[(9,3),(10,3),(11,3)]],
             'R':[[(2,5),(1,5),(0,5)],[(11,5),(10,5),(9,5)],[(8,5),(7,5),(6,5)],[(5,5),(4,5),(3,5)]]}

cube_move_2 = {'U':[[(0,3),(0,4),(0,5)],[(0,5),(1,5),(2,5)],[(2,5),(2,4),(2,3)],[(2,3),(1,3),(0,3)]],
             'D':[[(6,3),(6,4),(6,5)],[(6,5),(7,5),(8,5)],[(8,5),(8,4),(8,3)],[(8,3),(7,3),(6,3)]],
             'F':[[(3,3),(3,4),(3,5)],[(3,5),(4,5),(5,5)],[(5,5),(5,4),(5,3)],[(5,3),(4,3),(3,3)]],
             'B':[[(9,3),(9,4),(9,5)],[(9,5),(10,5),(11,5)],[(11,5),(11,4),(11,3)],[(11,3),(10,3),(9,3)]],
             'L':[[(3,0),(3,1),(3,2)],[(3,2),(4,2),(5,2)],[(5,2),(5,1),(5,0)],[(5,0),(4,0),(3,0)]],
             'R':[[(3,6),(3,7),(3,8)],[(3,8),(4,8),(5,8)],[(5,8),(5,7),(5,6)],[(5,6),(4,6),(3,6)]]}

def cubing(side, dir):
    global cube
    side_move = cube_move[side]
    side_move_2 = cube_move_2[side]

    if dir == '+':
        last = side_move[3]
        last_2 = side_move_2[3]
        List = deque()
        List.append(cube[last[0][0]][last[0][1]])
        List.append(cube[last[1][0]][last[1][1]])
        List.append(cube[last[2][0]][last[2][1]])

        for p in side_move:

            first = cube[p[0][0]][p[0][1]]
            second = cube[p[1][0]][p[1][1]]
            third = cube[p[2][0]][p[2][1]]
            List.append(first)
            List.append(second)
            List.append(third)
            cube[p[0][0]][p[0][1]] = List.popleft()
            cube[p[1][0]][p[1][1]] = List.popleft()
            cube[p[2][0]][p[2][1]] = List.popleft()

        List_2 =deque()
        List_2.append(cube[last_2[0][0]][last_2[0][1]])
        List_2.append(cube[last_2[1][0]][last_2[1][1]])
        List_2.append(cube[last_2[2][0]][last_2[2][1]])

        for q in side_move_2:
            first = cube[q[0][0]][q[0][1]]
            second = cube[q[1][0]][q[1][1]]
            third = cube[q[2][0]][q[2][1]]
            List_2.append(first)
            List_2.append(second)
            List_2.append(third)

        for w in side_move_2:
            cube[w[0][0]][w[0][1]] = List_2.popleft()
            cube[w[1][0]][w[1][1]] = List_2.popleft()
            cube[w[2][0]][w[2][1]] = List_2.popleft()

    elif dir == '-':
        last = side_move[0]
        last_2 = side_move_2[0]
        List = deque()
        List.append(cube[last[0][0]][last[0][1]])
        List.append(cube[last[1][0]][last[1][1]])
        List.append(cube[last[2][0]][last[2][1]])

        for p in side_move[::-1]:
            first = cube[p[0][0]][p[0][1]]
            second = cube[p[1][0]][p[1][1]]
            third = cube[p[2][0]][p[2][1]]
            List.append(first)
            List.append(second)
            List.append(third)
            cube[p[0][0]][p[0][1]] = List.popleft()
            cube[p[1][0]][p[1][1]] = List.popleft()
            cube[p[2][0]][p[2][1]] = List.popleft()

        List_2 = deque()
        List_2.append(cube[last_2[0][0]][last_2[0][1]])
        List_2.append(cube[last_2[1][0]][last_2[1][1]])
        List_2.append(cube[last_2[2][0]][last_2[2][1]])

        for q in side_move_2[::-1]:
            first = cube[q[0][0]][q[0][1]]
            second = cube[q[1][0]][q[1][1]]
            third = cube[q[2][0]][q[2][1]]
            List_2.append(first)
            List_2.append(second)
            List_2.append(third)

        for w in side_move_2[::-1]:
            cube[w[0][0]][w[0][1]] = List_2.popleft()
            cube[w[1][0]][w[1][1]] = List_2.popleft()
            cube[w[2][0]][w[2][1]] = List_2.popleft()

for i in range(n):
    cube = [[0, 0, 0, 'w', 'w', 'w', 0, 0, 0], [0, 0, 0, 'w', 'w', 'w', 0, 0, 0], [0, 0, 0, 'w', 'w', 'w', 0, 0, 0],
            ['g', 'g', 'g', 'r', 'r', 'r', 'b', 'b', 'b'], ['g', 'g', 'g', 'r', 'r', 'r', 'b', 'b', 'b'],
            ['g', 'g', 'g', 'r', 'r', 'r', 'b', 'b', 'b'],
            [0, 0, 0, 'y', 'y', 'y', 0, 0, 0], [0, 0, 0, 'y', 'y', 'y', 0, 0, 0], [0, 0, 0, 'y', 'y', 'y', 0, 0, 0],
            [0, 0, 0, 'o', 'o', 'o', 0, 0, 0], [0, 0, 0, 'o', 'o', 'o', 0, 0, 0], [0, 0, 0, 'o', 'o', 'o', 0, 0, 0]]

    c = int(sys.stdin.readline().rstrip())
    move = [j for j in sys.stdin.readline().rstrip().split()]
    for k in move:
        side,dir = k[0],k[1]
        cubing(side,dir)

    for u in range(3):
        for l in range(3,6):
            print(cube[u][l],end='')
        print()