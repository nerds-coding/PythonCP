class Node:

    def __init__(self, val):
        self.left = None
        self.value = val
        self.right = None


def insert(root, value):
    if(root is None) or root.value == value:
        return root

    if(root.value < value):
        if(root.right is None):
            root.right = Node(value)
        else:
            insert(root.right, value)
    else:
        if(root.left is None):
            root.left = Node(value)
        else:
            insert(root.left, value)


def InsertIntoBinaryTree(root, value):

    if(root is None):
        return root

    if(root.right is None) and (root.left is not None):
        root.right = Node(value)
        return root

    if(root.left is None)and (root.right is not None):
        root.left = Node(value)
        return root

    if(root.value < value):
        InsertIntoBinaryTree(root.right, value)
    else:
        InsertIntoBinaryTree(root.left, value)


def InorderTraversal(root):
    if(root):
        InorderTraversal(root.left)
        print(root.value)
        InorderTraversal(root.right)


root = Node(60)
insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)


InsertIntoBinaryTree(root, 100)
InorderTraversal(root)
