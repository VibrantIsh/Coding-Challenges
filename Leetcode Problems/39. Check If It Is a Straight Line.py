#https://leetcode.com/problems/check-if-it-is-a-straight-line/
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        return all((y - y1) * (x1 - x0) == (y1 - y0) * (x - x1) for x, y in coordinates[2:])
