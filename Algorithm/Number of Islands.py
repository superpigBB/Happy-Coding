# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by
# water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3


from collections import deque


### Solution 1:这题最好不用DFS，因为可能绕得层数多了，导致stack overflow
### 一般看到这种题就要想到宽度优先搜索，但这题不用分层，就是从第一个点开始搜索，如果是1，就把它设为0，然后找他相邻在矩阵范围内的点数，然后把那些也设置为0并保存到queue里,循环直到queue为空
### Time Complexity O(M*N) Space O(min(M,N))
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        ## 异常值判断
        if grid is None or len(grid) == 0:
            return 0  ## can't be found

        ## loop the whole matrix by column and row => to search every point until the end of matrix
        island_cnt = 0
        # row:i column: j
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ##判断 grid[i][j]是否为1
                if grid[i][j] == '0':
                    continue
                else:
                    ##如果是1， 就进行BFS search每一个neighbours 并标记为0
                    self.bfs_search(grid, i, j)

                    island_cnt += 1

        return island_cnt

    ## define bfs_search function
    def bfs_search(self, grid, row, col):
        ## 设置变动指针而不改变row and col
        x, y = row, col
        q = deque()
        q.append([x, y])
        ## 找到那个是1的点，然后初始化为0
        grid[x][y] = '0'
        ## moving horizontally and vertically => 4 directions
        moving_x = [-1, 0, 1, 0]
        moving_y = [0, 1, 0, -1]

        while q:
            [x, y] = q.popleft()
            ## calculate the x/y of new point
            for index in range(len(moving_x)):
                new_x = int(x) + moving_x[index]
                new_y = int(y) + moving_y[index]
                ## 判断new_point是否在matrix内
                if not self.inbound(grid, new_x, new_y):
                    continue
                ## 如果在matrix内，判断是否值为1， 如果是1=》存入q
                else:
                    new_point = grid[new_x][new_y]
                    if new_point == '1':
                        grid[new_x][new_y] = '0'
                        q.append([new_x, new_y])

    ## 判断新点坐标有没超出matrix范围
    def inbound(self, grid, new_x, new_y):
        row_len = len(grid)
        col_len = len(grid[0])

        return (row_len > new_x and new_x >= 0) and (col_len > new_y and new_y >= 0)


### Solution 2 : the same logic with Solution 1但没用deque, 直接用stack list然后pop(0)做的
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
    def numIslands(self, grid):
        ## 异常值判断
        if grid is None or len(grid) == 0:
            return 0  ## can't be found

        ## loop the whole matrix by column and row => to search every point until the end of matrix
        island_cnt = 0
        # row:i column: j
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ##判断 grid[i][j]是否为1
                if grid[i][j] == '0':
                    continue
                else:
                    ##如果是1， 就进行BFS search每一个neighbours 并标记为0
                    self.bfs_search(grid, i, j)

                    island_cnt += 1

        return island_cnt

    ## define bfs_search function
    def bfs_search(self, grid, x, y):
        ## 设置变动指针而不改变row and col
        q = [(x, y)]
        ## 找到那个是1的点，然后初始化为0
        grid[x][y] = '0' ## 可写可不写，因为他的neigbours 遇到1还是会把他化为0， 如果事先设置为0， 那就可以省几步判断操作 line 139
        ## moving horizontally and vertically => 4 directions
        moving_x = [-1, 0, 1, 0]
        moving_y = [0, 1, 0, -1]

        while q:
            (x, y) = q.pop(0)
            ## calculate the x/y of new point
            for index in range(len(moving_x)):
                new_x = int(x) + moving_x[index]
                new_y = int(y) + moving_y[index]
                ## 判断new_point是否在matrix内
                if not self.inbound(grid, new_x, new_y):
                    continue
                ## 如果在matrix内，判断是否值为1， 如果是1=》存入q
                else:
                    new_point = grid[new_x][new_y]
                    if new_point == '1':
                        grid[new_x][new_y] = '0'
                        q.append((new_x, new_y))

    ## 判断新点坐标有没超出matrix范围
    def inbound(self, grid, new_x, new_y):
        row_len = len(grid)
        col_len = len(grid[0])

        return (row_len > new_x and new_x >= 0) and (col_len > new_y and new_y >= 0)


###Solution 3: DFS not recommended since for this problem, using DFS might cause stack overflow
### Time O(M * N), Space O(M * N)
