# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(head):

        # edge case were head is empty
        if head is None:
            return head

        curr_node = head
        # iterate until the last node
        while (curr_node.next):
            next_node = curr_node.next

            if curr_node.val == next_node.val:
                curr_node.next = next_node.next
                next_node = next_node.next
            else:
                curr_node = next_node
                next_node = next_node.next

        return head
