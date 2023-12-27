# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = reduce(lambda x, y: x * y if y != 0 else x, nums, 1)
        zero_count = nums.count(0)
        
        if zero_count > 1:
            return [0] * len(nums)
        elif zero_count == 1:
            return [total_product if num == 0 else 0 for num in nums]
        else:
            return [total_product // num for num in nums]
