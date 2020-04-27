"""
Given a 2D matrix that contains integers only, which each row is sorted in an ascending order.
The first element of next row is larger than (or equal to) the last element of previous row.

Given a target number, returning the position that the target locates within the matrix.
If the target number does not exist in the matrix, return {-1, -1}.

Assumptions:

The given matrix is not null, and has size of N * M, where N >= 0 and M >= 0.
Examples:

matrix = { {1, 2, 3}, {4, 5, 7}, {8, 9, 10} }

target = 7, return {1, 2}

target = 6, return {-1, -1} to represent the target number does not exist in the matrix.
"""


class Solution(object):
    """
    解题思路： 因为每行都是sorted,而且next row第一个element也比last row的last element大，所以整个matrix就是一个sorted integer
    matrix => binary search是最好的选择.
    同样的用mid index来作准则,只是这题需要把index transformed into matrix index来locate element再来判断
    matrix(x, y) = element_index // col, element_index % col
    Time: O(logmn)  m = row, n = col
    Space: O(1)
    """
    def search(self, matrix, target):
        """
        input: int[][] matrix, int target
        return: int[]
        """
        # write your solution here
        """Corner Cases"""
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0 or matrix[0] is None:
            return [-1, -1]

        row = len(matrix)
        col = len(matrix[0])
        start, end = 0, row * col - 1

        while start <= end:
            mid = (start + end) // 2
            # need to transform into matrix index first
            mid_row, mid_col = mid // col, mid % col
            if matrix[mid_row][mid_col] == target:
                return [mid_row, mid_col]
            elif matrix[mid_row][mid_col] > target:
                end = mid - 1
            else:
                start = mid + 1

        return [-1, -1]

print(Solution().search([[1, 2, 3], [4, 5,7], [8, 9, 10]], target=7))     # [1, 2]
print(Solution().search([[1, 2, 3], [4, 5,7], [8, 9, 10]], target=6))     # [-1, -1]
