import sys


sys.stdin = open('input.txt','r')

import heapq
from collections import deque


def solution(priorities, location):
    answer = 0
    indexList = deque(int(i) for i in range(len(priorities)))
    priorities = deque(priorities)

    List = []
    for i in priorities:
        heapq.heappush(List ,-i)

    while True:
        curPrint1 = priorities[0]
        curPrint1Location = indexList[0]
        curPrint2 = heapq.heappop(List)
        curPrint2 = -curPrint2
        print2Index = priorities.index(curPrint2)
        curPrint2Location = indexList[print2Index]

        if (curPrint1 == curPrint2):
            answer +=1
            if curPrint1Location == location:
                break
            else:
                x = priorities.popleft()
                y = indexList.popleft()
        else:
            priorities = list(priorities)
            priorities = priorities[print2Index:] + priorities[:print2Index]
            priorities = deque(priorities)
            indexList = list(indexList)
            indexList = indexList[print2Index:] + indexList[:print2Index]
            indexList = deque(indexList)
            heapq.heappush(List,-curPrint2)

    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))