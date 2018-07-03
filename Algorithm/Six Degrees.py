# 531. Six Degrees
# Six degrees of separation is the theory that everyone and everything is six or fewer steps away, by way of introduction,
# from any other person in the world, so that a chain of "a friend of a friend" statements can be made to connect
# any two people in a maximum of six steps.
#
# Given a friendship relations, find the degrees of two people, return -1 if they can not been connected by friends of friends.
#
# Example
# Gien a graph:
#
# 1------2-----4
#  \          /
#   \        /
#    \--3--/
# {1,2,3#2,1,4#3,1,4#4,2,3} and s = 1, t = 4 return 2
#
# Gien a graph:
#
# 1      2-----4
#              /
#            /
#           3
# {1#2,4#3,4#4,2,3} and s = 1, t = 4 return -1

"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


## 给了起点和终点，求最短路径问题=》分层BFS
class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph node
    @return: an integer
    """

    def sixDegrees(self, graph, s, t):
        # write your code here
        if graph is None:
            return -1
        if s is t:
            return 0

        ## 把起点放入queue里/初始化pastNodes Set
        from collections import deque
        queue = deque([s])
        pastSet = set(s)

        levelCnt = 0
        while queue:
            levelCnt += 1
            if levelCnt > 6:
                return -1
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                ## loop all neighbors of the node
                for neighbor in node.neighbors():
                    if neighbor.label == t.label:
                        return levelCnt
                    if neighbor not in pastSet:
                        pastSet.add(neighbor)
                        queue.append(neighbor)
        return -1