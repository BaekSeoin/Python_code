import sys

sys.stdin = open("input.txt","r")

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())

number = str(A * B * C)

result = [0] * 10

for i in number:
    for j in range(10):
        if int(i) == j:
            result[j] += 1
            continue

for h in result:
    print(h)


