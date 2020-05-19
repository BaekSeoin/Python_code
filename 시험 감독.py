import sys

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())

A = [int(i) for i in sys.stdin.readline().rstrip().split()]

B,C = tuple(map(int,sys.stdin.readline().rstrip().split()))

count =0

for num in A:
    num -= B
    count +=1

    if num > 0:
        x = num // C
        y = num % C

        if y > 0:
            count += x+1
        else:
            count += x
print(count)