# regularExpressionMatching

To implement regular expression matching with support for '.' and '*', you can use a dynamic programming approach. Here's an implementation of the `isMatch` method:

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty pattern matches empty string
        dp[0][0] = True

        # Handle patterns with '*'
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

        return dp[m][n]
```

This code uses dynamic programming to match the input string `s` against the pattern `p`. It handles both '.' and '*' in the pattern. You can create an instance of the `Solution` class and call the `isMatch` method with your input string and pattern to check if they match.
