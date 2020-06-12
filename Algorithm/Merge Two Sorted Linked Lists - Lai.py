"""
Merge two sorted lists into one large sorted list.

Examples

L1 = 1 -> 4 -> 6 -> null, L2 = 2 -> 5 -> null, merge L1 and L2 to 1 -> 2 -> 4 -> 5 -> 6 -> null
L1 = null, L2 = 1 -> 2 -> null, merge L1 and L2 to 1 -> 2 -> null
L1 = null, L2 = null, merge L1 and L2 to null
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
TODO： recursion method
"""
class Solution(object):
    """
    解题思路：
    方法一（比较简单）：创建一个新linked list h3来save sorted nodes in h1 and h2
        这个方法比较耗空间复杂度因为新建list
        因为create a linked list from scratch, need to create a dummy head
    Time: O(max(size(one), size(two)))
    Space: O(1) => only created a dummy head node
    """
    def merge(self, one, two):
        """
        input: ListNode one, ListNode two
        return: ListNode
        """
        # write your solution here
        """corner cases"""
        if one is None:
            return two
        if two is None:
            return one

        dummy_head = ListNode(None)
        cur = dummy_head
        while one is not None and two is not None:
            if one.val <= two.val:
                cur.next = one
                one = one.next
            else:
                cur.next = two
                two = two.next

            cur = cur.next

        # link the rest of h1 or h2
        if one is not None:
            cur.next = one

        if two is not None:
            cur.next = two

        return dummy_head.next


# build nodes
h1 = ListNode(1); n2 = ListNode(4); n3 = ListNode(6)
h2 = ListNode(2); n4 = ListNode(5)
h1.next = n2; n2.next = n3;
h2.next = n4

merged = Solution().merge(h1,h2)
pass

