class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self, head):
        self.head = head

    def IteratingList(self, head):
        while(head):
            print(head.data)
            head = head.prev

    def sortedInsert(self, head, data):
        node = DoublyLinkedListNode(data)
        if (head == None):
            return node
        elif (data < head.data):
            node.next = head
            head.prev = node
            return node
        else:
            node = sortedInsert(head.next, data)
            head.next = node
            node.prev = head
            return head

    def reverse(self, head):
        if(head is None):
            return None
        else:
            prev = None
            cur = head
            nxt = head.next
            while (cur):
                cur.next = prev
                prev = cur
                cur = nxt
                if(cur is not None):
                    nxt = nxt.next
            return prev


dll = DoublyLinkedList(Node(2))
d1 = Node(3)
d2 = Node(99)
d3 = Node(4)
d4 = Node(6)
d5 = Node(8)

dll.head.next = d1

d1.next = d2
d1.prev = dll.head

d2.next = d3
d2.prev = d1

d3.next = d4
d3.prev = d2

d4.next = d5
d4.prev = d3

d5.prev = d4

dll.IteratingList(d5)
