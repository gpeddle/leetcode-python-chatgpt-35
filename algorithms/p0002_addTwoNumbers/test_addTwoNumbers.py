# addTwoNumbers

import pytest
from .solution import ListNode, Solution

# revise test_data to match problem statement
test_data = [
    {
        'name': 'Example 1',
        'l1': ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None))),
        'l2': ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None))),
        'expected': ListNode(val=7, next=ListNode(val=0, next=ListNode(val=8, next=None)))
    },
    {
        'name': 'Example 2',
        'l1': ListNode(0),
        'l2': ListNode(0),
        'expected': ListNode(0)
    },
    {
        'name': 'Example 3',
        'l1': ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))))),
        'l2': ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))),
        'expected': ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1,None))))))))
    }
]


@pytest.mark.parametrize("test_case", test_data)
def test_solution(test_case):
    solution = Solution()
    result = solution.addTwoNumbers(test_case['l1'], test_case['l2'])
    assert result == test_case['expected'], f"Test '{test_case['name']}' failed"
