class Solution(object):
    """
    解题思路: 利用Min HEAP， 并用set来记录每一个array所在array组里的位置和array里的位置
    Time: O(nlogk)
    Space: O(k)
    """

    def merge(self, arrayOfArrays):
        """
        input: int[][] arrayOfArrays
        return: int[]
        """
        # write your solution here
        # corner cases
        if not arrayOfArrays or len(arrayOfArrays) == 0:
            return []

        import heapq
        # store first element of each array into min heap
        heap = []

        for i in range(len(arrayOfArrays)):
            heapq.heappush(heap, (arrayOfArrays[i], i, 0))

        result = []
        while heap:
            e, array_i, e_i = heapq.heappop(heap)
            result.append(e)
            if e_i + 1 < len(arrayOfArrays[array_i]):
                heapq.heappush(heap, (arrayOfArrays[array_i][e_i + 1], array_i, e_i + 1))

        return result

print (Solution().merge([[1,2], [5,8], [4, 7]]))