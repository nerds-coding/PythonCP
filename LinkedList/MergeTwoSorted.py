class Node:
    def __init__(self, value):
        self.key = value
        self.next = None


def printLinkedList(root):
    while(root):
        print(root.key)
        root = root.next


def SortedMerge(a, b):

    if (a == None and b == None):
        return None

    res = None
    while (a != None and b != None):
        if (a.key <= b.key):
            temp = a.next
            a.next = res
            res = a
            a = temp
        else:

            temp = b.next
            b.next = res
            res = b
            b = temp

    while (a != None):

        temp = a.next
        a.next = res
        res = a
        a = temp

    while (b != None):

        temp = b.next
        b.next = res
        res = b
        b = temp

    return res


root1 = Node(10)
a = Node(12)
b = Node(13)
c = Node(15)
d = Node(19)
e = Node(21)
f = Node(22)
g = Node(23)

root1.next = a
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g


root2 = Node(50)
i = Node(54)
j = Node(55)
k = Node(57)
l = Node(59)
m = Node(60)
n = Node(61)
o = Node(69)
h = Node(80)

root2.next = i
i.next = j
j.next = k
k.next = l
l.next = m
m.next = n
n.next = o
o.next = h


printLinkedList(SortedMerge(root1, root2))
