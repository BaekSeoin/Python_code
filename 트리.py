import sys

sys.stdin = open("input.txt","r")


class Node():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

class Tree():
    def __init__(self,root,d,node):
        self.root = root
        self.d = d
        self.node = node

    def preorder(self, data):
        cur = node[d[data]]
        print(cur.data, end='')
        if cur.left != None: self.preorder(cur.left)
        if cur.right != None: self.preorder(cur.right)

    def inorder(self, data):
        cur = node[d[data]]
        if cur.left != None: self.inorder(cur.left)
        print(cur.data, end = '')
        if cur.right != None: self.inorder(cur.right)

    def postorder(self, data):
        cur = node[d[data]]
        if cur.left != None: self.postorder(cur.left)
        if cur.right != None: self.postorder(cur.right)
        print(cur.data, end='')




n = int(sys.stdin.readline().rstrip())
node = [Node() for i in range(n)]

root = 'A'

d = dict()

for idx,i in enumerate(range(n)):
    cur, left, right = map(str, sys.stdin.readline().rstrip().split())
    node[idx].data = cur
    d[cur] = idx
    if left != '.':
        node[idx].left = left
    if right != '.':
        node[idx].right = right


x = Tree(root,d,node)
x.preorder(root)
print()
x.inorder(root)
print()
x.postorder(root)

