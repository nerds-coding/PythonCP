class Node:

    def __init__(self, val):
        self.left = None
        self.value = val
        self.right = None


def insert(root, val):
    if(root is None or root.value == val):
        return root

    if(root.value < val.value):
        if(root.right is None):
            root.right = val
        else:
            insert(root.right, val)
    else:
        if(root.left is None):
            root.left = val
        else:
            insert(root.left, val)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

inorder(r)
