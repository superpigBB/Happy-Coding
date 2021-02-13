# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        total = 0
        self.recursion(root, total)
        return total

    def recursion(self, root, total):
        # base cases
        if root is None:
            return 0

        # left and right nodes
        left_node = self.recursion(root.left)
        self.recursion(root.right)

        return


root = TreeNode(3)
n1 = TreeNode(9)
n2 = TreeNode(20)
n3 = TreeNode(15)
n4 = TreeNode(7)

root.left = n1
root.right = n2
n2.left = n3
n2.right = n4


print(Solution().sumOfLeftLeaves(root))
