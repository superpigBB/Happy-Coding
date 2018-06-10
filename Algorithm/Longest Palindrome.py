# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

### Original Method
### check if odd length string > 1, each time encounter that, then total length - 1
### O(N)-> time  O(1) -> space => 96%
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1 or len(s) == 0:
            return len(s)
        odd_cnt, total = 0, 0
        for element in set(s):
            count = s.count(element)
            if count % 2 != 0:
                odd_cnt += 1
                if odd_cnt > 1:
                    total -=1
            total += count
        return total

obj = Solution()
print (obj.longestPalindrome("abccccdd"))
print (obj.longestPalindrome("abcd"))
print (obj.longestPalindrome("a"))
print (obj.longestPalindrome(""))
print (obj.longestPalindrome("acbca"))
print (obj.longestPalindrome("acbbbca"))
print (obj.longestPalindrome("ab"))

