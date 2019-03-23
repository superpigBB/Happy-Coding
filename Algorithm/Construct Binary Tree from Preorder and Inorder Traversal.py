"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Example
Example 1:
	Input:  [], []
	Output: null


Example 2:
	Input: in-order = [1,2,3], pre-order = [2,1,3]
	Output:

	  2
	 / \
	1   3

Notice
You may assume that duplicates do not exist in the tree.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
思路过程:
inorder seq: left -> root -> right
preorder seq:root -> left -> right 
也就是说能从preorder list里知道root的值是什么 =>然后推算inorder里的left and right
trees 
eg.  inorder    => 1, 2, 4, 3
     preorder   => 2, 1, 3, 4  
  2
 / \
1   3
   /
  4

1. root-> 2 => root index: 1 => left tree: inorder: [:index], postorder: [1: index + 1]   -> 1  / 1 
   right tree: inorder: [index:], postorder: [1 + index:] -> 4, 3 / 3, 4 
2. 对于左子树root： 1 / 1 => 知道root是1 =>推出 inorder: [], postorder: []
   然后return root如果Inorder 为空 => 1.left = None, 1.right = None , 2.left = 1
3. 对于右子树: 4, 3 / 3, 4 => 知道root是3， 其左子树是 4 / 4 , 右子树是 []
   对于 3的左子树 4/4 做同样的处理，得到4.left = None, 4.right = None 并return root
   4 =>然后知道3.left = 4, 3.right = None -> return root = 3 
     =>然后知道2.right = 3 
     
     
** 记得想想如果用iteration试试看以后**
"""


class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    """
    Space: O(N)， Time: O(N)
    """

    def buildTree(self, preorder, inorder):
        # write your code here
        if not inorder:
            return None

        rootval = preorder[0]
        root = TreeNode(rootval)
        rootindex = inorder.index(rootval)

        root.left = self.buildTree(preorder[1: rootindex + 1], inorder[:rootindex])
        root.right = self.buildTree(preorder[1 + rootindex:], inorder[rootindex + 1:])

        return root


