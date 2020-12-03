"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"
 

Constraints:

1 <= s.length, t.length <= 105
s and t consist of English letters.
 

Follow up: Could you find an algorithm that runs in O(n) time?

"""


class Solution:
    """
    解题思路： window size要最小并且含所有t里的元素， 则设左右指针，右指针找所有满足条件元素，
    左指针负责缩小范围，直到左右指针相遇并右指针到头
    Time: O(n)
    Space: O(n)
    """

    def minWindow(self, s: str, t: str) -> str:
        # corner cases
        if s == t or t == '' or s == '':
            return s

        from collections import defaultdict
        # scan t and return dict target: {e: cnt(>= 1)}
        target = defaultdict(int)
        for e in t:
            target[e] += 1

        left, right = 0, 0
        min_len = float('inf')
        target_char_cnt = len(t)
        result = ''

        while right < len(s):
            # 查找满足条件的substring
            if target[s[right]] > 0:
                target_char_cnt -= 1
            target[s[right]] -= 1
            right += 1

            # 找到了substring然后开始缩left指针
            while target_char_cnt == 0:
                if min_len > right - left:
                    min_len = right - left
                    result = s[left:right]
                # 左指针所在位置是t里面的元素
                if target[s[left]] == 0:
                    target_char_cnt += 1
                target[s[left]] += 1
                left += 1

        return result





