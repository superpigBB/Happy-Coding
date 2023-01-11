class Solution:
    """
    Time: O(row * col)
    Space: O(row * col)
    """
    def maxAreaOfIsland(self, grid) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[j][j] == 0:
                print(f'i: {i}, j: {j}')
                return 0

            grid[i][j] = 0
            cnt = 1
            cnt += dfs(i + 1, j)
            cnt += dfs(i - 1, j)
            cnt += dfs(i, j + 1)
            cnt += dfs(i, j - 1)
            return cnt

        if not grid:
            return 0
        res = 0
        rows = len(grid)
        if not rows:
            return 0
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))

        return res


print(Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
                                  [0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
                                  [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))