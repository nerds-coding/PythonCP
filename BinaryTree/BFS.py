class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def insert(root, key):
    if (root is None):
        return Node(key)
    else:
        if(root.data == key):
            return root
        elif(root.data > key):
            root.left = insert(root.left, key)
        elif(root.data < key):
            root.right = insert(root.right, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def bfs(root):
    if root:
        q = [root]
        while q:
            d = q.pop(0)
            print(d.data, end=' ')
            if (d.left):
                q.append(d.left)
            if (d.right):
                q.append(d.right)
            print()


root = Node(5)
root = insert(root, 1)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 4)
root = insert(root, 5)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 8)
root = insert(root, 9)
root = insert(root, 0)


# inorder(root)

bfs(root)
