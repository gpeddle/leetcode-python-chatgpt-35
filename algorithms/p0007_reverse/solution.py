# Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        result = 0

        # Handle negative numbers
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            pop = x % 10
            x //= 10

            # Check for overflow before updating the result
            if (result > INT_MAX // 10) or (result == INT_MAX // 10 and pop > 7):
                return 0
            if (result < INT_MIN // 10) or (result == INT_MIN // 10 and pop < -8):
                return 0

            result = result * 10 + pop

        return result * sign


