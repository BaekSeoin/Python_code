import sys

sys.stdin = open('input.txt','r')

hamburger_price = [int(sys.stdin.readline().rstrip()) for i in range(3)]
drink_price = [int(sys.stdin.readline().rstrip()) for i in range(2)]

ans = min(hamburger_price) + min(drink_price)

print(ans - 50)
