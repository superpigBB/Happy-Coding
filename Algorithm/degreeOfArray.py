# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
#
# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6
# Note:
#
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.

## Solution 1
def degreeOfArray(arr):
    #
    # Write your code here.
    #
    if arr is None or len(arr) == 0:
        return -1

    dict = {}
    for index in range(len(arr)):
        num = arr[index]
        if num not in dict:
            dict[num] = {}
            dict[num]['cnt'] = 0
            dict[num]['indexes'] = []
        else:
            dict[num]['cnt'] += 1
        dict[num]['indexes'].append(index)

    max_degree = -1
    degree_nums = []
    for num in dict:
        if dict[num]['cnt'] > max_degree:
            max_degree = dict[num]['cnt']
            degree_nums = []
            degree_nums.append(num)
        elif dict[num]['cnt'] == max_degree:
            degree_nums.append(num)

    min_len = float('inf')
    for num in degree_nums:
        index_list = dict[num]['indexes']
        if index_list[-1] - index_list[0] < min_len:
            min_len = index_list[-1] - index_list[0]
    return min_len + 1

## Sultion 2
def degreeOfArray(arr):
    left, right, count = {}, {}, {}
    for i, x in enumerate(arr):
        if x not in left: left[x] = i
        right[x] = i
        count[x] = count.get(x, 0) + 1

    ans = len(arr)
    degree = max(count.values())
    for x in count:
        if count[x] == degree:
            ans = min(ans, right[x] - left[x] + 1)

    return ans

print(degreeOfArray([5,1,2,2,3,1]))
print(degreeOfArray([6,1,1,2,1,2,2]))
print(degreeOfArray([17,802,88, 747, 23, 160, 681, 254, 46, 663, 752, 741, 857, 802, 387, 790, 528, 93]))