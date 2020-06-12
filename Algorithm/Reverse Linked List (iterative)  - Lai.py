"""
Reverse a singly-linked list iteratively.

Examples

L = null, return null
L = 1 -> null, return 1 -> null
L = 1 -> 2 -> 3 -> null, return 3 -> 2 -> 1 -> null

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    解题思路：因为可能要改变head,所以要设一个dummy head first, 然后return dummy_head即可
    Time: O(n)
    space: O(1)
    """
    def reverse(self, head):
        """
        input: ListNode head
        return: ListNode
        """
        # write your solution here
        """Corner Cases"""
        if head is None or head.next is None:
            return head

        dummy_head = None

        while head is not None:
            current = head.next
            head.next = dummy_head
            dummy_head = head
            head = current

        return dummy_head
    
# Nodes creation
n1 = ListNode(1); n2 = ListNode(2); n3 = ListNode(3)
n1.next = n2; n2.next = n3

print(Solution().reverse(n1))  # n3


