class Node:

    def __init__(self, val):
        self.left = None
        self.value = val
        self.right = None


root = Node(1)

node1 = Node(2)
node2 = Node(3)
node3 = Node(4)


root.left = node1
root.right = node2


node1.left = node3
