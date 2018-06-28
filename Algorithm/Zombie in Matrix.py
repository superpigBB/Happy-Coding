# Description
# Given a 2D grid, each cell is either a wall 2, a zombie 1 or people 0 (the number zero, one, two).
# Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall.
# How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.

# Example
# Given a matrix:
#
# 0 1 2 0 0
# 1 0 0 2 1
# 0 1 0 0 0
# return 2


class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    ## 类分层BFS的做法，对于grid，对人也就是0进行搜索， 找到人就设为1
    ## 每次遍历完整个grid算是一层搜索完成
    ## 设people_cnt and become_zombie_cnt,如果become_zombie_cnt = 0 return -1
    ## 当people_cnt == become_zombie_cnt, return 遍历个数
    def zombie(self, grid):
        # write your code here
        ## corner cases
        if grid is None:
            return -1

        row = len(grid)
        col = len(grid[0])

        ## initialize variables
        day_cnt = 1
        delta_x = [0, 0, -1, 1]
        delta_y = [1, -1, 0, 0]

        while True:
            peopleMetCnt = 0
            becomeZombieCnt = 0
            becomeZombieSet = set()  ## set来存储变成zombie的点坐标
            for i in range(row):
                for j in range(col):
                    ##找到人了，然后查左右邻居，只要有一个是1就return并且变为1
                    if grid[i][j] == 0:
                        peopleMetCnt += 1
                        ## check neighbors for those people
                        if self.neighborIsZombie(grid, i, j, delta_x, delta_y, becomeZombieSet):
                            grid[i][j] = 1  ## 如果发现四周有zombie,就把人变为zombie
                            becomeZombieSet.add((i, j))
                            becomeZombieCnt += 1
            # print 'people count is %d, become zombie count is %d' %(peopleMetCnt, becomeZombieCnt)
            if peopleMetCnt != 0 and becomeZombieCnt == 0:
                return -1
            if peopleMetCnt == becomeZombieCnt:
                return day_cnt
            day_cnt += 1

            ## detect people neighbors zombie or not and whether it's within boundary

    def neighborIsZombie(self, grid, x, y, delta_x, delta_y, becomeZombieSet):
        for i in range(len(delta_x)):
            newX = x + delta_x[i]
            newY = y + delta_y[i]

            if self.isBoundary(grid, newX, newY) and grid[newX][newY] == 1 and (newX, newY) not in becomeZombieSet:
                # print "yes"
                return True

    ## boundary 判断
    def isBoundary(self, grid, x, y):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])



