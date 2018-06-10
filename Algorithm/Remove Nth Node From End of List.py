# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.




# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


### Solution 1:

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if head is None:
            return None

        dummy_head = ListNode(0)
        dummy_head.next = head
        head = dummy_head

        total_length = 0
        while head.next:
            head = head.next
            total_length += 1

        # print total_length
        index = total_length - n
        # print "index is %d" %index

        i = 0
        head = dummy_head
        while i < index:
            # print head.val
            head = head.next
            i += 1
        head.next = head.next.next
        # if head.next:
        #     head.next = head.next.next
        # else:
        #     head.next = None

        return dummy_head.next





## build linked list
# ListNode().__init__(ListNode, 1)
print(Solution().removeNthFromEnd([1,2,3,4,5],2))