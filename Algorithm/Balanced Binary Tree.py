"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.

Example
Example  1:
	Input: tree = {1,2,3}
	Output: true

	Explanation:
	This is a balanced binary tree.
		  1
		 / \
		2  3


Example  2:
	Input: tree = {3,9,20,#,#,15,7}
	Output: true

	Explanation:
	This is a balanced binary tree.
		  3
		 / \
		9  20
		  /  \
		 15   7


Example  3:
	Input: tree = {1,#,2,3,4}
	Output: false

	Explanation:
	This is not a balanced tree.
	The height of node 1's right sub-tree is 2 but left sub-tree is 0.
		  1
		   \
		   2
		  /  \
		 3   4

"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
思路过程：
涉及到任何subtree的左右子树高度之差都不能超过1，否则return false=>用divide and conquer的方法
Time: O(N) Space: O(N)
方法一和方法二都是divide and conquer,但第一种方法更适合Industrial
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    """
    方法一： divide and conquer => return set of int + bool
    """

    def isBalanced(self, root):
        # write your code here
        if root is None:
            return True

        (height, returntype) = self.traverse(root)
        return returntype

    def traverse(self, node):
        if node is None:
            return (0, True)

        (leftH, returntype1) = self.traverse(node.left)
        (rightH, returntype2) = self.traverse(node.right)

        height = max(leftH, rightH) + 1
        if returntype1 == False or returntype2 == False or abs(leftH - rightH) > 1:
            return (height, False)

        return (height, True)

    """
    方法二：divide and conquer: return值就设为int：看是否 == -1
    height = positive int if true or return -1 if not satisfied

    """

    def isBalanced(self, root):
        return self.traverse(root) != -1

    def traverse(self, node):
        if node is None:
            return 0

        leftH = self.traverse(node.left)
        if leftH == -1:
            return -1
        rightH = self.traverse(node.right)
        if rightH == -1:
            return -1

        if abs(leftH - rightH) > 1:
            return -1

        return max(leftH, rightH) + 1
