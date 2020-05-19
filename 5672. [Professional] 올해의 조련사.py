import sys

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

def compare(start,end):
    start_al = names[start]
    end_al = names[end]
    if start_al < end_al:
        return start_al, start
    elif start_al == end_al and start!=end:
        next_start_al = names[start +1]
        next_end_al = names[end - 1]
        if next_start_al <= next_end_al:
            return start_al, start
        else:
            return end_al, end
    else:
        return end_al, end

for test in range(1,T+1):
    N = int(input().rstrip())
    names = [input().rstrip() for i in range(N)]
    len_names = len(names)
    start = 0
    end = len_names-1
    lst = ''
    for i in range(len_names):
        alpha, index = compare(start,end)
        lst += alpha
        if index == start:
            start +=1
        else:
            end -=1
    print('#'+str(test),end=' ')
    print(lst)
