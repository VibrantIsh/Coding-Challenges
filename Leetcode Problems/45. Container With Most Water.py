# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, h: List[int]) -> int:
        w, l, r = 0, 0, len(h) - 1

        while l < r:
            w = max(w, min(h[l], h[r]) * (r - l))
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1

        return w

