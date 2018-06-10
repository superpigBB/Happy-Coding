# Given an directed graph, a topological order of the graph nodes is defined as follow:
#
# For each directed edge A -> B in graph, A must before B in the order list.
# The first node in the order can be any node in the graph with no nodes direct to it.
# Find any topological order for the given graph.
#
#  Notice
# You can assume that there is at least one topological order in the graph.
#
# Have you met this question in a real interview?
# Clarification
# Learn more about representation of graphs
#
# Example
# For graph as follow:
#
# picture
#
# The topological order can be:
#
# [0, 1, 2, 3, 4, 5]
# [0, 2, 3, 1, 5, 4]
# ...



"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


## Time: O(N + M)， Space: O(min(M, N))
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        # write your code here
        ##异常值判断
        if graph is None or len(graph) == 0:
            return -1

        ## 存储所有入度 indegrees
        node_indegree = {}
        for node in graph:
            for neighbor in node.neighbors:
                if neighbor not in node_indegree:
                    node_indegree[neighbor] = 1
                else:
                    node_indegree[neighbor] += 1

        ## initialize top_list and BFS queue
        top_list = []
        queue = []

        ## put all nodes whose indegree = 0 first into top_list by checking hash node_indegree
        for node in graph:
            if node not in node_indegree:  ## node_indegree has values of 1 and > 1 only
                top_list.append(node)
                queue.append(node)

        ## Scan queue by BFS and reduce 1 for neighbors of those popped node
        ## if indegree == 0 => save into queue and top_list
        while queue:
            node = queue.pop(0)
            for neighbor in node.neighbors:
                node_indegree[neighbor] -= 1

                if node_indegree[neighbor] == 0:
                    queue.append(neighbor)
                    top_list.append(neighbor)

        ## check whether it's topological sorting by checking length of top_list == length of a graph
        if len(top_list) == len(graph):
            return top_list
        else:
            return -1
