import sys

sys.stdin = open("input.txt","r")

class Node():
    def __init__(self,start, end):
        self.start = start
        self.end = end
        self.data = sum(lst[self.start:self.end+1])
        self.left = None
        self.right = None

        if self.start < self.end:
            Sum = self.start + self.end
            if Sum % 2 == 0:
                self.mid = Sum // 2 - 1
            else:
                self.mid = Sum // 2
            self.left = Node(self.start,self.mid)
            self.right = Node(self.mid+1, self.end)

    def modify(self, a, b, c):
        for i in range(a,b+1):
            if (self.start <= i <= self.end):
                self.data += c
        if self.left != None: self.left.modify(a,b,c)
        if self.right != None: self.right.modify(a, b, c)

    def Print(self,a,b):
        ans = 0
        if (a == self.start) and (b == self.end):
            ans = self.data
        else:
            if (b <= self.mid):
                ans += self.left.Print(a,b)
            elif (a > self.mid):
                ans += self.right.Print(a,b)
            elif (a <= self.mid) and (b > self.mid):
                ans += self.left.Print(a,self.mid)
                ans += self.right.Print(self.mid+1,b)

        return ans


N,M,K = map(int, sys.stdin.readline().rstrip().split())

lst = [int(sys.stdin.readline().rstrip()) for i in range(N)]

order = [sys.stdin.readline().rstrip().split() for j in range(M+K)]

root = Node(0,len(lst)-1)

store = []

for o in order:
    if o[0] == '1':
        a,b,c = int(o[1])-1,int(o[2])-1,int(o[3])
        store.append((a, b, c))
        #root.modify(a,b,c)

    elif o[0] == '2':
        for j in store:
            a,b,c = j[0], j[1], j[2]
            root.modify(a,b,c)
        store = []
        a,b = int(o[1])-1,int(o[2])-1
        print(root.Print(a,b))


