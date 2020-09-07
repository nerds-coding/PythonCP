def removeLoop(head):
    s = set()
    prev = None
    temp = head
    while temp:
        if(temp in s):
            prev.next = None
            break
        s.add(temp)
        prev = temp
        temp = temp.next
