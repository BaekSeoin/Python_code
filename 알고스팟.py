import sys
import copy
import heapq

sys.stdin = open('input.txt','r')

M,N = map(int, sys.stdin.readline().rstrip().split())

board = [[i for i in sys.stdin.readline().rstrip()] for j in range(N)]

roomCount = 0
roomNumber = dict()
for i in range(N):
    for j in range(M):
        if board[i][j] == '1':
            roomCount +=1
            roomNumber[roomCount] = (i,j)

map = []
for i in range():
    newMap = []
    for j in range(roomCount):
        newMap.append(copy.deepcopy(board))
    map.append(newMap)

print(len(map[0]))

visit = [[[0 for i in range(M)] for j in range(N)] for k in range(roomCount+1)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]

start = (0,0)
end = (N-1,M-1)

def inRange(a,b):
    if (0<=a<N) and (0<=b<M):
        return True
    return False

def bfs(List):
    global roomCount, TotalCount
    while List:
        x = heapq.heappop(List)
        count = x[0]
        cur = x[1]
        crush_num = x[2]
        crush = crush_storage[crush_num]

        if cur == end:
            break

        for dir in direction:
            nextPos = (cur[0] + dir[0], cur[1] + dir[1])
            if inRange(nextPos[0],nextPos[1]):
                if (map[nextPos[0]][nextPos[1]] == '0') and (visit[count][nextPos[0]][nextPos[1]]==0):
                    visit[count][nextPos[0]][nextPos[1]] = 1
                    heapq.heappush(List, (count, nextPos, crush_num))
                elif (visit[count][nextPos[0]][nextPos[1]]==0) and (nextPos in crush):
                    visit[count][nextPos[0]][nextPos[1]] = 1
                    heapq.heappush(List, (count, nextPos, crush_num))
                elif (count < roomCount) and (map[nextPos[0]][nextPos[1]] == '1') and (visit[count+1][nextPos[0]][nextPos[1]]==0):
                    if nextPos not in crush:
                        crush.append(nextPos)
                        crush.sort()
                        crush = tuple(crush)
                        try:
                            x = crush_check[crush]
                            crush = list(crush)
                            heapq.heappush(List, (count + 1, nextPos, x))
                        except:
                            crush_check[crush] = TotalCount
                            crush = list(crush)
                            crush_v = copy.deepcopy(crush)
                            crush_storage[TotalCount] = crush_v
                            del crush_v
                            heapq.heappush(List, (count+1, nextPos, TotalCount))
                            TotalCount +=1
                        visit[count + 1][nextPos[0]][nextPos[1]] = 1
                        crush.remove(nextPos)

List = []
crush_storage = dict()
crush_storage[1] = []
crush_check = dict()
TotalCount = 2
heapq.heappush(List,(0,start,1))

bfs(List)


for k in range(roomCount+1):
    if visit[k][end[0]][end[1]] != 0:
        print(k)
        break