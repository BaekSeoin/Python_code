import sys

sys.stdin = open("input.txt","r")

A, B = (sys.stdin.readline().rstrip().split())

if int(A) > int(B):
    print('>')

elif int(A) < int(B):
    print('<')
else:
    print('==')