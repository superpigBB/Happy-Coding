# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# Example 1:
#
# Input: 1->1->2
# Output: 1->2
# Example 2:
#
# Input: 1->1->2->3->3
# Output: 1->2->3

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## 同向双指针
## 应该就是简单的Linked list的删除操作
## 一般这种最好设dummy variable,以防止误删
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## corner cases
        if head is None:
            return None

        ## dummy node/h1 node/h2 node initialization
        dummyHead = ListNode(0)
        h1 = dummyHead
        h1.next = head
        h1 = h1.next
        h2 = h1.next

        while h2:
            if h2.val != h1.val:
                h1.next = h2
                h1 = h1.next
            h2 = h2.next
        h1.next = None

        return dummyHead.next

    ## 这种类型的Linkedlist题也可以不设dummy variable
    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## corner cases
        if head is None:
            return None

        ## h1 node/h2 node initialization
        h1 = head
        h2 = h1.next

        while h2:
            if h2.val != h1.val:
                h1.next = h2
                h1 = h1.next
            h2 = h2.next
        h1.next = None

        return head

