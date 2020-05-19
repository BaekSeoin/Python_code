import sys

sys.stdin = open("input.txt","r")

A = [int(i) for i in sys.stdin.readline().rstrip().split()]

count = 0

def solution(A):
    global count
    bulb = [False for i in range(len(A))]
    check = [False for p in range(len(A))]

    for j in A:
        if j == 1:
            bulb[j-1] = True
            check[j-1] = True
            count +=1
            for index in range(j,len(A)):
                if check[index]== True:
                    bulb[index] = True
                else:
                    break
        else:
            if bulb[j-2] == True:
                bulb[j-1] = True
                check[j-1] = True
                count +=1
                for index in range(j,len(A)):
                    if check[index] == True:
                        bulb[index] = True
                    else:
                        break
            else:
                check[j-1] = True

    return count

print(solution(A))