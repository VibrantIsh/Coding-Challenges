# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        x = nums.count(0)
        nums[:] = [num for num in nums if num != 0]
        nums.extend([0] * x)

