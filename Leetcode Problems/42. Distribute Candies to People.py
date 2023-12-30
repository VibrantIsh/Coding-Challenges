# https://leetcode.com/problems/distribute-candies-to-people/description/

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        a, i, c = [0] * num_people, 0, 1
        while candies > 0:
            a[i % num_people] += min(candies, c)
            candies -= c
            c += 1
            i += 1
        return a
