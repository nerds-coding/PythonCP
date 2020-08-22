class Node:

    def __init__(self, data=None):
        self.value = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def IteratingValues(self, head):
        tmp = head

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

    def InsetingAtPosition(self, head, data, position):
        if(head is None):
            head.value = data
            return
        else:
            temp = head
            while(temp):
                if(temp == position):
                    break
                temp = temp.next
            prev = temp
            next = temp.next
            m = Node(data)
            m.next = next
            prev.next = m

    def reverse(self, head):
        if head is None:
            return None

        prev = None
        curr = head
        aux = head.next
        while curr is not None:
            curr.next = prev
            prev = curr
            curr = aux
            if curr is not None:
                aux = aux.next
        return prev

    def mergeLists(self, head1, head2):
        if(head1 == None and head2 == None):
            return None
        head = None
        h = list()
        while(head1):
            h.append((head1.data, head1))
            head1 = head1.next
        while(head2):
            h.append((head2.data, head2))
            head2 = head2.next
        h = sorted(h, key=lambda x: x[0])

        head = h[0][1]
        for index in range(len(h)-1):
            h[index][1].next = h[index+1][1]

        return head

    def removeDuplicates(self, head):
        if head:
            node = head
            while node.next:
                if node.data == node.next.data:
                    node.next = node.next.next
                else:
                    node = node.next
        return head


ll = LinkedList()
ll.InsertingAtTail(9)
#ll.head = Node(3)
el1 = Node(4)
el2 = Node(5)
el3 = Node(6)

ll.head.next = el1
el1.next = el2
el2.next = el3

ll.InsetingAtPosition(ll.head, 99, el2)
ll.InsertingAtTail(9)


m = ll.reverse(ll.head)
# ll.IteratingValues(m)
