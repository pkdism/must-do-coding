def intersetPoint(head_a,head_b):
    h = set()
    while head_a is not None:
        h.add(head_a)
        head_a = head_a.next
    while head_b is not None:
        if head_b in h:
            return head_b
        head_b = head_b.next
