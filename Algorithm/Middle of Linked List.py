# Example
# Given 1->2->3, return the node with value 2.
#
# Given 1->2, return the node with value 1.


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: the head of linked list.
    @return: a middle node of the linked list
    """

    def middleNode(self, head):
        # write your code here
        if head is None or head.next is None:
            return head
        ## slow pace 1, fast pace = slow pace * 2
        slow_h = head
        # fast_h = head.next
        ## or can be changed as
        fash_h = slow_h.next

        while fast_h is not None and fast_h.next is not None:
            slow_h = slow_h.next
            fast_h = fast_h.next.next

        return slow_h