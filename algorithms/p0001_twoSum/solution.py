from typing import List

class Solution:
    def twoSum(self, input: List[int], target: int) -> List[int]:
    
        # Create a dictionary to store the numbers and their indices
        num_indices = {}

        for index, num in enumerate(input):
            complement = target - num
            # Check if the complement exists in the dictionary
            if complement in num_indices:
                # Return the indices of the two numbers that add up to the target
                return [num_indices[complement], index]
            # Store the current number and its index in the dictionary
            num_indices[num] = index

        # If no solution is found, return an empty list
        return []

