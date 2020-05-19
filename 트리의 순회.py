import sys

sys.stdin = open("input.txt","r")
sys.setrecursionlimit(10000000)

T = int(sys.stdin.readline().rstrip())

def solve(in_start,in_end, pre_start, pre_end):
    global ans
    if (in_start > in_end) or (pre_start > pre_end): return
    root = preorder[pre_start]
    ans += str(root) + " "
    p = pos[root]
    left = p - in_start
    solve(in_start,p-1,pre_start, pre_start+left-1)
    solve(p + 1, in_end, pre_start + left, pre_end - 1)


for test in range(T):
    n = int(sys.stdin.readline().rstrip())

    inorder = [int(i) for i in sys.stdin.readline().rstrip().split()]
    preorder = [int(i) for i in sys.stdin.readline().rstrip().split()]

    pos = [0 for i in range(n+1)]

    for i in range(n):
        pos[inorder[i]] = i

    ans = ""
    solve(0,n-1,0,n-1)
    print(ans.strip())
