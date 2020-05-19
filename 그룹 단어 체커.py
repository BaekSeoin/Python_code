import sys

sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())

count = 0

for i in range(n):
    text = [i for i in sys.stdin.readline().rstrip()]
    check = []
    current_text = text[0]

    if len(text) == 1:
        count +=1
        continue

    for index,j in enumerate(text):
        if index == 0:
            check.append(current_text)
        else:
            if (index == (len(text) - 1)) and ((j not in check) or j == current_text):
                count += 1
            elif j == current_text:
                continue
            else:
                if j in check:
                    break
                else:
                    current_text = j
                    check.append(current_text)
print(count)
