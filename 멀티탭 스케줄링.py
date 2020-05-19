import sys

sys.stdin = open("input.txt","r")

n,k = tuple(map(int,sys.stdin.readline().rstrip().split()))

order = [int(i) for i in sys.stdin.readline().rstrip().split()]

on_off = [0 for i in range(k+1)]


count = 0
multitab =0
use = []

for index,i in enumerate(order):
    if multitab < n and i not in use:
        multitab +=1
        use.append(i)

    else:
        if i in use:
            continue
        else:
            last_value = None
            last_index = 0
            for j in use:
                if j not in order[index:]:
                    last_value = j
                    break
                for w,q in enumerate(order[index:]):
                    if q == j:
                        if last_index < w + index:
                            last_index = w + index
                            last_value = q
                        break

            if last_value != None:
                use.remove(last_value)
            else: use.pop()
            count +=1
            use.append(i)

print(count)
