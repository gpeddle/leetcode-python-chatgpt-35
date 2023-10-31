# twoSum

To solve the "Two Sum" problem efficiently, you can use a dictionary to store the indices of elements as you iterate through the array. This way, you can quickly check if the complement of the current element is present in the dictionary. Here's an implementation of the `twoSum` method:

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}  # Store indices of numbers

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i

        return []  # No solution found
```

This code iterates through the array, storing the indices of numbers in a dictionary. It checks if the complement of the current number is in the dictionary, indicating that a pair with the given sum has been found. You can create an instance of the `Solution` class and call the `twoSum` method with your input list of numbers and the target sum to get the indices of the two numbers that add up to the target.