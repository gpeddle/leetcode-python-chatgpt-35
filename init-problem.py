import os
import sys
import re

if len(sys.argv) != 3:
    print("Usage: python init-problem.py <problem_number> <problem_name>")
    sys.exit(1)

problem_number = -1, 
problem_name = "ERROR"

if not re.match(r'^\d+$', sys.argv[1]):
    problem_number = int(sys.argv[1])
    print("<problem_number> must contain only numbers.")
    sys.exit(1)

problem_number = "{:0>{width}}".format(int(sys.argv[1]), width=4)

problem_name = sys.argv[2]
pattern = r'^[A-z0-9]+$'
if not re.match(pattern, problem_name):
    print("<problem_name> must contain only numbers and letters.")
    sys.exit(1)


subfolder_name = f"algorithms/p{problem_number}_{problem_name}"

# Check if the subfolder exists
if os.path.exists(subfolder_name) and os.path.isdir(subfolder_name):
    print(f"Subfolder '{subfolder_name}' already exists.")
    sys.exit(1)

# If it doesn't exist, create the subfolder
os.mkdir(subfolder_name)
print(f"Created {subfolder_name}")

# Templates with placeholders for interpolation
templates = [
    {
        'filename': 'problem.md',
        'template': """# {problem_name}

Copy/paste the problem text from leetcode. 
"""
    },
    {
        'filename': '__init__.py',
        'template': """"""
    },
    {
        'filename': f"solution.py",
        'template': """# {problem_name}

from typing import List, Dict, Union

class Solution:
    # revise parameter list to match problem statement
    def {problem_name}(self, input: List[int], target: int) -> List[int]:
        # Implement your solution here
        return [0, 1]
"""
    },
    {
        'filename': f"test_{problem_name}.py",
        'template': """# {problem_name}

import pytest
from .solution import Solution

# revise test_data to match problem statement
test_data = [
    {{
        'name': 'Example 1',
        'input': [0, 0],
        'target': 0,
        'expected': [0, 0]
    }},
    {{
        'name': 'Example 2',
        'input': [0, 0],
        'target': 0,
        'expected': [0, 0]
    }},
    {{
        'name': 'Example 3',
        'input': [0, 0],
        'target': 0,
        'expected': [0, 0]
    }}
]

@pytest.mark.parametrize("test_case", test_data)
def test_solution(test_case):
    solution = Solution()
    result = solution.{problem_name}(test_case['input'], test_case['target'])
    assert result == test_case['expected'], f"Test '{{test_case['name']}}' failed"
"""
    }
]

# Emit the files with template interpolation
for item in templates:
    file_content = item['template'].format(problem_name=problem_name)
    with open(os.path.join(subfolder_name, f"{item['filename']}"), "w") as file:
        file.write(file_content)

    print(f"Created {subfolder_name}/{item['filename']}")
