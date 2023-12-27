# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lst = []
        for x in zip(*strs):
            if len(set(x)) == 1:
                lst.append(x[0])
            else:
                break
        return ''.join(lst)
