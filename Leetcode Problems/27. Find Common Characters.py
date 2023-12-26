# https://leetcode.com/problems/find-common-characters/
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
           return (list(reduce(lambda x, y: x & Counter(y), words, Counter(words[0])).elements())if words else [])
