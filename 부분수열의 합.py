import sys
sys.stdin = open("input.txt","r")

N, S = map(int,sys.stdin.readline().rstrip().split())

numbers = list(map(int,sys.stdin.readline().rstrip().split()))


cnt = 0
depth = 0
List = []

def cntSet(List, depth):
    global cnt
    if N == depth:
        if len(List) > 0 and sum(List) == S:
            cnt +=1
        return


    List.append(numbers[depth])
    cntSet(List, depth+1)
    List.pop()

    cntSet(List, depth+1)

cntSet(List, depth)

print(cnt)



    