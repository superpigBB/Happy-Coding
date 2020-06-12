"""
Reverse a singly-linked list recursively.

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
    解题思路：因为Iterative的规律可以总结归纳，所以也可以用recursion => 这个recusion设计得很巧妙！
    Time: O(n)
    Space: O(n)
    """

    def reverse(self, head):
        """
        input: ListNode head
        return: ListNode
        """
        # write your solution here
        """base cases"""
        if head is None or head.next is None:
            return head

        new_head = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head

# Nodes creation
n1 = ListNode(1);
n2 = ListNode(2);
n3 = ListNode(3)
n1.next = n2;
n2.next = n3

print(Solution().reverse(n1).val)  # n3
