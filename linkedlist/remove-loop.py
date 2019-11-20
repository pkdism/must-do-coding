def removeTheLoop(head):
    h = set()
    prev = None
    it = head
    while it is not None:
        if it in h:
            prev.next = None
            break
        h.add(it)
        prev = it
        it = it.next
