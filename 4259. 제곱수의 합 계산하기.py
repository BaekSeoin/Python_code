import sys

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

def calculate(number):
    ans = 0
    for num in number:
        a = num[:-1]
        b = num[-1]
        ans += int(a) **int(b)
    return ans

for test in range(1,T+1):
    n= int(input().rstrip())
    number = [i for i in input().rstrip().split()]
    ans = calculate(number)
    print('#'+str(test),end = ' ')
    print(ans)