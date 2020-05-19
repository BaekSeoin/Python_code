import sys

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

def type_1(index, a,b):
    A[index] = a
    B[index] = b
    List[index] = True

def type_2(i_th):
    A[i_th] = 0
    B[i_th] = 0
    List[i_th] = False

def type_3(x):
    new_dict = dict()
    Max_ans = 0
    for id,value in List.items():
        if value:
            new_dict[id] = True
            a = A[id]
            b = B[id]
            ans = a*x + b
            if ans > Max_ans:
                Max_ans = ans
    if Max_ans == 0:
        print("NO")
        return List
    else:
        print(Max_ans)
        return new_dict

for test in range(1,T+1):
    print('#' + str(test))
    N = int(input().rstrip())

    A = [0 for i in range(N+1)]
    B = [0 for i in range(N+1)]

    List = dict()

    for index, n in enumerate(range(N)):
        line = [int(i) for i in input().rstrip().split()]
        if line[0] == 1:
            type_1(index+1, line[1], line[2])
        elif line[0] == 2:
            type_2(line[1])
        else:
            List = type_3(line[1])
