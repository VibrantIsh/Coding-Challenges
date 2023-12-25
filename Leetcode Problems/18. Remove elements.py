# https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], x: int) -> int:
        # Keep ditching 'x' from 'nums' until it's all gone
        while x in nums:
            nums.remove(x)

