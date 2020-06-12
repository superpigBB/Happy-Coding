"""
Return the number of nodes in the linked list.

Examples

L = null, return 0
L = 1 -> null, return 1
L = 1 -> 2 -> null, return 2
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    解题思路：LinkedList基本概念
    Time: O(n)
    Space: O(1)
    """
    def numberOfNodes(self, head):
        """
        input: ListNode head
        return: int
        """
        # write your solution here
        """Corner Cases"""
        if head is None:
            return 0
        if head.next is None:
            return 1

        node_cnt = 0
        while head is not None:
            node_cnt += 1
            head = head.next

        return node_cnt

# Nodes Initialization
n1 = ListNode(1); n2 = ListNode(2); n3 = ListNode(3)
n1.next = n2; n2.next = n3

print(Solution().numberOfNodes(n1))  # 3


