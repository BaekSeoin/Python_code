import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

cal = [i for i in sys.stdin.readline().rstrip()]

total_max = int(cal[0])

List = []

for i in range(len(cal)-2):
    if i % 2 == 0:
        num = int(cal[i])
        opr = cal[i+1]
        next_num = int(cal[i+2])
        if opr == '+':
            ans = num + next_num
            total_max += next_num
        elif opr == '*':
            ans = num*next_num
            total_max *= next_num
        else:
            ans = num - next_num
            total_max -= next_num

        List.append(ans)
        List.append(0)

def calculate(a,b,c):
    if c == '+':
        ans = a+b
    elif c == '*':
        ans = a*b
    else:
        ans = a - b
    return ans

def dfs(total,index,prev_opr):
    global total_max
    if index > len(cal)-1:
        total_max = max(total_max,total)
        return

    for i in range(2):
        if i == 0:
            if index != len(cal)-1:
                num = List[index]
                total_b = calculate(total,num,prev_opr)
                try:
                    next_opr = cal[index + 3]
                except:
                    next_opr = '+'
                dfs(total_b,index+4,next_opr)

        if i == 1:
            num = int(cal[index])
            total_a = calculate(total, num, prev_opr)
            try:
                next_opr = cal[index + 1]
            except:
                next_opr = '+'
            dfs(total_a, index + 2, next_opr)


dfs(0,0,'+')
print(total_max)

