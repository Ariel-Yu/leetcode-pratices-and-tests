from abc import ABC, abstractmethod
from typing import List

from pytest import fixture, mark


class Solution(ABC):
    @abstractmethod
    def product(self, nums: List[int]) -> List[int]:
        pass


class SolutionLeftRight(Solution):
    def product(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left, right, answer = [0] * length, [0] * length, [0] * length

        # Instantiate product of the left values of nums[i]
        left[0] = 1
        for i in range(1, length):
            left[i] = left[i - 1] * nums[i - 1]

        # Instantiate product of the right values of nums[j]
        right[-1] = 1
        for j in range(length - 2, -1, -1):
            right[j] = right[j + 1] * nums[j + 1]

        # Answer of nums[x] equals product of left values * product of right values
        for x in range(length):
            answer[x] = left[x] * right[x]

        return answer


class SolutionLeftR(Solution):
    def product(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length

        answer[0] = 1
        for i in range(1, length):
            answer[i] = answer[i - 1] * nums[i - 1]

        r = 1
        for j in range(length - 1, -1, -1):
            answer[j] = answer[j] * r
            r *= nums[j]

        return answer


class TestSolutions:
    @fixture
    def solutions(self) -> List[Solution]:
        return [
            SolutionLeftRight()
        ]

    data_provider = [
        [
            [1,2,3,4],
            [24,12,8,6]
        ],
        [
            [1,2,0],
            [0,0,2]
        ],
        [
            [0,0],
            [0,0]
        ]
    ]

    @mark.parametrize("nums, expected", data_provider)
    def test_product(self, nums: List[int], expected: List[int], solutions):
        for solution in solutions:
            assert solution.product(nums) == expected
