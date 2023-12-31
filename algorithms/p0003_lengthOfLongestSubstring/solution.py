# lengthOfLongestSubstring

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
