# https://leetcode.com/problems/find-pivot-index/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        x = 0
        
        for i in range(len(nums)):
            if x == total - x - nums[i]:
                return i
            x += nums[i]
        
        return -1
