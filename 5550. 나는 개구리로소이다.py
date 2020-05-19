import sys

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

find = {'c':0,'r':1,'o':2,'a':3,'k':4}

for test in range(1,T+1):
    text = 'croak'
    word = input().rstrip()
    ans = 0
    List = [0]
    for cur_index in range(len(word)):
        current_state = word[cur_index]
        end = 0
        new_List = []
        for index,check_index in enumerate(List):
            if text[check_index] == current_state:
                end = 1
            if List[index] + 1 < len(text)-1:
                new_List.append(List[index]+1)
        if end == 0:
            if find[current_state] + 1 < len(text)-1:
                new_List.append(find[current_state]+1)
                if len(new_List) > ans:
                    ans = len(new_List)
            else:
                if len(new_List) + 1 > ans:
                    ans = len(new_List)
        else:
            if len(new_List) > ans:
                ans = len(new_List)
        List = new_List
    print('#'+str(test),end=' ')
    print(ans)
