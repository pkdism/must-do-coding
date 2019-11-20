def getNthfromEnd(head,n):
    l = 0
    it = head
    while it is not None:
        l += 1
        it = it.next
    k = l - n
    if k < 0:
        return -1
    it = head
    while k > 0:
        it = it.next
        k -= 1
    return it.data
