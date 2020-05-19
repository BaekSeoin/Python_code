import sys

sys.stdin = open("input.txt","r")

T = int(input())

def divide(number, m):
    x = 0
    for i in number:
        x = (x * 10 + int(i)) % m
    if x == 0:
        return True
    return False

def make(i,List,pos):
    for word in num[pos:]:


for test in range(1,T+1):
    n,m = tuple(map(int,input().rstrip().split()))
    num = input().rstrip()
    count = 0
    Len = len(num)
    for i in range(Len,0,-1):
        a = 0
        b = 0
        for j in range(0,Len):
            a +=1
            number = num[j:j+i]
            print(number)
            ans = divide(number,m)
            if ans:
                b +=1
        if a == b:
            count +=1
    print(count)







