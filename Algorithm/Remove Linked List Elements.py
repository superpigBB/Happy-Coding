# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
#
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.


### Solution 1:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        if head is None:
            return None

        dummy_head = ListNode(0)
        dummy_head.next = head
        head = dummy_head

        total_length = 0
        while head.next:
            head = head.next
            total_length += 1

        # print total_length
        index = total_length - n
        # print "index is %d" %index


        i = 0
        head = dummy_head
        while i < index:
            # print head.val
            head = head.next
            i += 1
        head.next = head.next.next
        # if head.next:
        #     head.next = head.next.next
        # else:
        #     head.next = None

        return dummy_head.next


###Solution 2:

class Solution:
    """
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: The head of linked list.
    """

    def removeNthFromEnd(self, head, n):
        # write your code here
        if head is None:
            return None

        dummy_head = ListNode(0)
        dummy_head.next = head
        # head = dummy_head
        first = dummy_head
        second = dummy_head

        i = 0
        while first.next:
            first = first.next
            i += 1
            if i > n:
                second = second.next
        second.next = second.next.next
        return dummy_head.next