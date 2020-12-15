"""
Given a binary tree and a target sum, determine if the tree has a root-to-leaf path such that adding
up all the values along the path equals the given target.

Example:
Given the below binary tree and target = 16,

              5
             / \
            4   8
           /   / \
          1    3  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5-8-3 which sum is 16.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    """
    解题思路：利用recursion
    Time: O(n)
    Space: O(n)
    """

    def exist(self, root, target):
        """
        input: TreeNode root, int target
        return: boolean
        """
        # write your solution here
        # base cases
        if root is None:
            return False

        # 因为要保障root.val的root是leaf nodes， 所以他的左右子树必须为空=> leaf nodes
        if root.val == target and not root.left and not root.right:
            return True

        # for left and right nodes
        return self.exist(root.left, target - root.val) or self.exist(root.right, target - root.val)