import sys

sys.setrecursionlimit(1500)

sys.stdin = open("input.txt", "r")


def getLine():
    return sys.stdin.readline().rstrip()


def longest_sub_seq(arr, n):
    maxi = 1
    for i in range(n + 1, len(arr)):
        if arr[n] < arr[i]:
            maxi = max(maxi, 1 + longest_sub_seq(arr, i))

    return maxi


N = int(getLine())
arr = list(map(int, getLine().split()))

print(longest_sub_seq(arr, 0))
