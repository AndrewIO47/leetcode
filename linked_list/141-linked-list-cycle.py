def hasCycle(head):

    # edge case were the list is empty
    if head is None:
        return False

    slow = head
    fast = head.next
    try:
        # while the fast hasn't reached the slow
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True

    except:
        return False
