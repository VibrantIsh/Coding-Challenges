class Solution:
    def ishappy(self, n):
        seen = set()

        while n != 1 and n not in seen:
            seen add(n)
            n = self.square_sum_of_digits(n)

        return n == 1

    def square_sum_of_digits(self, num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total

solution = Solution()
