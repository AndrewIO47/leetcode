
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):

        # dummy = ListNode(0, head)
        dummy = 0
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        # shifts left and right pointer until right pointer points to null
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
