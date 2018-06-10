# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
#
# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0,
# and to take course 0 you should also have finished course 1. So it is impossible.

### Solution 1: Time complexity is not good enough => Solution 2
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):
        # write your code here
        ## 异常值判断
        if prerequisites is None or len(prerequisites) == 0:
            return True

        ## neighbors_dict save key: pre_class value: list of neighbors of pre_class
        neighbors_dict = {}
        ## class_indegree dict key: class value: indegree count
        class_indegree = {}
        ## pairs_dict to check whether processing duplicate pairs - key: pair value: count
        pairs_dict = {}
        ## list including all distinct classes
        total_classes = []
        ## prerequisites pair [class node, pre-class node]
        for classpair in prerequisites:
            pre_class = classpair[1]
            current_class = classpair[0]
            if (current_class, pre_class) not in pairs_dict:
                pairs_dict[(current_class, pre_class)] = 1
            else:
                continue

            if current_class not in class_indegree:
                class_indegree[current_class] = 1
            else:
                class_indegree[current_class] += 1
            ## current_class as neighbor of pre_class
            if pre_class not in neighbors_dict:
                neighbors_dict[pre_class] = [current_class]
            else:
                neighbors_dict[pre_class].append(current_class)

            ## save unique class value
            if pre_class not in total_classes:
                total_classes.append(pre_class)
            if current_class not in total_classes:
                total_classes.append(current_class)

        ## initialize top_list and BFS queue
        top_list = []
        queue = []
        ## loop through list total_courses and save nodes with indegree = 0
        for class_node in total_classes:
            if class_node not in class_indegree:
                top_list.append(class_node)
                queue.append(class_node)
            if class_node not in neighbors_dict:
                neighbors_dict[class_node] = []

        ## scan BFS queue and reduce 1 indegree for those nodes
        while queue:
            class_node = queue.pop(0)
            for neighbor in neighbors_dict[class_node]:
                print("class_node %d: neighbor: %d" %(class_node, neighbor))
                class_indegree[neighbor] -= 1

                if class_indegree[neighbor] == 0:
                    queue.append(neighbor)
                    top_list.append(neighbor)

        ## check topological conditions:
        return len(total_classes) == len(top_list)

## Solution 2.1:
## 上次那个用dict存储每个node的neighbors 和相应的indegree counts,由于用到了很多hash,如果list量很大，比较耗space
## 这个方法和Solution1 类似，但把neighbors 设成array 组,实际就是adjacent list， 每个index代表每个course的相应neibors [[], [], ...]
## 然后在同一个loop里实现indegree的count
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):
        # write your code here
        ## extreme situations exclusion
        if prerequisites is None or len(prerequisites) == 0:
            return True

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

        return len(top_list) == numCourses


## Solution 2.2
## Solution 2 的进阶版，可以让速度更快，因为少存了一个top_list, top_list也耗space, 如果换成integer 效果一样但省空间
## 因为现在没让return topological list而是问是不是， 所以可以省去一个list的空间
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):
        # write your code here
        ## extreme situations exclusion
        if prerequisites is None or len(prerequisites) == 0:
            return True

        ## initialize neighbors list for each class [[], [], ...]
        class_neighbors = [[] for i in range(numCourses)]
        ## initialize indegree count for each class [0,0,...]
        class_indegree = [0] * numCourses

        for current_class, pre_class in prerequisites:
            class_neighbors[pre_class].append(current_class)
            class_indegree[current_class] += 1

        ## initialize BFS queue and topological sequeunce count
        queue = []
        count = 0

        ## get 0 indegree nodes into top_list first
        for class_num in range(numCourses):
            if class_indegree[class_num] == 0:
                # top_list.append(class_num)
                queue.append(class_num)

        ## loop queue and get its neighbors
        while queue:
            class_num = queue.pop(0)
            count += 1
            for neighbor in class_neighbors[class_num]:
                class_indegree[neighbor] -= 1
                if class_indegree[neighbor] == 0:
                    queue.append(neighbor)
                    # top_list.append(neighbor)

        return count == numCourses