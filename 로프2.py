import sys

sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())

List = []

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    List.append(a)

List.sort()

Max = 0
num = len(List)

for i in List:
    x = i * num
    if x> Max:
        Max = x
    num -= 1
print(Max)
