# lengthOfLongestSubstring

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a dictionary to store the last seen index of each character in the string.
        char_index = {}
        max_length = 0
        start = 0  # The starting index of the current substring.

        for end, char in enumerate(s):
            # If the character is already in the dictionary and its index is greater than or equal to the start of the current substring,
            # update the start index to the next index of that character.
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1

            # Update the last seen index of the character.
            char_index[char] = end

            # Update the maximum length if the current substring is longer.
            max_length = max(max_length, end - start + 1)

        return max_length

