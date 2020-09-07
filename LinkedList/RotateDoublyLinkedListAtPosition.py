def update(llist, p):

    last = llist.head  # finding tail of llist
    while last.next:
        last = last.next

    last.next = llist.head  # making circular
    new_last = last

    for i in range(p):  # shifting new_last and head 'p' position
        new_last = llist.head
        llist.head = llist.head.next

    new_last.next = None  # breaking circular
    return llist
