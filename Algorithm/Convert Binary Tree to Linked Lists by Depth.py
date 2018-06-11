# Description
# Given a binary tree, design an algorithm which creates a linked list
# of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
#
# Have you met this question in a real interview?
# Example
# Given binary tree:
#
#     1
#    / \
#   2   3
#  /
# 4
# return
#
# [
#   1->null,
#   2->3->null,
#   4->null
# ]


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


# {37,-34,-48,#,-100,-100,48,#,#,#,#,-54,#,-71,-22,#,#,#,8}


## 这题明显的分层BFS，每层遍历
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list

    ## function 1: 设了dummy node当create linked list, 第一个node就是dummy node， 然后返回dummynode.next
    def binaryTreeToLists(self, root):
        # Write your code here
        ## corner cases
        if root is None:
            return []

        ## initialization
        from collections import deque
        queue = deque([root])
        result = []
        dummyNode = ListNode(0)

        while queue:
            levelSize = len(queue)
            list_node = dummyNode
            for i in range(levelSize):
                treeNode = queue.popleft()
                list_node.next = ListNode(treeNode.val)
                list_node = list_node.next

                if treeNode.left:
                    queue.append(treeNode.left)
                if treeNode.right:
                    queue.append(treeNode.right)
            # print ("list node => ", list_node, " list node next => ", list_node.next)
            result.append(dummyNode.next)

        return result

    ## function 2: 没有设dummy node， 第一个node就是树的最左边的node
    def binaryTreeToLists2(self, root):
        # Write your code here
        ## corner cases
        if root is None:
            return []

        ## initialization
        from collections import deque
        queue = deque([root])
        result = []

        while queue:
            levelSize = len(queue)
            list_node = None
            for i in range(levelSize):
                treeNode = queue.popleft()
                if list_node is None:
                    list_node = ListNode(treeNode.val)
                    lastNode = list_node
                else:
                    lastNode.next = ListNode(treeNode.val)
                    lastNode = lastNode.next

                if treeNode.left:
                    queue.append(treeNode.left)
                if treeNode.right:
                    queue.append(treeNode.right)
            # print ("list node => ", list_node, " list node next => ", list_node.next)
            result.append(list_node)

        return result



