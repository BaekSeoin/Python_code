import sys
import copy
from collections import deque

sys.stdin = open("input.txt","r")

def makeList(a,List):
    include = copy.deepcopy(List)
    include.append(a)

    notinclude = copy.deepcopy(List)

    return include, notinclude


while True:
    a = [int(i) for i in sys.stdin.readline().rstrip().split()]
    k, test = a[0], a[1:]
    if k == 0:
        break
    List = deque()
    index = 0
    List.append(([],0))
    while List:
        curNode = List.popleft()

        if len(curNode[0]) == 6:
            print(curNode[0])
            continue

        if curNode[1] == k:
            continue

        a,b = makeList(test[curNode[1]],curNode[0])
        List.append((a,curNode[1]+1))
        List.append((b,curNode[1]+1))
