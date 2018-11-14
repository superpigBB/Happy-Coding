"""
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected,
i.e., there is only one black region. Pixels are connected horizontally and vertically.
Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Example
For example, given the following image:

[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2,
Return 6.
"""

"""
思路过程：
values: 0->white 1->black->connected
行和列应该都是连续的 => 才能用二分法
如果不连续=> BFS

可以找到上下左右的离boundary最近的那个1=>等同于各找一半
Time: O(nlog(m) + mlog(n)), Space: O(1)

0 0 1 0 
0 1 1 0
0 1 0 0 
"""


class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    """
    Solution1: 二分法 => 二分模板， 烦的是最后还要比较到底用start 还是 end，等同于额外再加个O(N/M)    
    image is a matrix
    Time: O(nlog(m) + mlog(n)), Space: O(1)
    """

    def minArea(self, image, x, y):
        # write your code here
        ## corner cases
        if len(image) == 0 or image is None or len(image[0]) == 0:
            return 0

        row = len(image)
        col = len(image[0])
        ## find top boundary row: 0 - x: first row  from the top shows 1
        top = self.findtop(image, 0, x)
        bottom = self.findbottom(image, x, row - 1)
        left = self.findleft(image, 0, y, row)
        right = self.findright(image, y, col - 1, row)

        print("top:{}, bottom:{}, left:{}, right:{}".format(top, bottom, left, right))
        ## calculate the rectangle area
        return (bottom - top + 1) * (right - left + 1)

    """
    find first row contains 1 
    """

    def findtop(self, matrix, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            sum_result = 0
            for num in matrix[mid]:
                sum_result += eval(num)
                if num == '1':
                    end = mid
                    break
            if sum_result == 0:
                start = mid + 1

        for num in matrix[start]:
            if num == '1':
                return start
        for num in matrix[end]:
            if num == '1':
                return end

    """
    find last row contains 1 
    """

    def findbottom(self, matrix, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            sum_result = 0
            for num in matrix[mid]:
                sum_result += eval(num)
                if num == '1':
                    start = mid
                    break
            if sum_result == 0:
                end = mid - 1

        for num in matrix[end]:
            if num == '1':
                return end
        for num in matrix[start]:
            if num == '1':
                return end

    """
    find keft row contains 1 
    """

    def findleft(self, matrix, start, end, rowLen):
        while start + 1 < end:
            mid = (start + end) // 2
            sum_result = 0
            ## loop column
            for row in range(rowLen):
                sum_result += eval(matrix[row][mid])
                if matrix[row][mid] == '1':
                    end = mid
                    break
            if sum_result == 0:
                start = mid + 1

        for row in range(rowLen):
            if matrix[row][start] == '1':
                return start
        for row in range(rowLen):
            if matrix[row][end] == '1':
                return end


    """
    find right row contains 1 
    """


    def findright(self, matrix, start, end, rowLen):
        while start + 1 < end:
            mid = (start + end) // 2
            sum_result = 0
            ## loop column
            for row in range(rowLen):
                sum_result += eval(matrix[row][mid])
                if matrix[row][mid] == '1':
                    start = mid
                    break
            if sum_result == 0:
                end = mid - 1

        for row in range(rowLen):
            if matrix[row][end] == '1':
                return end
        for row in range(rowLen):
            if matrix[row][start] == '1':
                return start

########################################################################################################################
    """
    Solution2: 二分法，但没用模板，在计算mid的时候做了点trick,让一个靠前一个靠后， 但省去了O(N/M）的复杂度，所以可能快点
    """
    def minArea2(self, image, x, y):
        # write your code here
        row = len(image)
        col = len(image[0])
        if not row or not col:
            return 0

        # find the right border
        start = y
        end = col - 1
        while start < end:
            mid = start + (end - start) // 2 + 1
            if self.checkCol(image, mid):
                start = mid
            else:
                end = mid - 1
        right = start

        # find the left border
        start = 0
        end = y
        left = y
        while start < end:
            # if self.checkCol(image,start):
            #     left=start
            #     break
            mid = start + (end - start) // 2
            if self.checkCol(image, mid):
                end = mid
            else:
                start = mid + 1
        left = start

        # find the top border

        start = 0
        end = x
        top = 0
        while start < end:

            # if self.checkRow(image,start):
            #     top=start
            #     break
            mid = start + (end - start) // 2
            if self.checkRow(image, mid):
                end = mid
            else:
                start = mid + 1

        top = start

        # find the bottom border
        start = x
        end = row - 1
        bottom = row - 1
        while start < end:
            # if self.checkRow(image,end):
            #     bottom=end
            #     break
            mid = start + (end - start) // 2 + 1
            if self.checkRow(image, mid):
                start = mid
            else:
                end = mid - 1
        bottom = start

        return (right - left + 1) * (bottom - top + 1)

    def checkCol(self, image, col):
        for i in range(len(image)):
            if image[i][col] == '1':
                return True
        return False

    def checkRow(self, image, row):
        for i in range(len(image[0])):
            if image[row][i] == '1':
                return True
        return False



# print(Solution().minArea([
#   "0010",
#   "0110",
#   "0100"
# ], 0, 2))
#



