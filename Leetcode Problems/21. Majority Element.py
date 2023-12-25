# https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return max(counter, key=counter.get)
        
