# https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        jewel_count = sum(1 for stone in stones if stone in jewel_set)
        return jewel_count
