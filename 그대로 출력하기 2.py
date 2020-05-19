import sys

sys.stdin = open("input.txt","r")

text = sys.stdin.read().split("\n")

for i in text:
    print(i)