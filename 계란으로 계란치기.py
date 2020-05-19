import sys

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())

egg = []

for i in range(N):
    #내구도/무게/깨짐 or 안깨짐(1,0)
    S,W = tuple(map(int,sys.stdin.readline().rstrip().split()))
    egg.append([S,W,0])

Max_egg_break_count = 0

def dfs(egg_num,egg_break_count):
    global Max_egg_break_count
    if egg_num == N:
        if Max_egg_break_count < egg_break_count:
            Max_egg_break_count = egg_break_count
        return

    current_pos = egg[egg_num]
    egg_s = current_pos[0]
    egg_w = current_pos[1]
    egg_break = current_pos[2]

    if egg_break == 1:
        dfs(egg_num+1,egg_break_count)
        return

    count =0
    for next_egg in range(N):
        next_egg_pos = egg[next_egg]
        next_egg_s = next_egg_pos[0]
        next_egg_w = next_egg_pos[1]
        next_egg_break = next_egg_pos[2]
        a = False
        b = False
        if next_egg != egg_num and next_egg_break == 0:
            new_egg_s = egg_s - next_egg_w
            new_next_egg_s = next_egg_s - egg_w

            if new_egg_s <=0:
                egg_break = 1
                a = True
                egg_break_count +=1

            egg[egg_num] = [new_egg_s,egg_w,egg_break]
            if new_next_egg_s <=0:
                next_egg_break = 1
                b = True
                egg_break_count += 1

            egg[next_egg] = [new_next_egg_s,next_egg_w,next_egg_break]
        elif next_egg == egg_num:
            continue
        else:
            count +=1
            if count < N-1:
                continue
            else:
                dfs(egg_num+1,egg_break_count)
                if Max_egg_break_count== N:
                    return
                continue
        dfs(egg_num+1,egg_break_count)
        if Max_egg_break_count == N:
            return
        if a:
            egg_break = 0
            egg_break_count -= 1
            a = False
        egg[egg_num] = [egg_s,egg_w,egg_break]
        if b:
            next_egg_break = 0
            egg_break_count -=1
            b = False
        egg[next_egg] = [next_egg_s, next_egg_w,next_egg_break]


dfs(0,0)
print(Max_egg_break_count)