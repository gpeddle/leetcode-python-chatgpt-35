# stringToInteger

import pytest
from .solution import Solution

# revise test_data to match problem statement
test_data = [
    {
        'name': 'Example 1',
        'input': 42,
        'expected': 42
    },
    {
        'name': 'Example 2',
        'input': 42,
        'expected': -42
    },
    {
        'name': 'Example 3',
        'input': '4193 with words',
        'expected': 4193
    }
]

@pytest.mark.parametrize("test_case", test_data)
def test_solution(test_case):
    solution = Solution()
    result = solution.myAtoi(test_case['input'])
    assert result == test_case['expected'], f"Test '{test_case['name']}' failed"
