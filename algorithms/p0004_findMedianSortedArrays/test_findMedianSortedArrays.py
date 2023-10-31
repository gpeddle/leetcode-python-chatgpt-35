# findMedianSortedArrays

import pytest
from .solution import Solution
from typing import List

# revise test_data to match problem statement
test_data = [
    {
        'name': 'Example 1',
        'nums1': [1,3],
        'nums2': [2],
        'expected': 2.0
    },
    {
        'name': 'Example 2',
        'nums1': [1,2],
        'nums2': [3,4],
        'expected': 2.5
    },
]

@pytest.mark.parametrize("test_case", test_data)
def test_solution(test_case):
    solution = Solution()
    result = solution.findMedianSortedArrays(test_case['nums1'], test_case['nums2'])
    assert result == test_case['expected'], f"Test '{test_case['name']}' failed"
