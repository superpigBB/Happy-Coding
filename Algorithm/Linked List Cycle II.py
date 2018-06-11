# Description
# Given a linked list, return the node where the cycle begins.
#
# If there is no cycle, return null.
#
# Example
# Given -21->10->4->5, tail connects to node index 1，return 10
#
# Challenge
# Follow up:
#
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

## Solution 1
## 先判断是否有cycle => linked list cycle I
## 然后一个指针回到原点，另一个指针继续往前 =》 相遇点即是那个node
## Time: O(n), Space： O（1）
class Solution:
    """
    @param: head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """

    def detectCycle(self, head):
        # write your code here
        ## corner cases:
        if head is None or head.next is None:
            return None

        slowH = head
        fastH = head.next

        while slowH is not fastH:
            if fastH is None or fastH.next is None:
                return None
            slowH = slowH.next
            fastH = fastH.next.next

        ## current: slowH is fastH, 一个回原点一个继续=>1:1 speed
        slowH = head
        fastH = fastH.next

        while slowH is not fastH:
            slowH = slowH.next
            fastH = fastH.next

        ## current: skowH is fastH
        return slowH


## Solution 2:
## Hash
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        current = head
        dict = {}

        while current:
            if current not in dict:
                dict[current] = current
            else:
                return dict[current]
            current = current.next

        return None

