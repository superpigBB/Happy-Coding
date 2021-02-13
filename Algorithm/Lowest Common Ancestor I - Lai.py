"""
Given two nodes in a binary tree, find their lowest common ancestor.

Assumptions

There is no parent pointer for the nodes in the binary tree

The given two nodes are guaranteed to be in the binary tree

Examples

        5

      /   \

     9     12

   /  \      \

  2    3      14

The lowest common ancestor of 2 and 14 is 5

The lowest common ancestor of 2 and 9 is 9
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """"""
    """
    解题思路：bottom up recursion
    两种情况： 1. p, q各在root的left and right
             2.  p, q都在同一支路上
    Time: O(n)
    Space: O(h)
    """

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # base cases
        # or can be merged as:
        if not root or root is p or root is q:
            return root
        # if root is None:
        #   return None
        # if root.val == p.val or root.val == q.val:
        #   return root

        # left and right nodes
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if left:
            return left
        if right:
            return right
        return None
        # Or can be written as:
        return left if left else right