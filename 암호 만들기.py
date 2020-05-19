import sys
sys.stdin = open("input.txt","r")

L, C = map(int,sys.stdin.readline().rstrip().split())

text = [i for i in sys.stdin.readline().rstrip().split()]

text.sort()
List = []
A = []

ae = ['a','e','i','o','u']
ae_cnt = 0
ce_cnt = 0

def dfs(A,i):
    global ae_cnt, ce_cnt
    if len(A) == L:
        for j in A:
            if j in ae:
                ae_cnt += 1
            else:
                ce_cnt +=1
        if 1 <= ae_cnt and 2<= ce_cnt:
            print("".join(A))
        ae_cnt = 0
        ce_cnt = 0
        return

    if i <= C-1:
        A.append(text[i])
        dfs(A,i+1)
        A.pop()

        dfs(A,i+1)

dfs(A,0)





