 # https://leetcode.com/problems/greatest-common-divisor-of-strings/
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        gcd_length = gcd(len(str1), len(str2))
        gcd_str = str1[:gcd_length]

        return gcd_str if str1 == gcd_str * (len(str1) // gcd_length) and str2 == gcd_str * (len(str2) // gcd_length) else ""
