# lengthOfLongestSubstring

import pytest
from .solution import Solution

# revise test_data to match problem statement
test_data = [
    {
        'name': 'Example 1',
        'input': [0, 0],
        'target': 0,
        'expected': [0, 0]
    },
    {
        'name': 'Example 2',
        'input': [0, 0],
        'target': 0,
        'expected': [0, 0]
    },
    {
        'name': 'Example 3',
        'input': [0, 0],
        'target': 0,
        'expected': [0, 0]
    }
]

@pytest.mark.parametrize("test_case", test_data)
def test_solution(test_case):
    solution = Solution()
    result = solution.lengthOfLongestSubstring(test_case['input'], test_case['target'])
    assert result == test_case['expected'], f"Test '{test_case['name']}' failed"
