import sys

sys.stdin = open("input.txt", "r")

A,B = tuple(map(int,sys.stdin.readline().rstrip().split()))

a_list = []
for a in str(A):
    a_list.append(a)
a_list.sort(reverse=True)

if len(str(B)) < len(str(A)):
    print(-1)
elif len(str(B)) > len(str(A)):
    print(int("".join(a_list)))
else:
    for j in range(len(str(A))):
        a_index = [0 for i in range(len(a_list))]
        ans = ""
        ans += a_list[j]
        a_index[j] = 1
        stop = 0
        if int(a_list[j]) > int(str(B)[0]):
            continue
        for i in range(1,len(str(B))):
            b = int(str(B)[i])
            index = 0
            while True:
                if a_index[index] == 0:
                    a = int(a_list[index])
                    if b >=a:
                        ans += str(a)
                        a_index[index] = 1
                        break
                    else:
                        index +=1
                else:
                    index+=1
                if index >= len(str(A)):
                    stop +=1
                    break
            if stop > 0:
                break
        if len(ans) == len(str(A)):
            break
        else:
            ans = -1
    if len(ans) != len(str(A)):
        ans = -1

    print(int(ans))