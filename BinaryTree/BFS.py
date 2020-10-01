class Node:

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def insert(root, value):
    if(not(root))or (root.data == value):
        return root
    else:
        if(root.data > value):
            if(not(root.left)):
                root.left = Node(value)
            else:
                insert(root.left, value)
        else:
            if(not(root.right)):
                root.right = Node(value)
            else:
                insert(root.right, value)


def inorder(root):
    if(root):
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def bfs(root):
    if(not(root)):
        return root
    q = [root]
    while(len(q) > 0):
        node = q.pop(0)

        if(node.left):
            q.append(node.left)
        if(node.right):
            q.append(node.right)
    for m in node:
        print(m.data)


root = Node(5)
insert(root, 1)
insert(root, 2)
insert(root, 3)
insert(root, 4)
insert(root, 5)
insert(root, 6)
insert(root, 7)
insert(root, 8)
insert(root, 9)
insert(root, 0)


# inorder(root)

bfs(root)
