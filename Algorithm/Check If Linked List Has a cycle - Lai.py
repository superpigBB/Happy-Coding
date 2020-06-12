"""
Check if a given linked list has a cycle. Return true if it does, otherwise return false.



Assumption:

You can assume there is no duplicate value appear in the linked list.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    解题思路：记得九章以前提过，trick to find if a cycle exists in linkedlist is to check whether fast/slow pointers他们可以
    相遇； 如果fast: slow = 2: 1, 那fast肯定最终能追上slow那个如果是cycle linkedlist
    Time: O(n)
    Space: O(1)
    """
    def checkCycle(self, head):
        """
        input: ListNode head
        return: boolean
        """
        # write your solution here
        """Corner Cases"""
        if head is None or head.next is None:
            return False

        fast, slow = head.next, head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False

# build linked list with cycle
n1 = ListNode(1); n2 = ListNode(2); n3 = ListNode(3); n4 = ListNode(4)
# n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n1
n1.next = n2; n2.next = n3; n3.next = n4; n4.next = None

# test cases
print(Solution().checkCycle(n1))
