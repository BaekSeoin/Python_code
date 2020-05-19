import sys

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

def dfs(coupon_cost,game_machine_cost,List):
    global min_cost

    for index,c in enumerate(coupon):
        if List[index] == 0:
            coupon_cost += c[0]
            game_machine_cost *= 0.01 * (100-c[1])
            List[index] = 1
            total = coupon_cost + game_machine_cost
            if total < min_cost:
                min_cost = total
                dfs(coupon_cost,game_machine_cost,List)
            coupon_cost -=c[0]
            game_machine_cost //= 0.01 * (100-c[1])
            List[index] = 0

for test in range(1,T+1):
    #쿠폰 개수, 게임기의 기존 가격
    N, C = tuple(map(int,input().rstrip().split()))
    coupon = []
    for i in range(N):
        #쿠폰의 가격, 쿠폰 할인율
        X,P = tuple(map(int,input().rstrip().split()))
        coupon.append((X,P))
    coupon = sorted(coupon, key = lambda x:(-x[1],x[0]))
    min_cost = C
    List = [0 for i in range(N)]
    dfs(0,C,List)
    print('#'+str(test),end=' ')
    print(min_cost)