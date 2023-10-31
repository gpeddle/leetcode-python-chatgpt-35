# lengthOfLongestSubstring

import pytest
from .solution import Solution

# revise test_data to match problem statement
test_data = [
    {
        'name': 'Example 1',
        'input': 'abcabcbb',
        'expected': 3
    },
    {
        'name': 'Example 2',
        'input': 'bbbbb',
        'expected': 1
    },
    {
        'name': 'Example 3',
        'input': 'pwwkew',
        'expected': 3
    }
]

@pytest.mark.parametrize("test_case", test_data)
def test_solution(test_case):
    solution = Solution()
    result = solution.lengthOfLongestSubstring(test_case['input'])
    assert result == test_case['expected'], f"Test '{test_case['name']}' failed"
