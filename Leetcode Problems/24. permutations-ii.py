# https://leetcode.com/problems/permutations-ii/
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(permutations(nums)))



# OR


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        c = []
        
        def y(nums, temp):
            if len(nums) == 0:
                c.append(temp)
                return
            for i in range(len(nums)):
                y(nums[:i] + nums[i+1:], temp + [nums[i]])
                
        y(nums, [])
        return set(tuple(ele) for ele in c)
