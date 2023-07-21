from two_sum_naive import Solution as Naive
from two_sum_hash_1pass import Solution as Pass1
from two_sum_hash_2pass import Solution as Pass2

test_nums_list = [
    [
        [2,7,11,15],
        9,
        [0, 1]
    ],
    [
        [3,2,4],
        6,
        [1,2]
    ],
    [
        [3,3],
        6,
        [0,1]
    ]
]

def test_twoSum(nums, target, expected, Class):
    solution = Class()
    reverse_expected = [expected[1], expected[0]]
    result = solution.twoSum(nums, target)
    assert result == expected or result == reverse_expected

for Solution in (Naive, Pass1, Pass2):
    [test_twoSum(test_nums[0], test_nums[1], test_nums[2], Solution) for test_nums in test_nums_list]
