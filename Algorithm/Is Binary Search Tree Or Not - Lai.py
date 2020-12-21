"""
Determine if a given binary tree is binary search tree.There should no be duplicate keys in binary search tree.

Assumptions

You can assume the keys stored in the binary search tree can not be Integer.MIN_VALUE or Integer.MAX_VALUE.
Corner Cases

What if the binary tree is null? Return true in this case.
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
    To - Do: 做一次in order iterative 遍历
    
    解题思路：1. recursion, 通过从上到下传递min, max来判定 2. 利用Pre-order scan，然后看in order value是不是 > pre-value,
    如果不是，则立刻停止
    这里用1. recursion方法
    Time: O(n)
    Space: O(h), h = n
    """

    def isBST(self, root):
        """
        input: TreeNode root
        return: boolean
        """
        # write your solution here
        min_val, max_val = float('-inf'), float('inf')
        return self.helper(root, min_val, max_val)

    def helper(self, root, min_val, max_val):
        # base cases
        if root is None:
            return True

            # for left and right nodes
        # return condition
        if root.val <= min_val or root.val >= max_val:
            return False

        return self.helper(root.left, min_val, root.val) and self.helper(root.right, root.val, max_val)
