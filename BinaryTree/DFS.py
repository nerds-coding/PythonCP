class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, val):
    if(not(root)):
        return Node(val)
    else:
        if(root.data == val):
            return root
        elif(root.data > val):
            root.left = insert(root.left, val)
        elif(root.data < val):
            root.right = insert(root.right, val)
    return root


def inorder(root):

    if (root):
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def dfs(root):
    if root:
        temp = [root]
        stack = list()
        while temp:
            m = temp.pop(0)
            stack.append(m)
            if(m.left):
                temp.append(m.left)
            if(m.right):
                temp.append(m.right)

        for x in stack[::-1]:
            print(x.data)


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

dfs(root)
