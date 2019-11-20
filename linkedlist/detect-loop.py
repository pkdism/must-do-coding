def detectLoop(head):
    if head is None:
        return False
    slow, fast = head, head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
