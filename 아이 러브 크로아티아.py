import sys
sys.stdin = open("input.txt","r")

K = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
finish_time = 210
time = 0
while True:
    a = [i for i in sys.stdin.readline().rstrip().split()]
    time += int(a[0])
    correct = a[1]

    if time >= finish_time:
        print(K)
        break

    if correct == "T":
        if K < 8:
            K += 1

        elif K == 8:
            K = 1

