# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=0 
        for x_val in nums:
            if x<2 or x_val>nums[x - 2]:
                nums[x]=x_val
                x+=1
        return x

