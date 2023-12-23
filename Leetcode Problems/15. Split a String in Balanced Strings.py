# https://leetcode.com/problems/split-a-string-in-balanced-strings
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        x = 0
        b = 0

        for x_char in s:
            if x_char == 'R':
                x += 1
            else:
                x -= 1
            
            if x == 0:
                b += 1

        return b
