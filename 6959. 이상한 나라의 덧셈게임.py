import sys
sys.stdin = open("input.txt","r")

T = int(input())

for i in range(T):
    number = input().rstrip()
    count = 0

    if len(number) == 1:
        print('#',end='')
        print(i+1, end=' ')
        print('B')
        continue

    while True:
        if len(number) == 1:
            print('#',end='')
            print(i+1,end = ' ')
            if count%2 == 0:
                print('B')
            else:
                print('A')
            break

        a = int(number[0])
        b = int(number[1])
        Sum = a+b
        number = str(Sum) + number[2:]
        count += 1