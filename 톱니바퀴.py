#톱니바퀴
import sys
sys.stdin = open("input.txt","r")

one = [int(i) for i in sys.stdin.readline().rstrip()]
two = [int(i) for i in sys.stdin.readline().rstrip()]
three = [int(i) for i in sys.stdin.readline().rstrip()]
four = [int(i) for i in sys.stdin.readline().rstrip()]

K = int(sys.stdin.readline().rstrip())
test = []

for i in range(K):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    test.append((a,b))

one_Index,two_Index_1, two_Index_2 = 2,6,2
three_Index_1, three_Index_2, four_Index = 6,2,6

def change(direction, a):
    if direction == 1:
        if a > 0:
            a -= 1
        else:
            a = 7
    else:
        if a < 7 :
            a += 1
        else:
            a = 0
    return a


def wheel(a,b,a_index,b_index,i):

    if a[a_index] != b[b_index]:
        a_index = change(i, a_index)
        b_index = change(-i, b_index)
        return a_index, b_index,True
    else:
        a_index = change(i, a_index)
        return a_index, b_index,False


for i in test:
    if i[0] == 1:

        one_Index, two_Index_1,result = wheel(one, two, one_Index,two_Index_1,i[1])
        if result:
            two_Index_2, three_Index_1,result = wheel(two,three, two_Index_2, three_Index_1,-i[1])
            if result:
                three_Index_2, four_Index, result = wheel(three, four, three_Index_2, four_Index,i[1])

    if i[0] == 2:

        two_Index_1, one_Index, result = wheel(two, one, two_Index_1, one_Index,i[1])
        two_Index_2, three_Index_1, result = wheel(two, three, two_Index_2, three_Index_1,i[1])

        if result:
            three_Index_2, four_Index, result = wheel(three, four, three_Index_2, four_Index,-i[1])

    if i[0] == 3:

        three_Index_2, four_Index, result = wheel(three, four, three_Index_2, four_Index,i[1])
        three_Index_1, two_Index_2, result = wheel(three, two, three_Index_1, two_Index_2,i[1])
        if result:
            two_Index_1, one_Index, result = wheel(two,one, two_Index_1, one_Index,-i[1])

    if i[0] == 4:
        four_Index, three_Index_2, result = wheel(four, three, four_Index, three_Index_2,i[1])
        if result:
            three_Index_1, two_Index_2, result = wheel(three,two,three_Index_1, two_Index_2,-i[1])
            if result:
                two_Index_1, one_Index, result = wheel(two, one, two_Index_1, one_Index,i[1])

total = 0

def final(a, a_index,P):
    global total
    if a_index > 1:
        a_index -= 2
        if a[a_index] == 1:
            total += P
    else:
        a_index += 6
        if a[a_index] == 1:
            total += P

final(one, one_Index,1)
final(two, two_Index_2,2)
final(three, three_Index_2,4)

if four_Index < 6:
    four_Index += 2
    if four[four_Index] == 1:
        total += 8
else:
    four_Index -= 6
    if four[four_Index] == 1:
        total += 8

print(total)