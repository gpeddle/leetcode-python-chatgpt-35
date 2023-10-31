# palindromeNumber

To determine if an integer is a palindrome without converting it to a string, you can reverse the integer and compare it with the original value. Here's an implementation of the `isPalindrome` method:

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_x = 0
        while x > reversed_x:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10

        return x == reversed_x or x == reversed_x // 10
```

This code reverses the integer `x` while ensuring that it is a positive integer (negative integers and multiples of 10 cannot be palindromes). It then compares the original and reversed values to determine if `x` is a palindrome. You can create an instance of the `Solution` class and call the `isPalindrome` method with your input integer to check if it's a palindrome.