# https://leetcode.com/problems/unique-number-of-occurrences/
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        x = {}
        for n in arr:
            if n in x:
                x[n] += 1
            else:
                x[n] = 1
        return len(set(x.values())) == len(x)
