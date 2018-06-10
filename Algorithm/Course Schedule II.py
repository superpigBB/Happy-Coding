# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
#
# Have you met this question in a real interview?
# Example
# Given n = 2, prerequisites = [[1,0]]
# Return [0,1]
#
# Given n = 4, prerequisites = [1,0],[2,0],[3,1],[3,2]]
# Return [0,1,2,3] or [0,2,1,3]


##觉得这题和course scedule一样，只是一个返回是否topology，这个表示要返回一个topological sorting list
## 就是return值不一样 + 把count list numbers 变成topological list
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        ## initialize neighbors list for each class [[], [], ...]
        class_neighbors = [[] for i in range(numCourses)]
        ## initialize indegree count for each class [0,0,...]
        class_indegree = [0] * numCourses

        for current_class, pre_class in prerequisites:
            class_neighbors[pre_class].append(current_class)
            class_indegree[current_class] += 1

        ## initialize topological list and BFS queue
        top_list = []
        queue = []

        ## get 0 indegree nodes into top_list first
        for class_num in range(numCourses):
            if class_indegree[class_num] == 0:
                top_list.append(class_num)
                queue.append(class_num)

        ## loop queue and get its neighbors
        while queue:
            class_num = queue.pop(0)
            for neighbor in class_neighbors[class_num]:
                class_indegree[neighbor] -= 1
                if class_indegree[neighbor] == 0:
                    queue.append(neighbor)
                    top_list.append(neighbor)

        if len(top_list) == numCourses:
            return top_list
        else:
            return []
