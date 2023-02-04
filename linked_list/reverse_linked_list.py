from locale import currency


class Solution(object):
    def reverseList(self, head):

        prev = None
        curr = head

        while curr:  # while current is not null
            next = curr.next  # store the value bc we are going to update curr.next
            curr.next = prev

            # shifting prev and curr pointers
            prev = curr
            curr = next
        return prev
