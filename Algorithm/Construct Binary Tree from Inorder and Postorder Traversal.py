"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Example
Example 1:

Input:
[1,2]
[2,1]
Output:
{1,#,2}
Explanation:
    1
     \
      2
Example 2:

Input:
[1,2,3]
[1,3,2]
Output:
{2,1,3}
Explanation:
  2

 /  \

1    3

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
思路过程：
given: inorder trasvesal result + postorder trasvesal result => guess original 
       binary tree is 是个逆向的过程

inorder: left->root->right  postorder: left->right->root 
从已知条件来看，postorder的最后一位肯定是root所对应的值 => 通过确认root，就能
在inorder sequence里找出左子树和右子树distribution => 以此迭代循环
=>所以是recursion

eg. 1 
   / \
  2   3
   \
    4

inorder seq:   2->4->1->3
postorder seq: 4->2->3->1 

recursions: 
1. we know 1 is root => left tree: 2->4, right tree: 3
2. for left tree: inorder seq: 2->4 postorder: 4->2 
   => we know 2 is the root for left tree1, and 4 is its right tree 
   => sub lefttree is None, sub right tree inorder: 4, postorder: 4  
   => we know 2.left = None 
   => for sub righttree 4. we know 4 is the root, and no left and right tree
   => 4.left = None, 4.right = None 
   => 2.right = 4 
   => 1.left =2
3. 同理， for right tree 

** 记得想想如果用iteration试试看以后**
"""


class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    """
    Space: O（N）, Time: O(N)
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        ## recursion end condition
        if not inorder:  # 相当于inorder is None or len(inorder) == 0:
            return None

        rootval = postorder[-1]
        rootindex = inorder.index(rootval)

        root = TreeNode(rootval)

        root.left = self.buildTree(inorder[:rootindex], postorder[:rootindex])
        root.right = self.buildTree(inorder[rootindex + 1:], postorder[rootindex: -1])

        return root



