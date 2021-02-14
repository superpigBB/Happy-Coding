class Solution(object):
    """
    Time: O(nlogn)
    Space: O(n)
    """

    def mergeSort(self, array):
        """
        input: int[] array
        return: int[]
        """
        # write your solution here
        # corner cases
        if array is None or len(array) == 0 or len(array) == 1:
            return array

        start, end = 0, len(array) - 1
        result = [0] * len(array)
        self.mergesort(array, start, end, result)
        return array

    def mergesort(self, array, start, end, result):
        # base cases
        if start >= end:
            return

        mid = (start + end) // 2
        self.mergesort(array, start, mid, result)
        self.mergesort(array, mid + 1, end, result)

        self.merge(array, start, mid, end, result)

    def merge(self, array, start, mid, end, result):
        i, j = start, mid + 1
        index = start
        while i <= mid and j <= end:
            if array[i] <= array[j]:
                result[index] = array[i]
                i += 1
            else:
                result[index] = array[j]
                j += 1

            index += 1

        while i <= mid:
            result[index] = array[i]
            i += 1
            index += 1
        while j <= end:
            result[index] = array[j]
            j += 1
            index += 1

        for i in range(start, end + 1):
            array[i] = result[i]



print(Solution().mergeSort([3, 5, 1, 2, 4, 8]))