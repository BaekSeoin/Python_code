import sys

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

def function(n,k):
    up = 1
    down = 1
    for i in range(n,n-k,-1):
        up *= i
    for j in range(1,k+1):
        down *= j
    ans = up // down
    return ans

def calculate(num):
    while num > 1:
        a = 2
        while True:
            if num % a == 0:
                num //= a
                try:
                    check[a] +=1
                except:
                    check[a] = 1
                break
            else:
                a +=1
for test in range(1,T+1):
    n,k = tuple(map(int,input().rstrip().split()))
    num = function(n,k)
    check = dict()
    num = num % 1000000007
    calculate(num)
    final_ans = 1
    for k,v in check.items():
        final_ans *=(v+1)
    print('#'+str(test),end=' ')
    print(final_ans)