class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


def insert(root, value):
    if root is None:
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


def findMinimum(root):
    current = root
    while current.left:
        current = current.left
    return current


def inorder(root):
    if root:
        inorderIteration(root.left)
        print(root.value)
        inorderIteration(root.right)


def deletingElements(root, value):
    if root is None:
        return root

    if(root.value < value):
        root.right = deletingElements(root.right, value)
    elif(root.value > value):
        root.left = deletingElements(root.left, value)
    else:
        if(root.right is None):
            temp = root.left
            root = temp
            return root
        else:
            temp = root.right
            root = temp
            return root

        temp = findMinimum(root.right)

        root.value = temp.value

        root.right = deletingElements(root.right, temp.value)


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = deletingElements(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 30")
root = deletingElements(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 50")
root = deletingElements(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)
