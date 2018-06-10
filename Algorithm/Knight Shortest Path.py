# Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
# Return -1 if knight can not reached.
#
#  Notice
# source and destination must be empty.
# Knight can not enter the barrier.
#
# Have you met this question in a real interview?
# Clarification
# If the knight is at (x, y), he can get to the following positions in one step:
#
# (x + 1, y + 2)
# (x + 1, y - 2)
# (x - 1, y + 2)
# (x - 1, y - 2)
# (x + 2, y + 1)
# (x + 2, y - 1)
# (x - 2, y + 1)
# (x - 2, y - 1)
# Example
# [[0,0,0],
#  [0,0,0],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return 2
#
# [[0,1,0],
#  [0,0,0],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return 6
#
# [[0,1,0],
#  [0,0,1],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return -1

### Solution 1: BFS
### Time O(N * M),  Space O(min(M,N))

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    ### 给了起点和终点， 肯定用BFS做才能找到最短路径, 而且要用level分层遍历，count 有多少层
    def shortestPath(self, grid, source, destination):
        # write your code here
        ## 异常值检测
        if grid is None or grid[destination.x][destination.y] == 1:
            return -1

        ## initialize queue to store points
        q = [(source.x, source.y)]  ## store x/y values into queue
        path_cnt = 0
        delta_x = [1, 1, -1, -1, 2, 2, -2, -2]
        delta_y = [2, -2, 2, -2, 1, -1, 1, -1]

        while q:
            level_size = len(q)
            for i in range(level_size):
                (x, y) = q.pop(0)
                # print("x, y are %d, %d" % (point.x, point.y))
                if x == destination.x and y == destination.y:
                    return path_cnt

                for i in range(len(delta_x)):
                    new_x = x + delta_x[i]
                    new_y = y + delta_y[i]

                    ## judge whether new_x/new_y is beyond limits
                    if not self.inboundary(grid, new_x, new_y):
                        continue

                    if grid[new_x][new_y] == 1:
                        continue

                    q.append((new_x, new_y))
                    ## set we have passed once
                    grid[new_x][new_y] = 1

            path_cnt += 1
            # print("path count is %d" % path_cnt)

        ## after while loop, if no return before it ends, it means found nothing
        return -1

    def inboundary(self, grid, x, y):
        col_cnt = len(grid[0])
        row_cnt = len(grid)

        return x >= 0 and x < row_cnt and y >= 0 and y < col_cnt


### Solution 2: 双向BFS遍历法
### Time 是原来的根号倍数

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


## 最短路径， 然后给出起点和终点还是简单图，那就可以用双向宽度BFS算法
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        # write your code here
        ## 异常值判断
        if grid is None:
            return -1

        ## initilize a queue to search from the start pointand another queue to search from the end point
        start_queue = [(source.x, source.y)]
        end_queue = [(destination.x, destination.y)]

        ## initilize two hashes to store the unique past nodes for start queue / end queue
        start_dict = {(source.x, source.y): 1}
        end_dict = {(destination.x, destination.y): 1}

        ## 八个方向的delta定义
        delta_x = [1, 1, -1, -1, 2, 2, -2, -2]
        delta_y = [2, -2, 2, -2, 1, -1, 1, -1]

        path_cnt = 0

        ## 遍历start queue and end queue直到在他们各自的hash里找到共同的element,然后返回path_cnt
        while start_queue or end_queue:
            ## 对start queue 和 end_queue 进行分层遍历
            start_level_size = len(start_queue)
            end_level_size = len(end_queue)

            ## 先遍历start queue
            for num in range(start_level_size):
                (x, y) = start_queue.pop(0)
                ## 判断是否点在end_dict里
                if (x, y) in end_dict:
                    return path_cnt
                # print("start point is (%d, %d)" %(x, y))
                ##寻找 start_head的所有可能位移点
                for i in range(len(delta_x)):
                    new_x = x + delta_x[i]
                    new_y = y + delta_y[i]

                    if not self.inboundary(grid, new_x, new_y):
                        continue

                    # if grid[new_x][new_y] == 1:
                    #     continue

                    ## save that point to start_queue and start_dict and check whether it exists in end_dict
                    # if (new_x, new_y) in end_dict:
                    #     return path_cnt
                    if (new_x, new_y) in start_dict:
                        continue
                    else:
                        start_dict[(new_x, new_y)] = 1
                        start_queue.append((new_x, new_y))
                        # grid[new_x][new_y] = 1

            path_cnt += 1
            # print ('current path count is %d' %path_cnt)
            ## 再遍历end queue
            for num in range(end_level_size):
                (x, y) = end_queue.pop(0)
                ## 判断是否点在start_dict里
                if (x, y) in start_dict:
                    return path_cnt
                # print("end point is (%d, %d)" %(x, y))
                ##寻找 end_head的所有可能位移点
                for i in range(len(delta_x)):
                    new_x = x + delta_x[i]
                    new_y = y + delta_y[i]

                    if not self.inboundary(grid, new_x, new_y):
                        continue

                    # if grid[new_x][new_y] == 1:
                    #     continue

                    ## save that point to start_queue and start_dict and check whether it exists in end_dict
                    # if (new_x, new_y) in start_dict:
                    #     return path_cnt
                    if (new_x, new_y) in end_dict:
                        continue
                    else:
                        end_dict[(new_x, new_y)] = 1
                        end_queue.append((new_x, new_y))
                        # grid[new_x][new_y] = 1

            path_cnt += 1

        return -1

    def inboundary(self, grid, x, y):
        col_cnt = len(grid[0])
        row_cnt = len(grid)

        return x >= 0 and x < row_cnt and y >= 0 and y < col_cnt