# https://leetcode.com/problems/combination-sum-iii/ 
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        x = [i for i in range(1, 10)]
        ans = []
        
        for i in itertools.combinations(x, k):
            if sum(i) == n:
                ans.append(list(i))
        
        return ans
