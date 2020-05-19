import sys
sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline().rstrip())
A = [int(i) for i in sys.stdin.readline().rstrip().split()]
cal = [int(i) for i in sys.stdin.readline().rstrip().split()]

result = []
Max = -1000000000
Min = 1000000000

def dfs(cal, i, a):
    global Max, Min
    if i ==len(A)-1:
        if a > Max:
            Max = a
        if a < Min:
            Min = a
        return

    if cal[0] >= 1:
        cal[0] -= 1
        dfs(cal, i+1, a + A[i+1])
        cal[0] += 1

    if cal[1] >= 1:
        a -= A[i+1]
        cal[1] -= 1
        dfs(cal, i+1,a)
        a += A[i+1]
        cal[1] += 1

    if cal[2] >= 1:
        a *= A[i+1]
        cal[2] -= 1
        dfs(cal, i+1, a)
        a //= A[i+1]
        cal[2] += 1

    if cal[3] >= 1:
        if a >= 0:
            cal[3] -=1
            dfs(cal, i+1, a//A[i+1])

        else:
            cal[3] -=1
            dfs(cal, i+1, -(abs(a)//A[i+1]))
        cal[3] += 1


dfs(cal, 0, A[0])

print(Max)
print(Min)




