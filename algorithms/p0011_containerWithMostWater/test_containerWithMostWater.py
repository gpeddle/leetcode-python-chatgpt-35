# containerWithMostWater

import pytest
from .solution import Solution

# revise test_data to match problem statement
test_data = [
    {
        'name': 'Example 1',
        'input': [1,8,6,2,5,4,8,3,7],
        'expected': 49
    },
    {
        'name': 'Example 2',
        'input': [1, 1],
        'expected': 1
    }
]

@pytest.mark.parametrize("test_case", test_data)
def test_solution(test_case):
    solution = Solution()
    result = solution.maxArea(test_case['input'])
    assert result == test_case['expected'], f"Test '{test_case['name']}' failed"
