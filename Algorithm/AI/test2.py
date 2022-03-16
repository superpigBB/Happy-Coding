# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    """
    解题思路：因为是sorted linked list, 只要把insert的val和前后linked list val比较即可选择插入
    Time: O(n)
    Space: O(1)
    """

    def insert(self, head, value):
        """
        input: ListNode head, int value
        return: ListNode
        """
        # write your solution here
        # corner cases
        if not head:
            return None

        # 因为可能会改变head，所以要设置dummy head
        dummy = ListNode(None)
        d = dummy
        d.next = head

        insert_node = ListNode(value)

        while d.next:
            if value <= d.next.val:
                insert_node.next = d.next.next
                d.next = insert_node
                break
            elif value > d.next.val:
                d = d.next

        return dummy.next

head = ListNode(3)
print(Solution().insert(head, 3))