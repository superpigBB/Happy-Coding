"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    """
    解题思路： 显然，我们从根节点开始，递归地对树进行遍历，并从叶子结点先开始翻转。如果当前遍历到的节点root 的左右两棵子树都已经翻转，
    那么我们只需要交换两棵子树的位置，即可完成以root 为根节点的整棵子树的翻转
    Time: O(n)
    Space: O(n)
    """
    def invertTree(self, root):
        """
        input: TreeNode root
        return: TreeNode
        """
        # write your solution here
        # base cases
        if root is None:
            return root

        # left and right nodes
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left
        return root
