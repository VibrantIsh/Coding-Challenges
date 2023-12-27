# https://leetcode.com/problems/increasing-triplet-subsequence/
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = None
        for n in nums:
            if first is None or n <= first:
                first = n
            elif second is None or n <= second:
                second = n
            else:
                return True
        return False

