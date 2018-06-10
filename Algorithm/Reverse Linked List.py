# Reverse a singly linked list.
#
# click to show more hints.
#
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?
#
# Example
# For linked list 1->2->3, the reversed linked list is 3->2->1


class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

### Solution 1:
### Time O(N), Space O(1)
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new = None
        # new = ListNode(None)
        # print(head.val, head.next.val)
        cur = head
        # # print(cur.val, cur.next.val)
        # head = head.next
        # cur = cur.next
        # head.next = new
        # cur.next = new


        # print(head.val, head.next.val, cur.val, cur.next.val)
        while head:
            head = head.next
            cur.next = new
            new = cur
            cur = head
        return new


### Solution 1.2:
### Time O(N), Space O(1)

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new = None
        while head is not None:
            tmp = head.next
            head.next = new
            new = head
            head = tmp
        return new


### Solution 2 recursive
### Directly copy from other answer online
### Time O(N), Space O(N)
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.doReverse(head, None)

    def doReverse(self, head, newHead):
        if head is None:
            return newHead
        next = head.next
        head.next = newHead
        return self.doReverse(next, head)

### Solution 2.2 Recursive
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        p = head.next
        n = self.reverseList(p)

        head.next = None
        p.next = head
        return n