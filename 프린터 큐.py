import sys
from collections import deque

sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline().rstrip())

for test in range(1,T+1):
    N,doc = tuple(map(int,sys.stdin.readline().rstrip().split()))
    print_doc = deque()
    print_importance = deque()

    for index, i in enumerate(sys.stdin.readline().rstrip().split()):
        print_doc.append(index)
        print_importance.append(i)

    final_print_list= [-1 for i in range(N)]
    order = 1
    while print_doc:
        if max(print_importance) == print_importance[0]:
            current_doc = print_doc.popleft()
            current_importance = print_importance.popleft()
            final_print_list[current_doc] = order
            order +=1
            if current_doc == doc:
                break
        else:
            current_doc = print_doc.popleft()
            print_doc.append(current_doc)
            current_importance = print_importance.popleft()
            print_importance.append(current_importance)

    print(final_print_list[doc])
