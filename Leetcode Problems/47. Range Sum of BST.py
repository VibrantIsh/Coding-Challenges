# https://leetcode.com/problems/range-sum-of-bst/
class Solution:
    def rangeSumBST(self, r: Optional[TreeNode], l: int, h: int) -> int:
        if not r: return 0
        v = r.val if l <= r.val <= h else 0
        left = self.rangeSumBST(r.left, l, h)
        right = self.rangeSumBST(r.right, l, h)
        return v + left + right
