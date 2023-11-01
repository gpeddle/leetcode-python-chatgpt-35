# leetcode-python-chatgpt-35

## Overview

ChatGPT 3.5 does TDD oriented solutions of leetcode problems using Python3.
(a clone/mod of https://github.com/gpeddle/leetcode-python)

This project uses the same approach outlined below, but using ChatGPT 3.5 as the code generator with a simple prompt sequence. 

Using this approach, I completed 10 problems in about an hour… but most of the time was spent on file copy/paste. The actual time the AI was involved is probably about 5 minutes.

ChatGPT got everything right on its first attempt.

## Setup

### Prerequisites

- Python3
- PyTest

*Assumption: Python3 and PyTest are installed globally, so no need for virtual environments.*  

## Initializing a new problem

A new problem folder can be initialized using the `init-problem.py` script.

This script requires the following parameters:

- <problem_number> an integer that corresponds to the leetcode problem number.
- <problem_name> the name of the leetcode method used to invoke the solution

Note that the problem name must contain only letters and numbers. This allows us to emit valid Python modules that include the problem name. Consult leetcode to get the problem name before initializing.

*For example, problem #1, 'Two Sum' has the following method definition:*

`def twoSum(self, input: List[int], target: int) -> List[int]:`

*... and so the problem name is 'twoSum'. When initializing this problem:*

`python3 init-problem.py 1 twoSum`

## Examine the new problem folder
Each problem is set up in a subdirectory under the `algorithms` subfolder.

The `init-problem.py` script does the following:

1. Creates a new subdirectory for the problem
2. Creates a `problem.md` file
3. Creates a `prompt.md` file
4. Creates a `response.md` file
5. Creates a `solution.py` file with a sample solution class
6. Creates a `tests_<problem_name>.py` file with a table-driven test

## Edit the initialized problem before working

1. Navigate to the problem subdirectory.
2. Copy/paste/format the problem description from leetcode into the `problem.md` file.
3. Edit the tests file to make `test_data` match the examples from the problem description.
4. Copy/paste the solution class method signature from leetcode into `solution.py`
    - *The method signature must match the invocation in the test script!*

## Format the prompt

The `prompt.md` file has an initial instuction and two sections: `PROBLEM` and `SKELETON`. Each of the sections has a code fence just below the section heading. The code fences are in markdown and python respectively.

1. Copy the contents of `problem.md` into the area below `PROBLEM:`
2. Copy the contents of `solution.md` into the area below `SKELETON:`

## Working with ChatGPT

1. Copy the contents of `prompt.md` into a ChatGPT session. You do not need a new session because the prompt includes an initial reset instruction.
2. Click 'Send' to submit the prompt
3. Examine the output
4. Copy the entire response into the `response.md` file.
5. Copy the generated solution calss into the `solution.py` file.

## Working a problem locally

1. Navigate to the problem subdirectory.
2. Run `pytest -v` to test the solution
3. Revise the `prompt.md` file if needed and resubmit to ChatGPT.
4. Repeat #2 and #3 to arrive at a solution that satisfies the examples provided by leetcode.

## Running a problem in leetcode

When the solution passes all the example `test_data` locally, copy the contents of `solution.py` and paste it into leetcode's editor, then click [Run].

Observe that leetcode runs the solution and check to output for errors. Review any errors and revisit the solution locally to correct the method. 

> Note that leetcode will only test your solution against the example `test_data` during [Run].

## Submitting a problem to leetcode

Once you are satisfied that the solution passes tests proposed by the example data, click [Submit]. This submits the solution to the leetcode judge. the judge runs the solution with additional test data to verify the correctness and performance of the solution.

> Note that the leetcode judge will usually impose additional edge cases which must be addressed. If your solution does not handle these cases, simply copy the new unexpected edge case input parameters to a new entries in `test_data` and return to working on the solution.

## Completing a problem

Once you have completed a problem and passed the leetcode judge submission process, review the code folder and then commit to github. This maintains a clean set of solutions and a history of how you approached solving these problems.

Congratulations! Your next step is to choose a new problem and repeat this process. 

My own experience of approaching leetcode this way was centered around a time-boxed (45 minute) period in the early morning. If a problem was not complete at the end of my time-box, I would simply continue the next morning and work the cycle.

## Enjoy

I hope this approach aids you in hacking through leetcode problems, and especially that it elevates your happiness in coding.
