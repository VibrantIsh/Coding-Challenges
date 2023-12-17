# https://leetcode.com/problems/maximum-69-number/
class Solution:
    def maximum69Number(self, num: int) -> int:
        digits_list = list(str(num))

        for i in range(len(digits_list)):
            if digits_list[i] == '6':
                digits_list[i] = '9'
                break

        return int(''.join(digits_list))
