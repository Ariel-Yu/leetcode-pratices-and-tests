from abc import ABC, abstractmethod
from heapq import heappop, heappush
from typing import List

from pytest import mark

# 1. Will extra 0s in nums1 always be on the right hand side?
# 2. Will nums1 it self also have 0s?
# 3. Can nums1 and num2 be empty


class Solution(ABC):
    @abstractmethod
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        pass


class SolutionSort(Solution):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        nums1[m:] = nums2
        nums1.sort()


class SolutionHeapQ(Solution):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        hq = []
        if m:
            heappush(hq, (nums1[0], 1, 1))
        if n:
            heappush(hq, (nums2[0], 2, 1))

        sorted_array = []
        while len(hq):
            item = heappop(hq)
            sorted_array.append(item[0])
            if item[1] == 1 and item[2] < m:
                heappush(hq, (nums1[item[2]], item[1], item[2] + 1))
            if item[1] == 2 and item[2] < n:
                heappush(hq, (nums2[item[2]], item[1], item[2] + 1))

        nums1[:] = sorted_array


class TestSolutions:
    data_provider_1 = [
        [[1, 2, 3, 0, 0], 3, [2, 5], 2, [1, 2, 2, 3, 5]],
        [[-1, 0, 1, 2, 3, 0, 0], 5, [2, 5], 2, [-1, 0, 1, 2, 2, 3, 5]],
        [
            [-1, 0, 1, 2, 3, 0, 0, 0, 0],
            5,
            [-2, 0, 2, 5],
            4,
            [-2, -1, 0, 0, 1, 2, 2, 3, 5],
        ],
        [[0, 0], 0, [2, 5], 2, [2, 5]],
        [[-1, 0, 1, 2, 3], 5, [], 0, [-1, 0, 1, 2, 3]],
        [[], 0, [], 0, []],
    ]

    data_provider_2 = [
        [[1, 2, 3, 0, 0], 3, [2, 5], 2, [1, 2, 2, 3, 5]],
        [[-1, 0, 1, 2, 3, 0, 0], 5, [2, 5], 2, [-1, 0, 1, 2, 2, 3, 5]],
        [
            [-1, 0, 1, 2, 3, 0, 0, 0, 0],
            5,
            [-2, 0, 2, 5],
            4,
            [-2, -1, 0, 0, 1, 2, 2, 3, 5],
        ],
        [[0, 0], 0, [2, 5], 2, [2, 5]],
        [[-1, 0, 1, 2, 3], 5, [], 0, [-1, 0, 1, 2, 3]],
        [[], 0, [], 0, []],
    ]

    @mark.parametrize("nums1, m, nums2, n, expected", data_provider_1)
    def test_merge_solution_sort(
        self, nums1: List[int], m: int, nums2: List[int], n: int, expected: List[int]
    ):
        solution = SolutionSort()
        solution.merge(nums1, m, nums2, n)
        assert nums1 == expected

    # Since the solution is changing the input in-place, we can not re-use the same data provider
    @mark.parametrize("nums1, m, nums2, n, expected", data_provider_2)
    def test_merge_solution_heapq(
        self, nums1: List[int], m: int, nums2: List[int], n: int, expected: List[int]
    ):
        solution = SolutionHeapQ()
        solution.merge(nums1, m, nums2, n)
        assert nums1 == expected


def complexity_analysis_sort():
    print("=> Time complexity: O((m+n) log(m+n))")
    print("=> Space complexity: O(1)")


def complexity_analysis_heapq():
    print("=> Time complexity: O((m+n))")
    print("=> Space complexity: O(1)")


if __name__ == "__main__":
    complexity_analysis_sort()
    complexity_analysis_heapq()
