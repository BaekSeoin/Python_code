import sys
sys.setrecursionlimit(1500)

sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())
List = [-1 for i in range(n+1)]

def f(n):
    if n == 1:
        Ans = 1

    elif n == 2:
        Ans = 2

    else:
        if List[n] != -1:
            Ans = List[n]
        else:
            Ans = (f(n-1) + f(n-2)) % 10007

            List[n] = Ans

    return Ans

ans = f(n)

print(ans)