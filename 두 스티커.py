import sys
import copy

sys.stdin = open("input.txt", "r")

H,W = tuple(map(int,sys.stdin.readline().rstrip().split()))
N = int(sys.stdin.readline().rstrip())

sticker = []

for i in range(N):
    a,b = sys.stdin.readline().rstrip().split()
    sticker.append((int(a),int(b)))

lst_of_sticker = []

List = []
def dfs(List, index):
    if len(List) == 2:
        lst_of_sticker.append(copy.deepcopy(List))
        return
    for i in range(index+1,N):
        List.append(sticker[i])
        dfs(List,i)
        List.pop()
dfs(List,-1)

def check(st1,st2,board):
    ans = 0
    for row in range(st1[0]):
        for col in range(st1[1]):
            try:
                board[row][col] = 1
                ans +=1
            except:
                return (False,0)
    for row in range(H-1,H - st2[0]-1,-1):
        for col in range(W-1,W-st2[1]-1,-1):
            try:
                if board[row][col] !=1:
                    board[row][col] = 1
                    ans +=1
                else:
                    return (False,0)
            except:
                return (False,0)
    return (True,ans)
board = [[0 for i in range(W)] for j in range(H)]

Max_count = 0
for st1,st2 in lst_of_sticker:
    value = st1[0] * st1[1] + st2[0] * st2[1]
    if value <= Max_count:
        continue
    st1_change = (st1[1],st1[0])
    st2_change = (st2[1],st2[0])
    ans1,ans2,ans3,ans4 = 0,0,0,0
    case1,ans1 = check(st1,st2,copy.deepcopy(board))
    if not case1:
        case2,ans2 = check(st1,st2_change,copy.deepcopy(board))
        if not case2:
            case3,ans3 = check(st1_change,st2,copy.deepcopy(board))
            if not case3:
                case4,ans4 = check(st1_change,st2_change,copy.deepcopy(board))
    Max_count = max(Max_count,ans1,ans2,ans3,ans4)
print(Max_count)