# stringToInteger

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        result = 0
        sign = 1
        i = 0

        # Remove leading whitespace
        while i < len(s) and s[i] == ' ':
            i += 1

        # Handle sign character
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Parse digits
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow before updating the result
            if (result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1

        return sign * result
