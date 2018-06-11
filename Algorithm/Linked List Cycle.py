# Given a linked list, determine if it has a cycle in it.

# Example
# Given -21->10->4->5, tail connects to node index 1, return true
#
# Challenge
# Follow up:
# Can you solve it without using extra space?

# Follow up:
# Can you solve it without using extra space?


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

"""
Solution 1: 快慢指针 =》 space saved => recommended 
Solution 2: 用dict保存走过node
"""

## Solution 1: 设置两快慢指针， 速度为2:1, 如果相遇则表明有环
## Time: O(n), Space: O(1)
class Solution:
    """
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """

    def hasCycle(self, head):
        # write your code here
        ## corner cases
        if head is None or head.next is None:
            return False

        slowH = head
        fastH = head.next
        while fastH and fastH.next:
            slowH = slowH.next
            fastH = fastH.next.next
            if fastH is slowH:
                return True

        return False


## OR 1 and 2 are the same, but out of while loop condition different
    def hasCycle2(self, head):
        # write your code here
        ## corner cases
        if head is None or head.next is None:
            return False

        slowH = head
        fastH = head.next
        while fastH is not slowH:
            if not fastH or not fastH.next:
                return False
            slowH = slowH.next
            fastH = fastH.next.next

        return True


