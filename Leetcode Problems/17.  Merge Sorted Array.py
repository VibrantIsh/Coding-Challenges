# https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x = len(nums1) - m
        for i in range(x):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()
