import sys

sys.stdin = open("input.txt","r")

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())
P = int(sys.stdin.readline().rstrip())

A_fee = A * P

if  P <= C:
    B_fee = B
else:
    B_fee = B + (P-C) * D

print(min(A_fee,B_fee))