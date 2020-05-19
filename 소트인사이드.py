import sys

sys.stdin = open('input.txt','r')

N = [i for i in sys.stdin.readline().rstrip()]

N.sort(reverse=True)

print(int("".join(N)))