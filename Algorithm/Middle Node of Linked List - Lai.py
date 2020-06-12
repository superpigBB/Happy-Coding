"""
Find the middle node of a given linked list.

Examples

L = null, return null
L = 1 -> null, return 1
L = 1 -> 2 -> null, return 1
L = 1 -> 2 -> 3 -> null, return 2
L = 1 -> 2 -> 3 -> 4 -> null, return 2
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    解题思路： 用快慢指针的方法，speed of 快指针:慢指针 = 2：1
    Time: O(n/2)
    Space: O(1)
    """
    def middleNode(self, head):
        """
        input: ListNode head
        return: ListNode
        """
        # write your solution here
        """Corner Cases"""
        if head is None or head.next is None:
            return head

        # set up fast, slow pointer
        slow, fast = head, head.next

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        return slow

n1 = ListNode(1); n2 = ListNode(2); n3 = ListNode(3); n4 = ListNode(4); n5 = ListNode(5);
n6 = ListNode(6); n7 = ListNode(7)

# head = n1; head.next = n2; n2.next = n3; n3.next = n4; n4.next = n5;
# head = n1; head.next = n2; n2.next = n3; n3.next = n4; n4.next = n5; n5.next = n6; n6.next = n7
head = None
# head = n1; head.next = None
# head = n1; head.next = n2; n2.next = n3; n3.next = n4; n4.next = None

# print(Solution().middleNode(head))  # 1 2 3 4 5 => 3
# print(Solution().middleNode(head))  # 1, 2, 3, 4, 5, 6, 7 => 4
print(Solution().middleNode(head))  # None
# print(Solution().middleNode(head))  # 1 => 1
# print(Solution().middleNode([1, 2]))  # 1
# print(Solution().middleNode([1, 2, 3]))  # 2
# print(Solution().middleNode(head))  # 1,2,3,4 = > 2
