# Given a undirected graph, a node and a target, return the nearest node to given node which value of it is target, return NULL if you can't find.
#
# There is a mapping store the nodes' values in the given parameters.
#
# It's guaranteed there is only one available solution

# Example
# 2------3  5
#  \     |  |
#   \    |  |
#    \   |  |
#     \  |  |
#       1 --4
# Give a node 1, target is 50
#
# there a hash named values which is [3,4,10,50,50], represent:
# Value of node 1 is 3
# Value of node 2 is 4
# Value of node 3 is 10
# Value of node 4 is 50
# Value of node 5 is 50
#
# Return node 4

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


## Solution 总结：
## BFS 方法肯定是针对这题的最优解法
## Solution 1 是传统的利用hashset来记录访问过的node的BFS法 =》 比较推荐如果直接先写
## Solution 2 是对space进行了优化，属于优化写法，就是每次遍历过的点把他们都标记为遍历过（这里是直接删了所在的key/value）
## 能作为follow up 优化处理的解法用
## 2 是 1 的改进版！
#########################################################################################################

## Solution 1: 这题如果能想到BFS方法做就容易很多了
## 这题实际就是给定原点，然后开始遍历neighbor上所有的nodes
## 一旦有node的值是target值，那就直接返回
## 一定要用hashset来记录访问过的节点否则会重复访问节点
## Time: O(N + M), Space: O(N)
class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """

    def searchNode(self, graph, values, node, target):
        # write your code here
        ## corner cases
        if node is None:
            return None
            ## 还要考虑可能是自己的情况
        if values[node] == target:
            return node

        ## initialize queue and hashset
        from collections import deque
        queue = deque([node])
        visitedNodes = {node}

        while queue:
            graphNode = queue.popleft()
            for neighbor in graphNode.neighbors:
                if values[neighbor] == target:
                    return neighbor

                if neighbor not in visitedNodes:
                    visitedNodes.add(neighbor)
                    queue.append(neighbor)

        return None


"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""



## Solution 2: 和Solution 1不一样的地方是不用hashset来记录访问过的nodes
## 而是直接删访问过的values key/value pair， 这样能省space 空间！
## Time: O(N + M), Space: O(1)
class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """

    def searchNode(self, graph, values, node, target):
        # write your code here
        ## corner cases
        if node is None:
            return None
            ## 还要考虑可能是自己的情况
        if values[node] == target:
            return node

        ## initialize queue
        from collections import deque
        queue = deque([node])
        del values[node]

        while queue:
            graphNode = queue.popleft()

            for neighbor in graphNode.neighbors:
                if neighbor in values:
                    if values[neighbor] == target:
                        return neighbor
                    queue.append(neighbor)
                    ## 删除访问过的node
                    del values[neighbor]

        return None

