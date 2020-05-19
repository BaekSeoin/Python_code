import sys

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

num = '0123456789'

def num_check(name):
    for i in name:
        if i in num:
            return True
    return False

def check(name):
    if num_check(name):
        return False
    elif name[0] == name[0].upper():
        if name[1:] == name[1:].lower():
            return True
        else:
            return False
    else:
        return False

for test in range(1,T+1):
    N = int(input().rstrip())
    sentence = input().rstrip()
    sentence = sentence.replace('!','.').replace('?','.').split('.')[:-1]
    print('#'+str(test),end=' ')
    n = 1
    for st in sentence:
        st = st.split()
        count = 0
        for name in st:
            ans = check(name)
            if ans:
                count +=1
        if n != N:
            print(count,end=' ')
            n +=1
        else:
            print(count)



