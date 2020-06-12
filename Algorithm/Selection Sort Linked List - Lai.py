"""
Given a singly-linked list, where each node contains an integer value, sort it in ascending order.
The selectoin sort algorithm should be used to solve this problem.

Examples

null, is sorted to null
1 -> null, is sorted to 1 -> null
1 -> 2 -> 3 -> null, is sorted to 1 -> 2 -> 3 -> null
4 -> 2 -> 6 -> 3 -> 5 -> null, is sorted to 2 -> 3 -> 4 -> 5 -> 6
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    解题思路：selecton sort就是从头开始扫，先排第一个，再依次排下去，知道最后一个数 => sorted in place
    因为要改变head, 所以最好create a dummy head
    Time: O(N^2)
    Space: O(N)
    """
    def selectionSort(self, head):
        """
        input: ListNode head
        return: ListNode
        """
        # write your solution here
        """corner cases"""
        if head is None or head.next is None:
            return head

        dummy_head = ListNode(None)
        dummy_head.next = head
        tmp_head = head

        while tmp_head is not None:
            cur = tmp_head.next
            min = tmp_head
            while cur is not None:
                if cur.val < min.val:
                    min = cur
                cur = cur.next
            dummy_head.next = cur
            tmp_head = tmp_head.next
