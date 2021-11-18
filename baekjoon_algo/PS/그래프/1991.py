import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

# https://ko.wikipedia.org/wiki/%ED%8A%B8%EB%A6%AC_%EC%88%9C%ED%9A%8C 트리순회

def preorder(v):  # 전위 순회
    if v != '.':
        print(v, end='')
        preorder(tree[v][0])
        preorder(tree[v][1])

def inorder(v):  # 중위 순회
    if v != '.':
        inorder(tree[v][0])
        print(v, end='')
        inorder(tree[v][1])

def postorder(v): # 후위 순회
    if v != '.':
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(v, end='')


tree = {}
for _ in range(int(input())):
    node = list(input().split())
    tree[node[0]] = [node[1], node[2]]

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()