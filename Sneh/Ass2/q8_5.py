tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [None, None],
    'D': [None, None],
    'E': [None, None]
}

def preorder(node):
    if node is not None:
        print(node,end=" ")
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node is not None:
        inorder(tree[node][0])
        print(node,end=" ")
        inorder(tree[node][1])

def postorder(node):
    if node is not None:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node,end=" ")

print("preorder: ")
preorder('A')

print("\nInorder: ")
inorder('A')

print("\nPostorder: ")
postorder('A')

