import sys

sys.stdin = open('input.txt','r')

M,N = map(int,sys.stdin.readline().rstrip().split())

number = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}

keys = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
box = []

for num in range(M,N+1):
    if num < 10:
        ans = number[num]
    else:
        x = str(num)
        a = number[int(x[0])]
        b = number[int(x[1])]
        ans = a + " " + b
    box.append(ans)
box.sort()

maxIndex = len(box) - 1

for index,num in enumerate(box):
    x = num.split()
    ans = ""
    for i in x:
        ans += str(keys[i])
    ans = int(ans)

    if (index+1) % 10 != 0:
        print(ans, end=" ")
    else:
        print(ans)


