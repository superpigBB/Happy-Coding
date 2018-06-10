# Lintcode Description
# Write a program to find the node at which the intersection of two singly linked lists begins.
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Have you met this question in a real interview?  Yes
# Example
# The following two linked lists:
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# begin to intersect at node c1.
#
# Challenge
# Your code should preferably run in O(n) time and use only O(1) memory.

############################################################################################################3

# LeetCode Description
#
# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# begin to intersect at node c1.
#
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
#
#

"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


## 这题就是假设两个linked list肯定有intersection部分除corner cases情况之外
## 而且要求不呢个改变original structure,那就不能人工构造环形
## 要么就从两头以速度1：1走然后走到头以后交换->Solution 1
## 要么就走长的一头先，直到剩下的长度和短的那条linked listy一样，同时以1：1速度走，第一次遇见的就是入口 -> Solution 2
## 要么就是用hashset来记录两条linkedlist走过的路径，知道在某个node另一条也正好走过，就是第一次相遇的地方 -> Solution 3.1/3.2
## 最后一种解法leetcode不允许，因为尽管最后把linked lists还原了，可还是变动过了，不符合题意

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## 这题就是假设两个linked list肯定有intersection部分除corner cases情况之外
## 而且要求不呢个改变original structure,那就不能人工构造环形
## 要么就从两头以速度1：1走然后走到头以后交换->Solution 2
## 要么就走长的一头先，直到剩下的长度和短的那条linked listy一样，同时以1：1速度走，第一次遇见的就是入口 -> Solution 1
## 要么就是用hashset来记录两条linkedlist走过的路径，知道在某个node另一条也正好走过，就是第一次相遇的地方 -> Solution 3

## Solution 1
## 同时从两头出发，遇到None 然后交换到另一条linked list继续走，直到相遇
## Time: O(N), Space: O(1)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ## Corner cases
        if headA is None or headB is None:
            return None

        h1 = headA
        h2 = headB


        ## speed 1:1
        ## expression 1: faster => recommended variable = value1 if ... else value2
        while h1 is not h2:
            h1 = headB if not h1 else h1.next
            h2 = headA if not h2 else h2.next

        ## expression 2: slower
        # while h1 is not h2:
        #     if not h1:
        #         h1 = headB
        #     else:
        #         h1 = h1.next
        #
        #     if not h2:
        #         h2 = headA
        #     else:
        #         h2 = h2.next

        return h1


## Solution 2
## 分别得到两个linked list的长度，然后先遍历长的那一根，直到长的那一根的剩余长度=短的，然后同时以速度1：1走
## Time: O(N), Space: O(1)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ## Corner cases
        if headA is None or headB is None:
            return None

        h1 = headA
        h2 = headB

        ## get A length
        lenA = 0
        while h1:
            lenA += 1
            h1 = h1.next

        ## get B length
        lenB = 0
        while h2:
            lenB += 1
            h2 = h2.next

        h1 = headA
        h2 = headB
        ## compare lenA with lenB and loop longer linked list
        while lenA > lenB:
            h1 = h1.next
            lenA -= 1

        while lenB > lenA:
            h2 = h2.next
            lenB -= 1

        ## current lenA = lenB and h1, h2 start at the relative same position of two updated linked lists
        while h1 is not h2:
            h1 = h1.next
            h2 = h2.next

        return h1


## Solution 3.1: 用两个dicts分别记录两个指针经过的路径
## time: O(n), space: O(n)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ## corner cases
        if headA is None or headB is None:
            return None

        ## initialize two moving pointers
        h1 = headA
        h2 = headB

        if headA == headB:
            return headA

        ## initialize two hashes to save first two head nodes
        from collections import defaultdict
        dict1 = defaultdict(int); dict1[headA] = 1
        dict2 = defaultdict(int); dict2[headB] = 1

        while h1.next and h2.next:
            h1 = h1.next
            h2 = h2.next

            if h1 in dict2:
                return h1
            dict1[h1] = 1

            if h2 in dict1:
                return h2
            dict2[h2] = 1

        ## left linked list is h1
        while h1.next is not None:
            h1 = h1.next
            if h1 in dict2:
                return h1

        ## left linked list is h2
        while h2.next is not None:
            h2 = h2.next
            if h2 in dict1:
                return h2

        return None

## Solution 3.2:用两个sets分别记录两个指针经过的路径
## time: O(n), space: O(n)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ## corner cases
        if headA is None or headB is None:
            return None

        ## initialize two moving pointers
        h1 = headA
        h2 = headB

        if headA.val == headB.val:
            return headA

        ## initialize two sets of pointers path
        set1 = {headA.val}
        set2 = {headB.val}

        while h1.next is not None and h2.next is not None:
            h1 = h1.next
            h2 = h2.next

            if h1.val in set2:
                return h1
            set1.add(h1.val)

            if h2.val in set1:
                return h2
            set2.add(h2.val)

        ## left linked list is h1
        while h1.next is not None:
            h1 = h1.next
            if h1.val in set2:
                return h1

        ## left linked list is h2
        while h2.next is not None:
            h2 = h2.next
            if h2.val in set1:
                return h2

        return None





## Solution: 同向双指针=>不用hash or set来存过往路径 => lintcode works but not leetcode
## 因为中间modify一次那个linked list但leetcode说明不能modify任何一次
## 通过构造成带环链表，让最后一个node指向headB, 从而形成一个以headA为起点的带环链表
## Time: O(n), Space O(1)
class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ## corner cases
        if headA is None or headB is None:
            return None
        if headA == headB:
            return headA
        ## 遍历其中一个head, 以headA为例，把末尾node指向headB从而形成带环链表
        h1 = headA
        while h1.next:
            h1 = h1.next
        h1.next = headB ## 因为不能改变structure, 所以把h1的位置得记录下来

        ## 从headA出发慢指针h1, headA.next出发快指针h2, 两倍速度于h1
        ## 当h1和h2相遇时，h1退回headA, 和h2同时以速度1出发，相遇的点就是first interacted
        h11 = headA
        h22 = headA.next

        ##找h1和h2首次相遇的node, speed_h1:speed_h2 = 1:2
        while h11 != h22:
            if h22 is None or h22.next is None: ## 如果首尾相连后还是能找到None,说明没有共同点
                return None

            h11 = h11.next
            h22 = h22.next.next

        ## h1退回原点，speed_h1:speed_h2 = 1:1
        h11 = headA
        h22 = h22.next
        while h11 != h22:
            h11 = h11.next
            h22 = h22.next
            # print h1.val, h2.val

        ##  还原A link
        h1.next = None
        return h11


