import sys

sys.stdin = open("input.txt","r")

M,N = (sys.stdin.readline().rstrip().split())

List = [i for i in range(int(M),int(N)+1)]


for i in List:
    if i > 2:
        for j in range(len(List)):
            if List[j] != i and List[j] % i == 0:
                List[j] = 0



