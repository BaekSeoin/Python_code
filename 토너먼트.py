import sys

sys.stdin = open("input.txt", "r")

N,kim, lim = tuple(map(int,sys.stdin.readline().rstrip().split()))

game = [int(i) for i in range(1,N+1)]

Round = 0
end = 0
while True:
    new_game = []
    Len = len(game)
    Round +=1
    for num in range(0,Len-1,2):
        player_1 = game[num]
        player_2 = game[num+1]
        if (player_1 != kim) and (player_1 != lim) and (player_2 != kim) and (player_2!= lim):
            new_game.append(player_1)
        elif (player_1 == kim or player_2 == kim) and (player_1 !=lim and player_2!=lim):
            new_game.append(kim)
        elif (player_1 == lim or player_2 == lim) and (player_1 !=kim and player_2 != kim):
            new_game.append(lim)
        elif (player_1 == kim or player_1 == lim) and (player_2 == kim or player_2 == lim):
            print(Round)
            end = 1
            break
    if end == 1:
        break
    if Len % 2 == 1:
        new_game.append(game[-1])
    game = new_game