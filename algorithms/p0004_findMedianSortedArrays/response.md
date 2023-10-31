This problem involves finding the median of two sorted arrays efficiently. Here's an implementation of the `findMedianSortedArrays` method using the concept of binary search:

```python
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # Ensure nums1 is the shorter array.

        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            if i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0: max_of_left = nums2[j - 1]
                elif j == 0: max_of_left = nums1[i - 1]
                else: max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return float(max_of_left)

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0
```

This code finds the median of two sorted arrays, `nums1` and `nums2`, in O(log(min(m, n)) time complexity, where `m` and `n` are the lengths of the two arrays. You can create an instance of the `Solution` class and call the `findMedianSortedArrays` method with your input arrays to get the median.