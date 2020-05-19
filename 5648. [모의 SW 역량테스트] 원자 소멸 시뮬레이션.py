import sys

sys.stdin = open("input.txt", "r")

#상하좌우
direction = {0:(0,0.5),1:(0,-0.5),2:(-0.5,0),3:(0.5,0)}

T = int(input().rstrip())

def inRange(a,b):
    if -1000 <= a <=1000 and -1000 <= b <= 1000:
        return True
    return False

def move(atom):
    atom2 = []
    for A in atom:
        current = A[0]
        dir = A[1]
        nextPos = (current[0] + dir[0], current[1] + dir[1])
        if inRange(nextPos[0],nextPos[1]):
            atom2.append((nextPos, dir, A[2]))
    return atom2

def check_pos(atom):
    global energy
    yeah = dict()
    atom2 = []
    for i in atom:
        try:
            yeah[i[0]].append((i[1],i[2]))
        except:
            yeah[i[0]] = [(i[1],i[2])]

    for key, values in yeah.items():
        if len(values) > 1:
            for add in values:
                energy += add[1]
        else:
            atom2.append((key,values[0][0],values[0][1]))
    return atom2

for test in range(1,T+1):
    N = int(input())
    atom = []
    for i in range(N):
        x,y,dir, k = tuple(map(int,input().rstrip().split()))
        dir = direction[dir]
        atom.append(((x,y), dir, k))
    energy = 0
    for i in range(4002):
        atom = move(atom)
        atom = check_pos(atom)
        R = len(atom)
        if R ==0 or R == 1:
            break
    print('#'+str(test),end =' ')
    print(energy)