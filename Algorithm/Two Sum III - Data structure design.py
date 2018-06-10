# Design and implement a TwoSum class. It should support the following operations: add and find.
#
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
#
# For example,
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false

### Original Method
# wrong since if [0,0,0], then dict[val] is all 3, which means dict[val] always == dict[value -val] if val == value - val even there are multiple of them
# one key can only have one value
# class TwoSum(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.dict = {}
#         self.i = 0
#     def add(self, number):
#         """
#         Add the number to an internal data structure..
#         :type number: int
#         :rtype: void
#         """
#         self.dict[number] = self.i
#         self.i += 1
#
#     def find(self, value):
#         """
#         Find if there exists any pair of numbers which sum is equal to the value.
#         :type value: int
#         :rtype: bool
#         """
#         found = 0
#         for val in self.dict:
#             if value - val in self.dict and self.dict[val] != self.dict[value - val]:
#                 found = 1
#         return found == 1

### Method 2: debug the original script: create hash to store numbers and then find if target - val == value and if target - val== val and dict[key] > 1 (occurrance is multiple)
### 515s
# class TwoSum(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.dict = {}
#     def add(self, number):
#         """
#         Add the number to an internal data structure..
#         :type number: int
#         :rtype: void
#         """
#         if number not in self.dict:
#             self.dict[number] = 1
#         else:
#             self.dict[number] += 1
#
#     def find(self, value):
#         """
#         Find if there exists any pair of numbers which sum is equal to the value.
#         :type value: int
#         :rtype: bool
#         """
#         found = 0
#         for val in self.dict:
#             if value - val in self.dict and ((value - val) != val or ((value - val) == val and self.dict[val] > 1)):
#                 found = 1
#         return found == 1


### Method3
### still use hash but add min val in hash values and max val in hash values since I found the earlier return something, may avoid the O(N) time complexity
### use the min_val and max_val to get minimum or maximum value of dict keys => Line 28: AttributeError: 'TwoSum' object has no attribute 'min_val', for example
### ["TwoSum","find"]
##  [[],[0]]
### There are no value added into obj, then it might have the attributeerror of min_val or max_val, thus we need to avoid iterate the hash but find the min or max
### when add the number => Method 3.2

# class TwoSum(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.dict = {}
#     def add(self, number):
#         """
#         Add the number to an internal data structure..
#         :type number: int
#         :rtype: void
#         """
#         if number not in self.dict:
#             self.dict[number] = 1
#         else:
#             self.dict[number] += 1
#         self.min_val = min(self.dict.iterkeys())
#         self.max_val = max(self.dict.iterkeys())
#         # print self.min_val, self.max_val
#
#     def find(self, value):
#         """
#         Find if there exists any pair of numbers which sum is equal to the value.
#         :type value: int
#         :rtype: bool
#         """
#         if self.min_val * 2 > value or self.max_val * 2 < value:
#             return False
#         for val in self.dict:
#             target = value - val
#             if target in self.dict and ( self.dict[target] > 1 or target != val ):
#                 return True
#         return False

### Method 3.2 get min/max when add each number, others keep the same as Method 3

### Turns out   very successfully => 92ms O(N) time complexity and O(N) Space Complexity
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.min_val = float('inf')
        self.max_val = float('-inf')

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number not in self.dict:
            self.dict[number] = 1
        else:
            self.dict[number] += 1
        self.min_val = min(number, self.min_val)
        self.max_val = max(number, self.max_val)
        # print self.min_val, self.max_val

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if self.min_val * 2 > value or self.max_val * 2 < value:
            return False
        for val in self.dict:
            target = value - val
            if target in self.dict and ( self.dict[target] > 1 or target != val ):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
obj = TwoSum()
obj.add(1); obj.add(3); obj.add(5)
print (obj.find(4))
print (obj.find(7))
obj = TwoSum()
obj.add(0); obj.add(0); obj.add(0)
print (obj.find(0))