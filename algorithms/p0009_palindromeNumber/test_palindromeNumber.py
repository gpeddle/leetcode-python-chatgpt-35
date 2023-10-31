# palindromeNumber

import pytest
from .solution import Solution

# revise test_data to match problem statement
test_data = [
    {
        'name': 'Example 1',
        'input': 121,
        'expected': True
    },
    {
        'name': 'Example 2',
        'input': -121,
        'expected': False
    },
    {
        'name': 'Example 3',
        'input': 10,
        'expected': False
    }
]

@pytest.mark.parametrize("test_case", test_data)
def test_solution(test_case):
    solution = Solution()
    result = solution.isPalindrome(test_case['input'])
    assert result == test_case['expected'], f"Test '{test_case['name']}' failed"
