class Node:

    def __init__(self, data=None):
        self.value = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def IteratingValues(self):
        tmp = self.head

        while tmp:
            print(tmp.value)
            tmp = tmp.next

    def InsertingAtTail(self, data):
        if(self.head is None):
            self.head = Node(data)
            return
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = Node(data)


ll = LinkedList()
ll.InsertingAtTail(9)
#ll.head = Node(3)
el1 = Node(4)
el2 = Node(5)
el3 = Node(6)

ll.head.next = el1
el1.next = el2
el2.next = el3

ll.InsertingAtTail(9)

ll.IteratingValues()
