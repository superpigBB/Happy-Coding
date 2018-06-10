# On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).
#
# A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
#
# Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.
#
# The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.
#
# Example:
# Input: 3, 2, 0, 0
# Output: 0.0625
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
# From each of those positions, there are also two moves that will keep the knight on the board.
# The total probability the knight stays on the board is 0.0625.
# Note:
# N will be between 1 and 25.
# K will be between 0 and 100.
# The knight always initially starts on the board.

### Solution 1: BFS not works , Time Exceeded! 因为走步没有标记。当K 很大，可能走的depth很深,
class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        ##极端值判断
        if r >= N or c >= N:
            return 0
        if K == 0:
            return 1

        ## save start point r c to queue
        queue = [(r, c)]

        ## initialize move count
        level_cnt = 0
        total_cnt = 0

        ## initialize 8 directions
        delta_x = [2, 1, -2, -1, 2, 1, -2, -1]
        delta_y = [-1, 2, 1, 2, 1, -2, -1, -2]

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                (x, y) = queue.pop(0)

                for i in range(len(delta_x)):
                    new_x, new_y = x + delta_x[i], y + delta_y[i]
                    if self.inboundary(N, new_x, new_y):
                        queue.append((new_x, new_y))
                        # total_cnt += 1

            level_cnt += 1
            # total_cnt += 1

            if level_cnt == K:
                break

        return len(queue) / 8 ** K

    def inboundary(self, N, point_x, point_y):
        return point_x < N and point_x >= 0 and point_y < N and point_y >= 0
