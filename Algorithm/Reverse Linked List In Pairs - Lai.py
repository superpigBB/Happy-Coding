"""
Reverse pairs of elements in a singly-linked list.

Examples

L = null, after reverse is null
L = 1 -> null, after reverse is 1 -> null
L = 1 -> 2 -> null, after reverse is 2 -> 1 -> null
L = 1 -> 2 -> 3 -> null, after reverse is 2 -> 1 -> 3 -> null

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """ """
    """
    方法1： iteration
    解题思路：
    Time: O(n)
    Space：O(1)
    """
    def reverseInPairs1(self, head):
        """
        input: ListNode head
        return: ListNode
        """
        # write your solution here
        # corner cases
        if not head or not head.next:
            return head

        dummy = ListNode(None)
        d = dummy
        h = head
        d.next = head

        while h and h.next:
            n1 = h.next
            n2 = h.next.next
            d.next = n1
            n1.next = h
            h.next = n2

            d = h
            h = n2

        return dummy.next

    """
    方法2： recursion
    解题思路：
      Time: O(n)
      Space: O(n)
    """
    def reverseInPairs2(self, head):
        """
        input: ListNode head
        return: ListNode
        """
        # write your solution here
        # base cases
        if not head or not head.next:
            return head

        newhead = head.next
        head.next = self.reverseInPairs2(head.next.next)
        newhead.next = head

        return newhead
