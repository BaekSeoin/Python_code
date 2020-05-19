import sys

sys.stdin = open('input.txt','r')

T = int(sys.stdin.readline().rstrip())

def inRange(a,b):
    if (0<=a<65536) and (0<=b<65536):
        return True
    return False

def bfs(List):
    while List:
        cur = List.popleft()


for t in range(T):
    numOfConvenienceStore = int(sys.stdin.readline().rstrip())

    Map = [[0 for i in range(65536)] for j in range(65536)]
    visit = [[0 for i in range(65536)] for j in range(65536)]

    home = tuple([int(i) + 32768 for i in sys.stdin.readline().rstrip().split()])
    for i in range(numOfConvenienceStore):
        a,b = map(int,sys.stdin.readline().rstrip().split())
        Map[a+32768][b + 32768] = 'c'

    festival = tuple([int(i) + 32768 for i in sys.stdin.readline().rstrip().split()])

