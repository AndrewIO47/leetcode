class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    og = []
    reversed = []

    # 1) convert the list into an array
    while head:
        og.append(head.val)
        head = head.next

    # 2) reverse the array
    for i in range(len(og), -1, -1):
        reversed.append(og[i])
    # 3) compare
    if og == reversed:
        return True

    return False


head = [1, 2, 2, 1]
print(isPalindrome(head))
