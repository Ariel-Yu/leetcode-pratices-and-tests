from abc import ABC, abstractmethod
from heapq import heappop, heappush
from typing import List

from pytest import fixture, mark


class Solution(ABC):
    @abstractmethod
    def k_closest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pass


class Solution_Heapq(Solution):
    def k_closest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hq = []
        for i in range(len(points)):
            heappush(hq, (points[i][0] ** 2 + points[i][1] ** 2, i, points[i]))

        res = []
        for j in range(k):
            res.append(heappop(hq)[2])

        return res


class SolutionSort(Solution):
    def k_closest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda nums: nums[0] ** 2 + nums[1] ** 2)
        return points[:k]


class TestSolutions:
    @fixture
    def solutions(self) -> List[Solution]:
        return [Solution_Heapq()]

    data_provider = [
        [[[1, 3], [-2, 2]], 1, [[-2, 2]]],
        [[[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]],
    ]

    @mark.parametrize("points, k, expected", data_provider)
    def test_k_closest(
        self, points: List[List[int]], k: int, expected: List[List[int]], solutions
    ):
        for solution in solutions:
            assert solution.k_closest(points, k) == expected
