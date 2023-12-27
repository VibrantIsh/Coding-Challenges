# https://leetcode.com/problems/reverse-vowels-of-a-string/
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        reverse = [c for c in s if c in vowels][::-1]
        string = ''
        idx = 0
        for x in s:
            if x in vowels:
                string += reverse[idx]
                idx += 1
            else:
                string += x
        return string

