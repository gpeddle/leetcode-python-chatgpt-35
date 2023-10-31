# regularExpressionMatching

import pytest
from .solution import Solution

# revise test_data to match problem statement
test_data = [
    {
        'name': 'Example 1',
        's': 'aa',
        'p': 'a',
        'expected': False
    },
    {
        'name': 'Example 2',
        's': 'aa',
        'p': 'a*',
        'expected': True
    },
    {
        'name': 'Example 3',
        's': 'ab',
        'p': '.*',
        'expected': True
    }
]

@pytest.mark.parametrize("test_case", test_data)
def test_solution(test_case):
    solution = Solution()
    result = solution.isMatch(test_case['s'], test_case['p'])
    assert result == test_case['expected'], f"Test '{test_case['name']}' failed"
