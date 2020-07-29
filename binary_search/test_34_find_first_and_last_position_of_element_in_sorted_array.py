from abc import ABC, abstractmethod
from typing import List

from pytest import fixture, mark


class Solution(ABC):
    @abstractmethod
    def search_range(self, nums: List[int], target: int) -> List[int]:
        pass


# Avg: O(log n)
# Worst: O(n)
class Solution1(Solution):
    def search_range(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        found = None
        while left <= right:
            index = (left + right) // 2
            if nums[index] > target:
                right = index - 1
            elif nums[index] < target:
                left = index + 1
            else:
                found = index
                break

        if found is None:
            return [-1, -1]

        ceil = floor = found
        for i in range(found + 1, len(nums)):
            if nums[i] == target:
                ceil = i
            else:
                ceil = i - 1
                break
        for j in range(found + -1, -1, -1):
            if nums[j] == target:
                floor = j
            else:
                floor = j + 1
                break

        return [floor, ceil]


# Avg: O(n)
class Solution2(Solution):
    def find_index(self, nums: List[int], target: int, first: bool = True) -> int:
        index = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                if first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return index

    def search_range(self, nums: List[int], target: int) -> List[int]:
        return [self.find_index(nums, target), self.find_index(nums, target, False)]


class TestSolutions:
    @fixture
    def solutions(self) -> List[Solution]:
        return [Solution1()]

    data_provider = [
        [[1, 1, 2, 2, 3, 3, 3], 1, [0, 1]],
        [[1, 1, 2, 2, 3, 3, 3], 2, [2, 3]],
        [[1, 1, 2, 2, 3, 3, 3], 3, [4, 6]],
        [[1, 1, 2, 2, 3, 3, 3], 4, [-1, -1]],
        [[1, 2, 3], 1, [0, 0]],
        [[1, 2, 3], 2, [1, 1]],
        [[1, 2, 3], 3, [2, 2]],
        [[1], 1, [0, 0]],
        [[], 1, [-1, -1]],
    ]

    @mark.parametrize("nums, target, expected", data_provider)
    def test_search_range(
        self, nums: List[int], target: int, expected: List[int], solutions
    ):
        for solution in solutions:
            assert solution.search_range(nums, target) == expected
