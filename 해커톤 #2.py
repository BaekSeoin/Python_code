import sys
import copy
from collections import deque

sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline().rstrip())

def solution(N):
    number1 = deque()
    number1.append(1)
    number1.append(1)
    if N == 1:
        return 2

    for i in range(N-1):
        number2 = copy.deepcopy(number1)
        number2.append(0)
        Ans = deque()
        carryout = 0
        for j in reversed(number2):
            if len(number1) !=0:
                b = j + number1.pop() + carryout
                carryout = 0
                if b >=10:
                    carryout = 1
                    b -= 10
            else:
                b = j + carryout
                carryout = 0
            Ans.appendleft(b)

        number1 = Ans

    one_count = 0
    print(Ans)

    for k in Ans:
        if k == 1:
            one_count +=1
    return one_count

print(solution(N))