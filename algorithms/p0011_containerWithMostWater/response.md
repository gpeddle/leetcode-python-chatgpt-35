# containerWithMostWater

To find the container that can hold the most water, you can use a two-pointer approach. Here's an implementation of the `maxArea` method:

```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_water = max(max_water, h * w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
```

This code initializes two pointers, `left` and `right`, at the beginning and end of the array. It then iterates through the array while keeping track of the maximum water container. The key is to move the pointer that points to the shorter wall inward, as moving the taller wall won't increase the area. This way, it efficiently finds the maximum water container. You can create an instance of the `Solution` class and call the `maxArea` method with your input list of heights to determine the maximum amount of water that can be stored.