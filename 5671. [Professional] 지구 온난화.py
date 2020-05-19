import sys
import copy

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

def pick_alphabet(M,possible_alphabet_list,index):
    if len(possible_alphabet_list) == M:
        final_possible_alphabet_list.append(copy.deepcopy(possible_alphabet_list))
        return

    for i in range(index+1,len(alphabet_List)):
        if (i != index) and (alphabet_List[i] not in possible_alphabet_list):
            possible_alphabet_list.append(alphabet_List[i])
            pick_alphabet(M,possible_alphabet_list,i)
            possible_alphabet_list.pop()

for test in range(1,T+1):
    N,M = tuple(map(int, input().rstrip().split()))
    words = []
    alphabet_List = {0: 'c', 1: 'd', 2: 'f', 3: 'g', 4: 'h', 5: 'j', 6: 'k', 7: 'l', 8: 'n', 9: 'm', 10: 'p', 11: 'q',
                     12: 'r',13: 's', 14: 't', 15: 'u', 16: 'v', 17: 'w', 18: 'x', 19: 'y', 20: 'z'}
    possible_alphabet_list = []
    final_possible_alphabet_list = []
    for i in range(N):
        word = input().rstrip()
        words.append(word)
    pick_alphabet(M,possible_alphabet_list,-1)
    Max_count = 0

    for alpha_list in final_possible_alphabet_list:
        count = 0
        for word in words:
            for num,w in enumerate(word):
                if w not in alpha_list:
                    break
                elif (w in alpha_list) and ((num +1) == len(word)):
                    count += 1
                else:
                    continue
        if count > Max_count:
            Max_count = count
        if Max_count == len(words):
            break
    print('#'+str(test),end=' ')
    print(Max_count)

