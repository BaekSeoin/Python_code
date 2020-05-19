import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt","r")


n = int(sys.stdin.readline().rstrip())

stairs = [int(i) for i in sys.stdin.readlines()]

length = len(stairs)

final = 0

def Function(index,count, point):
    global final
    if index == length-1:
        if point > final:
            final = point
        return

    for i in range(1,3):
        if count == 2 and i == 1:
            count = 1
            continue

        next_index = index + i
        if next_index < length:
            point += stairs[next_index]
            if i == 1:
                Function(next_index,count+1,point)
            else:
                Function(next_index, count, point)
            point -= stairs[next_index]

for i in range(0,2):
    if length == 1 and i == 1:
        continue

    point = stairs[i]
    count = 1
    Function(i,count,point)

print(final)