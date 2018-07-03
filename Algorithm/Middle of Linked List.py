# Example
# Given 1->2->3, return the node with value 2.
#
# Given 1->2, return the node with value 1.


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


### simple solution: loop through and get the length, then find the mid-th point
### this solution is: one loop and find the middle using 同向快慢指针
### 快：慢 = 2： 1
### Time: O(n), Space: O(1)
class Solution:
    """
    @param: head: the head of linked list.
    @return: a middle node of the linked list
    """
    ## 形式1： 更快一点
    def middleNode(self, head):
        # write your code here
        if head is None or head.next is None:
            return head
        ## slow pace 1, fast pace = slow pace * 2
        slow_h = head
        ## fast_h = head.next
        ## or can be changed as
        fast_h = slow_h.next

        while fast_h is not None and fast_h.next is not None:
            slow_h = slow_h.next
            fast_h = fast_h.next.next

        return slow_h

    ## 形式2： 更容易被理解一点
    def middleNode2(self, head):
        # write your code here
        ## corner cases
        if head is None or head.next is None:
            return head

        ## initialize fast and slow pointer
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            if fast is None:
                return slow
            slow = slow.next
        return slow