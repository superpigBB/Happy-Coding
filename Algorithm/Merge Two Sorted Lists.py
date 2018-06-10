# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


### Solution1:
### Time Complextiy O(n + m), space O(1)
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1 is None and l2 is None:
            return None

        head = ListNode(0)
        cur = head
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next

        else:
            cur.next = l2
            l2 = l2.next

        cur = cur.next
        # print("test")
        while l1 and l2:
            # print(l1.val, l2.val)
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l2 is None:
            cur.next = l1
        else:
            cur.next = l2
        return head.next


### Solution1.2:
### Enhancements from Solution 1
### Time Complextiy O(n + m), space O(1)
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1 is None and l2 is None:
            return None

        head = ListNode(0)
        cur = head
        # print("test")
        while l1 and l2:
            # print(l1.val, l2.val)
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l2 is None:
            cur.next = l1
        else:
            cur.next = l2
        return head.next

### Solution2:
### Time Complextiy O(n + m), space O(n + m)
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

