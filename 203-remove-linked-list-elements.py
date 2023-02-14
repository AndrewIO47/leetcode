from multiprocessing import dummy


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head, val):

    dummy = ListNode(next=head)
    setter = dummy
    looker = head

    while looker:
        if looker.val == val:
            setter.next = looker.next
            looker = looker.next
        else:
            setter = looker
            looker = looker.next

    return dummy.next
