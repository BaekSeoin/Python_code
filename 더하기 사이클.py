import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

num = N
count = 0
while True:
    count += 1
    if num < 10:
        new_num = num
        real_num = int(str(num) + str(new_num))
    else:
        new_num = int(str(num)[0]) + int(str(num)[1])
        if new_num < 10:
            real_num = int(str(num)[1] + str(new_num))
        else:
            real_num = int(str(num)[1] + str(new_num)[1])

    if real_num == N:
        print(count)
        break
    num = real_num
