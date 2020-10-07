"""
Given a Binary Search Tree(BST), find the second largest element. You can assume that a node inside this tree
only contains a single value. For this problem, the requirement is to solve this with recursion. If there is any
subroutine you need, it also nees to be written with recursion
Examples:

Input: Root of below BST
    10
   /
  5

Output:  5


Input: Root of below BST
        10
      /   \
    5      20
             \
              30

Output:  20
"""
"""TO DO !!!"""
# Definition for a binary tree node.
class TreeNode(object):
    """
    Time: O(H) -> Height of Tree
    Space: O(H) -> Height of Tree
    """
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

class Solution(object):
    """Find Largest Node First"""
    def find_largest(self, root):
        if not root:
            return

        current = root
        while current:
            if not current.right:
                return current.value
            current = current.right

    """Find Second Largest and 2 cases for that """
    def find_second_largest(self, root):
        """Corner cases"""
        if root is None or root.left is None and root.right is None:
            return

        current = root

        while current:
            # Case 1
            if current.left and not current.right:
                return self.find_largest(current.left)

            # Case 2
            if current.right and not current.right.left and not current.right.right:
                return current.value

            current = current.right


T1 = TreeNode(10); T2 = TreeNode(7); T3 = TreeNode(3); T4 = TreeNode(8); T5 = TreeNode(12)
T6 = TreeNode(11); T7 = TreeNode(13)

T1.left = T2; T2.left = T3; T2.right = T4; T1.right = T5; T5.left = T6; T5.right = T7

print(Solution().find_second_largest(T1))
