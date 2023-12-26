# https://leetcode.com/problems/merge-strings-alternately/
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lst = []
        ml = min(len(word1), len(word2)) 
        for x, y in zip(word1[:ml], word2[:ml]):  
            lst.append(x)
            lst.append(y)
        if len(word1) > len(word2):
            lst.extend(word1[ml:])
        elif len(word2) > len(word1):
            lst.extend(word2[ml:])
        string = "".join(lst)
        return string

