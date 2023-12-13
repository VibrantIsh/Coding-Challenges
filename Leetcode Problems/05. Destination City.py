# https://leetcode.com/problems/destination-city/
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return (set(dest for _, dest in paths) - set(src for src, _ in paths)).pop()
