# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums):
        nums[:] = sorted(set(nums))
