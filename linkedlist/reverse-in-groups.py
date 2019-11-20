def reverse(head, k):
    if head is None:
        return None
    prev, curr, nxt = None, head, None
    i = 0
    while i < k and curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        i += 1
    if curr is not None:
        head.next = reverse(nxt, k)
    return prev
