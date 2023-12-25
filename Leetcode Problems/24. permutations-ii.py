# https://leetcode.com/problems/permutations-ii/
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(permutations(nums)))



# OR

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        x = []

        def ss(p, remaining):
            if len(remaining) == 0:
                if p not in x:
                    x.append(p[:])
                return 
            ch = remaining[0]
            for i in range(len(p) + 1):
                ss(p[0:i] + [ch] + p[i:], remaining[1:])
        nums.sort()
        ss([], nums)
        return x
