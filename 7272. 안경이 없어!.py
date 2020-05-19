import sys

sys.stdin = open("input.txt","r")

T = int(input())

non_hole = ['C','E','F','G','H','I','J','K','L','M','N','S','T','U','V','W','X','Y','Z']
hole = ['A','D','O','P','Q','R']

for i in range(1,T+1):
    test_A, test_B = tuple(map(str, input().split()))
    count = 0
    for j in range(len(test_A)):
        if len(test_A) != len(test_B):
            print('#', end='')
            print(i, end=' ')
            print("DIFF")
            break

        if test_A[j] in non_hole and test_B[j] in non_hole:
            count += 1
        elif test_A[j] in hole and test_B[j] in hole:
            count += 1
        elif test_A[j] == 'B' and test_B[j] == 'B':
            count += 1
        else:
            print('#',end='')
            print(i,end = ' ')
            print("DIFF")
            break
    if count == len(test_A):
        print('#',end='')
        print(i,end = ' ')
        print("SAME")




