"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example
Example 1:

Input: tree = {}
Output: 0
Explanation: The height of empty tree is 0.
Example 2:

Input: tree = {1,2,3,#,#,4,5}
Output: 3
Explanation: Like this:
   1
  / \
 2   3
    / \
   4   5
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
因为是最大深度肯定用DFS的思想，也可以用BFS, 但没必要！ 
以给出的example 为例
                     left: None => return  
            left: 2 / 
知道root 1 /        \right: None => return   
                             left: None => return 
           \        /left: 4/    
            right: 3        \right: None => return 
                              left: None => return                    
                    \right: 5/
                             \right: None => return 


Time: O(N), Space: O(N)

这种题有两种解法：
解法一: 比较直观的divide and conquer: 自下而上的解法
解法二：递归recursion: 自上而下的解法，是要设一个全局变量
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    """
    方法一：Divide and Conquer =>比较直观
    Time: O(N), Space: O(N)
    """

    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0

        leftH = self.maxDepth(root.left)
        rightH = self.maxDepth(root.right)

        return max(leftH, rightH) + 1

    """
    方法二：recursion DFS遍历法： 一层层往下找直到遇到None然后return 
    create a global variable max_depth 来记录谁是最高的然后和当前的层数一一比较
    Time: O(N), Space: O(N)
    """

    def maxDepth(self, root):
        ## corner cases =>在这里可写可不写
        if root is None:
            return 0
            ## init global variable
        self.max_depth = 0

        current_depth = 1

        self.rootTraverse(root, current_depth)

        return self.max_depth

    def rootTraverse(self, node, currentDepth):
        if node is None:
            return

        if self.max_depth < currentDepth:
            self.max_depth = currentDepth

        self.rootTraverse(node.left, currentDepth + 1)
        self.rootTraverse(node.right, currentDepth + 1)









