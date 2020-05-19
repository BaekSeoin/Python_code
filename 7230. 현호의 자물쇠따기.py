import sys
import copy

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

def dfs(number_list, index,check):
    if len(number_list) == N:
        if int(number_list[-1]) % 2 == check:
            final_num_lst.append(copy.deepcopy(number_list))
        return

    for i in range(N):
        if i !=index and str(number[i]) not in number_list:
            number_list.append(str(number[i]))
            dfs(number_list,i,check)
            number_list.pop()

for test in range(1,T+1):
    N = int(input().rstrip())
    number = [int(i) for i in input().rstrip().split()]
    K = int(input().rstrip())
    if K % 2 == 0:
        check = 0
    else:
        check = 1
    number_list=[]
    final_num_lst = []
    dfs(number_list,-1,check)
    ans = 0

    for num in final_num_lst:
        num = "".join(num)

        if int(num) % K == 0:
            ans +=1
    print('#'+str(test),end=' ')
    print(ans)