"""Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example
Consider the following matrix:

[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.

Challenge
O(log(n) + log(m)) time
"""

"""
思路过程：
matrix  m * n 
row 1 
    ...  => sorted integers 
    m  

1 3  5  7
9 10 13 15 

find target
return => True/False

如果硬做， Time: O(n * m), Space:O（1）
但如果要优化做，就要用到两次二分： Time: O(log(m) + log(n)), Space: O(1) 
"""


class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    """
    方法一： 两次二分： 先确定大概在哪个row, 然后确定column
    Time: O(log(n) + log(m)), Space: O(1)
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        ### corner cases
        if len(matrix) == 0 or matrix is None:
            return False

        m, n = len(matrix), len(matrix[0])

        ## compare target with start of medium row and get two rows at the end
        start_row, end_row = 0, m - 1
        while start_row + 1 < end_row:
            med_row = (start_row + end_row) // 2
            ## compare the first value of the row with target value
            if target == matrix[med_row][0]:
                return True
            elif target < matrix[med_row][0]:
                end_row = med_row - 1
            else:  ## target > matrix[med_row][0]
                start_row = med_row

        ## get two rows and compare with the last value of each rows
        if matrix[start_row][-1] == target or matrix[end_row][-1] == target:
            return True
        if matrix[start_row][-1] < target:
            target_row = end_row
        if matrix[start_row][-1] > target:
            target_row = start_row

        ## 二分法search target所在的那row的位置， 如果找不到return False
        start_col, end_col = 0, n - 1
        while start_col + 1 < end_col:
            med_col = (start_col + end_col) // 2
            if target == matrix[target_row][med_col]:
                return True
            elif target < matrix[target_row][med_col]:
                end_col = med_col - 1
            else:
                start_col = med_col + 1

        if matrix[target_row][start_col] == target:
            return True
        if matrix[target_row][end_col] == target:
            return True
        return False


    """
    方法二：直接确定medium position所在的column and row， 和target进行比较
    Time: O(log(n * m)) = O(log(n) + log(m)), Space: O(1)
    """

    def searchMatrix2(self, matrix, target):
        # write your code here
        ## corner cases
        if matrix is None or len(matrix) == 0:
            return False

        m, n = len(matrix), len(matrix[0])
        start, end = 0, n * m - 1  ## 如果把list里元素全展开的index值

        while start + 1 < end:
            mid_pos = (start + end) // 2
            mid_row = mid_pos // n
            mid_col = mid_pos % n

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                start = mid_pos + 1
            else:
                end = mid_pos - 1

        start_row, start_col = start // n, start % n
        end_row, end_col = end // n, end % n

        if matrix[start_row][start_col] == target:
            return True
        if matrix[end_row][end_col] == target:
            return True

        return False


