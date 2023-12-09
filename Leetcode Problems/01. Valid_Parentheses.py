#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s):  
        stack = []
        a = {')': '(', '}': '{', ']': '['}

        for b in s:
            if b in a:
                if not stack or stack.pop() != a[b]:
                    return False
            else:
                stack.append(b)

        return not stack


