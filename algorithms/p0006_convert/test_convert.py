# convert

import pytest
from solution import Solution

# revise test_data to match problem statement
test_data = [
    {
        'name': 'Example 1',
        's': 'PAYPALISHIRING',
        'numRows': 3,
        'expected': 'PAHNAPLSIIGYIR'
    },
    {
        'name': 'Example 2',
        's': 'PAYPALISHIRING',
        'numRows': 4
        'expected': 'PINALSIGYAHRPI'
    },
    {
        'name': 'Example 3',
        's': 'A',
        'numRows': 1,
        'expected': 'A'
    }
]

@pytest.mark.parametrize("test_case", test_data)
def test_solution(test_case):
    solution = Solution()
    result = solution.convert(test_case['s'], test_case['numRows'])
    assert result == test_case['expected'], f"Test '{test_case['name']}' failed"
