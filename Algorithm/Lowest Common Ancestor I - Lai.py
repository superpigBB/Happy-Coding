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
    解题思路：自上向下然后自下向上的recursion比较合理，分情况讨论：
    1. common分别在left, right node上，则parent node就是Lowest
    2. common在一条支路上，则先碰到的那个就是lowest
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
        # base cases:
        if root is None:
            return None

        if root is p or root is q:
            return root

        # for left and right nodes
        left_common = self.lowestCommonAncestor(root.left, p, q)
        right_common = self.lowestCommonAncestor(root.right, p, q)

        # 2 conditions
        if left_common and right_common:
            return root

        return left_common if left_common else right_common
