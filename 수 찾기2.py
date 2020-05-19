import sys

sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())

A = dict()

for i in sys.stdin.readline().rstrip().split():
    A[int(i)] = True

MAX_A = max(A)

m = int(sys.stdin.readline().rstrip())
m_array = [int(u) for u in sys.stdin.readline().rstrip().split()]

for i in m_array:
    if MAX_A < i:
        print(0)
        continue
    try:
        if A[i] == True:
            print(1)
    except:
        print(0)
