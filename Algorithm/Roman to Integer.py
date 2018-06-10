# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.

### Reference for Roman numerals https://en.wikipedia.org/wiki/Roman_numerals

### Solution 1: utilize dict to store the roman numerics mapping to decimal numeric
### Time Compleixty O(N), Space Complexity O(N)
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        i = 0
        dict= {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X':10, 'V':5, 'I':1}
        for i in range(len(s) - 1):
            if dict[s[i]] >= dict[s[i+1]]:
                num += dict[s[i]]
            else:
                num -= dict[s[i]]
            i += 1
        num += dict[s[-1]]
        return num

### Solution 2: instead cost space, we directly create another helper function numeric(char) to transform from roman to decimal numeric
### Time Complexity O(N), Space complexity O(1)

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        i = 0

        for i in range(len(s) - 1):
            if self.numeric(s[i]) >= self.numeric(s[i + 1]):
                num += self.numeric(s[i])
            else:
                num -= self.numeric(s[i])
            i += 1
        num += self.numeric(s[-1])
        return num

    def numeric(self, char):
        if char == 'M':
            num = 1000
        elif char == 'D':
            num = 500
        elif char == 'C':
            num = 100
        elif char == 'L':
            num =  50
        elif char == 'X':
            num = 10
        elif char == 'V':
            num =  5
        else:
            num = 1
        return num