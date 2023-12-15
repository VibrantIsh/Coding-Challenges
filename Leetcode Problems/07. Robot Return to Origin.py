# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        i = j = 0
        for a in moves:
            if a == 'L':
                j -= 1
            elif a == 'R':
                j += 1
            elif a == 'U':
                i -= 1
            else:
                i += 1
        return i == j == 0
