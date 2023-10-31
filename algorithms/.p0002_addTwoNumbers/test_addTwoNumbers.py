# addTwoNumbers

import pytest
from .solution import Solution

# revise test_data to match problem statement
test_data = [
    {
        'name': 'Example 1',
        'l1': [2,4,3], 
        'l2': [5,6,4],
        'target': 0,
        'expected': [5,6,4]
    },
    {
        'name': 'Example 2',
        'l1': [0],
        'l2': [0],
        'target': 0,
        'expected': [0]
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
    result = solution.addTwoNumbers(test_case['l1'], test_case['l2'], test_case['target'])
    assert result == test_case['expected'], f"Test '{test_case['name']}' failed"
