# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
class Solution:
    def average(self, x: List[int]) -> float:
        x = sorted(x)
        x.pop(0)
        x.pop(-1)
        return sum(x) / float(len(x))
