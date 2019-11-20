def reverseList(self):
    # Code here
    if self.head is None:
        return None
    prev, curr, nxt = None, self.head, None
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    self.head = prev
