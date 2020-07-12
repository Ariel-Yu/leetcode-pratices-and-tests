from abc import ABC, abstractmethod
from heapq import heappop, heappush, nlargest
from typing import List

from pytest import fixture, mark


class Solution(ABC):
    @abstractmethod
    def kth_largest_element(self, nums: List[int], k: int) -> int:
        pass


class SolutionSort(Solution):
    def kth_largest_element(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


class SolutionHeapQ(Solution):
    def kth_largest_element(self, nums: List[int], k: int) -> int:
        hq = []
        for num in nums:
            heappush(hq, num)
            if len(hq) > k:
                heappop(hq)

        return heappop(hq)


class SolutionHeapQNLargest(Solution):
    def kth_largest_element(self, nums: List[int], k: int) -> int:
        return nlargest(k, nums)[-1]


class TestSolutions:
    @fixture
    def solutions(self) -> List[Solution]:
        return [SolutionSort(), SolutionHeapQ(), SolutionHeapQNLargest()]

    data_provider = [
        [[2, 3, 4, 5, 1, 4, 4, 5], 2, 5],
        [[2, 3, 4, 5, 1, 4, 4, 5], 4, 4],
        [[2, 3, 4, 5, 1, 4, 4, 5], 6, 3],
    ]

    @mark.parametrize("nums, k, expected", data_provider)
    def test_kth_largest_element(
        self, nums: List[int], k: int, expected: int, solutions
    ):
        for solution in solutions:
            assert solution.kth_largest_element(nums, k) == expected
