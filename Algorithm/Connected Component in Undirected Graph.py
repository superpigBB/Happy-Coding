# Find the number connected component in the undirected graph. Each node in the graph contains a label and a list of its
# neighbors. (a connected component (or just component) of an undirected graph is a subgraph in which any two vertices are
# connected to each other by paths, and which is connected to no additional vertices in the supergraph.)
#
# Example
# Given graph:
#
# A------B  C
#  \     |  |
#   \    |  |
#    \   |  |
#     \  |  |
#       D   E
# Return {A,B,D}, {C,E}. Since there are two connected component which is {A,B,D}, {C,E}

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

## Two Solutions: ## 无向图连通块, 可以使用BFS或者并查集union find求解 .
## 1) BFS/DFS => 因为现在只会这个方法， 但觉得union find 会更快，等以后学了再回过头来做！ 2) Union Find

## Solution 1): BFS =>
## 测试连通性=》BFS，并标记所有连通好的nodes，然后把剩下没联通好
## 的node继续BFS测试连通性
## Time: O(n*(n + m)), Space: O(n)
class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """

    def connectedSet(self, nodes):
        # write your code here
        ## corner cases
        if nodes is None:
            return []

        ## initialization
        visitedNodes = set()  # hashset to save visited nodes
        returnResult = []  # return list
        from collections import deque
        queue = deque([])

        ## loop all nodes
        # import heapq
        for node in nodes:
            if node in visitedNodes:
                continue
            visitedNodes.add(node)
            queue.append(node)
            ## loop queue until empty
            connectedLabels = []
            while queue:
                graphNode = queue.popleft()
                # heapq.heappush(connectedLabels, graphNode.label)
                connectedLabels.append(graphNode.label)
                for neighbor in graphNode.neighbors:
                    if neighbor not in visitedNodes:
                        visitedNodes.add(neighbor)
                        queue.append(neighbor)

            returnResult.append(sorted(connectedLabels))

        return returnResult
