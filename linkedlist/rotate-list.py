def rotateList(head, k):
    if k == 0:
        return head

    l = 0
    it = head
    while it is not None:
        l += 1
        it = it.next

    k = k % l

    start = 0
    it = head

    head_node = None
    while start < k:
        it = it.next
        start += 1

    head_node = it
    head_iter = head_node

    while head_iter.next is not None:
        head_iter = head_iter.next

    head_iter.next = head
    while k > 0:
        head_iter = head_iter.next
        k -= 1
    head_iter.next = None

    return head_node
