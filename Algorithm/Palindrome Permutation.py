# Given a string, determine if a permutation of the string could form a palindrome.
#
# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.

### Original method
### almost the same with longest Palidrome , with time O(N) and space O(1)
### 57%
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) == 1:
            return True
        odd_cnt = 0
        for element in set(s):
            count = s.count(element)
            if count % 2 != 0:
                odd_cnt += 1

        if odd_cnt > 1:
            return False
        else:
            return True

obj = Solution()
print (obj.canPermutePalindrome('code'))
print (obj.canPermutePalindrome('aab'))
print (obj.canPermutePalindrome('carerac'))
print (obj.canPermutePalindrome('c'))
print (obj.canPermutePalindrome(''))
