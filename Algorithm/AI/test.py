"""Corner Cases: better ask interviewer to confirm return value for corner cases"""
if list is None or len(list) == 0 or k == 0:
    return []

"""find closest element from target first in list: 
   利用helper function call binary search first to get closest index 
   make that closet element a centered value and set two pointers i & j to get the k closest  
"""
i = self.findLowerClosest(A, target)
j = i + 1
return_list = list  # return A to store sorted elemets according to |e.value - target|

"""这一段找k个element的入list的过程是enhanced的，只是喜欢这个的func design思想，别的没区别"""
for index in range(k):
    if j > len(A) - 1 or (i >= 0 and abs(A[i] - target) <= abs(A[j] - target)):
        return_list.append(A[i])
        i -= 1
    else:
        return_list.append(A[j])
        j += 1

return return_list

"""helper function for binary search"""


def findLowerClosest(self, A, target):
    start, end = 0, len(A) - 1
    """Removed closest_index 先定义，因为可以把找到的当成end，然后继续找最小的"""
    while start < end - 1:
        mid = (start + end) // 2
        if A[mid] == target:
            end = mid
        elif A[mid] > target:
            end = mid
        else:
            start = mid

    return start if abs(A[start] - target) <= abs(A[end] - target) else end