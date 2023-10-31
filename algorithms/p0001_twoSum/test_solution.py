import pytest
from .solution import Solution

# data is an array of test case inputs
test_data = [
    {
        'name': 'Example 1',
        'input': [2, 7, 11, 15],
        'target': 9,
        'expected': [0, 1]
    },
    {
        'name': 'Example 2',
        'input': [3, 2, 4],
        'target': 6,
        'expected': [1, 2]
    },
    {
        'name': 'Example 3',
        'input': [3, 3],
        'target': 6,
        'expected': [0, 1]
    }
]


@pytest.mark.parametrize("test_case", test_data)
def test_solution(test_case):
    solution = Solution()
    result = solution.twoSum(test_case['input'], test_case['target'])
    assert result == test_case['expected'], f"Test '{test_case['name']}' failed"
