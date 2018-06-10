#
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


### Solution 1 and 1.1不知道为什么在时间复杂度都是O（N^2）情况下还是会超时

### Solution 1: take one number of list as i, and a number not equals to that number equals j => target= t1 + t2, t1=>i, t2=>j
### use sorted in two loops: exceed time limit!
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list = []
        dict = {}
        for i in range(len(nums)):
            ## target t1 = 0 - nums[i]
            t1 = -nums[i]
            for j in range(len(nums)):
                if j == i:
                    continue
                ## target t2 = t1 - list[j]
                t2 = t1 - nums[j]
                if t2 in dict.values() and sorted([-t1, nums[j], t2]) not in list:
                    list.append(sorted([-t1, nums[j], t2]))
                if j not in dict:
                    dict[j] = nums[j]
            dict = {}
        return list

# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))  #[[-1, 0, -1], [-1, 2, -1]]
# print(Solution().threeSum([1,2,1,1,1]))          # -1
# print(Solution().threeSum([0, 0, 0, 0, 0]))        #[[-1, 0, -1], [-1, 2, -1]]
# print("\n")

### Solution 1.1: take one number of list as i, and a number not equals to that number equals j => target= t1 + t2, t1=>i, t2=>j
### try removing sorted from the loop, add manual sort into loop => the same problem: time limit exceeded!!!
### Time O(N^2), Space O(1)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list = []
        dict = {}
        for i in range(len(nums)):
            ## target t1 = 0 - nums[i]
            t1 = -nums[i]
            for j in range(len(nums)):
                if j == i:
                    continue
                ## target t2 = t1 - list[j]
                t2 = t1 - nums[j]
                if t2 in dict.values():
                    ## set first, second, third to sort element in list first
                    if t2 >= -t1 and t2 >= nums[j]:
                        first = t2
                        if -t1 >= nums[j]:
                            second = -t1
                            third = nums[j]
                        else:
                            second = nums[j]
                            third = -t1
                    elif -t1 >= t2 and -t1 >= nums[j]:
                        first = -t1
                        if t2 >= nums[j]:
                            second = t2
                            third = nums[j]
                        else:
                            second = nums[j]
                            third = t2
                    elif nums[j] >= -t1 and nums[j] >= t2:
                        first = nums[j]
                        if -t1 >= t2:
                            second = -t1
                            third = t2
                        else:
                            second = t2
                            third = -t1

                    if [first, second, third] not in list:
                        list.append([first, second, third])
                if j not in dict:
                    dict[j] = nums[j]
            dict = {}

        return list
        # ### sort list to get sorted list and remove duplicates
        # unique_list = []
        # for l in list:


# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))  #[[-1, 0, -1], [-1, 2, -1]]
# print(Solution().threeSum([1,2,1,1,1]))          # -1
# print(Solution().threeSum([0, 0, 0, 0, 0]))        #[[-1, 0, -1], [-1, 2, -1]]
# print("\n")


### Solution 1.2: same as Solution1 but sort first let's see how it works
### the same problem: time limit exceeded!!!
### Time O(N^2), Space O(1)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list = []
        dict = {}
        nums = sorted(nums)
        prev_first = float('inf')
        for i in range(0, len(nums) -2):
            t1 = 0 - nums[i]
            if t1 == prev_first:
                continue
            for j in range(i+1, len(nums)):
                t2 = t1 - nums[j]
                if t2 in dict.values() and sorted([-t1, t2, nums[j]]) not in list:
                    list.append(sorted([-t1, t2, nums[j]]))

                dict[j] = nums[j]
            dict = {}
            ## set previous first variable to save the previous first value, if encounter the same then skip
            prev_first = t1

        return list


# print(Solution().threeSum([-2,0,0,2,2]))           #[-2, 0, 2]
# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))  #[[-1, 0, -1], [-1, 2, -1]]
# print(Solution().threeSum([1,2,1,1,1]))          # -1
# print(Solution().threeSum([0, 0, 0, 0, 0]))        #[[-1, 0, -1], [-1, 2, -1]]
# print(Solution().threeSum([1,2,-2,-1])) #[]
# print("\n")


### Solution 2: sort list first and then use two pointers
### Time O(N^2), Space O(1)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## sort nums first
        nums = sorted(nums)
        list = []

        if len(nums) < 3 or not nums:
            return list

        if all ( num == 0 for num in nums) and len(nums) >=3:
            # print(nums)
            return [[0,0,0]]

        for i in range(0, len(nums) -2):
            if nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]

            ## set up left and right as two pointers to match target value
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right]
                if total < target:
                    left += 1
                elif total > target:
                    right -=1
                else:
                    list.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -= 1

                    ## skip duplicate pairs with the same left
                    while left < right and nums[left] == nums[left - 1]:
                        left +=1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return list

# print(Solution().threeSum([-2,0,0,2,2]))           #[-2, 0, 2]
# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))  #[[-1, 0, -1], [-1, 2, -1]]
# print(Solution().threeSum([1,2,1,1,1]))            # []
# print(Solution().threeSum([0, 0, 0, 0, 0]))        #[[-1, 0, -1], [-1, 2, -1]]
# print(Solution().threeSum([1,2,-2,-1]))            #[]
# print("\n")


### Solution 2.1: sort list first and then use two pointers -- another way to process [0,0,0,0,...]
### Time O(N^2), Space O(1)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## sort nums first
        nums = sorted(nums)
        list = []

        if len(nums) < 3 or not nums:
            return list

        for i in range(0, len(nums) -2):
            if nums[i] == nums[i-1] and i != 0:
                continue
            target = 0 - nums[i]

            ## set up left and right as two pointers to match target value
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right]
                if total < target:
                    left += 1
                elif total > target:
                    right -=1
                else:
                    list.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -= 1

                    ## skip duplicate pairs with the same left
                    while left < right and nums[left] == nums[left - 1]:
                        left +=1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return list

# print(Solution().threeSum([-2,0,0,2,2]))           #[-2, 0, 2]
# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))  #[[-1, 0, -1], [-1, 2, -1]]
# print(Solution().threeSum([1,2,1,1,1]))            # []
# print(Solution().threeSum([0, 0, 0, 0, 0]))        #[[-1, 0, -1], [-1, 2, -1]]
# print(Solution().threeSum([1,2,-2,-1]))            #[]
# print("\n")


### Solution 3: from online best solution in leetcode: use dict, but found problematic on lintcode but I think ours correct
### Time O(N^2), Space O(N)
class Solution:
    def threeSum(self, nums):
        dic={}
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        if 0 in dic and dic[0]>=3:
            ans=[[0,0,0]]
        else:
            ans=[]
        ns = sorted([x for x in dic if x<0], reverse=True)
        nns = sorted([x for x in dic if x>=0])
        for n in ns:
            for nn in nns:
                chk = -(nn + n)
                if chk in dic:
                    if chk in [n,nn] and dic[chk] > 1:
                        ans.append([n, chk, nn])
                    elif chk<n:
                        ans.append([chk, n, nn])
                    elif nn<chk:
                        ans.append([n,nn,chk])
        return ans

print(Solution().threeSum([-2,0,0,0,2]))           #[-2, 0, 2], [0,0,0]
print(Solution().threeSum([-2,0,0,2,2]))           #[-2, 0, 2]
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))  #[[-1, 0, -1], [-1, 2, -1]]
print(Solution().threeSum([1,2,1,1,1]))            # []
print(Solution().threeSum([0, 0, 0, 0, 0]))        #[[-1, 0, -1], [-1, 2, -1]]
print(Solution().threeSum([1,2,-2,-1]))            #[]
print("\n")