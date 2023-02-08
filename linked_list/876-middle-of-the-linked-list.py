# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):

        curr_node = head
        length = 0
        # get the length of the linked list
        while (curr_node):
            curr_node = curr_node.next
            length += 1

        middle = length/2
        # reset curr_node
        curr_node = head
        # search for the middle of the linked list
        while (middle != 0):
            curr_node = curr_node.next
            middle -= 1

        head = curr_node
        return head

# ONLINE SOLUTION
    def middleNode(self, head):
        slow = fast = head

        # fast will go twice as fast as slow making the slow point
        # the middle when it finishes
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
