# lengthOfLongestSubstring

To find the length of the longest substring without repeating characters, you can use a sliding window approach. Here's an implementation of the `lengthOfLongestSubstring` method:

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_indices = {}  # Store the indices of characters in the string
        max_length = 0  # Initialize the maximum length
        start = 0  # Initialize the start of the sliding window

        for end in range(len(s)):
            if s[end] in char_indices and char_indices[s[end]] >= start:
                # If the character is repeated and the previous occurrence is within the window,
                # update the start of the window to the next index of the repeated character
                start = char_indices[s[end]] + 1

            # Update the index of the current character
            char_indices[s[end]] = end

            # Calculate the current window length and update the maximum length
            current_length = end - start + 1
            max_length = max(max_length, current_length)

        return max_length
```

This code iterates through the string using a sliding window and maintains a dictionary to store the indices of characters in the string. When a character is repeated, it updates the start of the window to the next index of the repeated character. It calculates the current window length and updates the maximum length. You can create an instance of the `Solution` class and call the `lengthOfLongestSubstring` method with your input string to find the length of the longest substring without repeating characters.