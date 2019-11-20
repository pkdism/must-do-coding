def findMid(head):
    slow, fast = head, head
    while fast.next is not None:
        fast = fast.next
        if fast.next is not None:
            fast = fast.next
        slow = slow.next
    return slow
