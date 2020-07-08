from abc import ABC, abstractmethod
from typing import List

from pytest import fixture, mark


class Solution(ABC):
    @abstractmethod
    def my_pow(self, x: float, n: int) -> float:
        pass


class SolutionPow(Solution):
    def my_pow(self, x: float, n: int) -> float:
        return x ** n


class SolutionMath(Solution):
    def my_pow(self, x: float, n: int) -> float:
        def helper(x: float, n: int) -> float:
            if n == 0:
                return 1.0

            tmp = helper(x, n // 2)
            if n % 2 == 0:
                return tmp * tmp
            if n % 2 != 0:
                return x * tmp * tmp

        if n >= 0:
            return helper(x, n)

        return 1 / helper(x, -n)


class TestSolutions:
    @fixture
    def solutions(self) -> List[Solution]:
        return [SolutionPow(), SolutionMath()]

    data_provider = [[2.0, 2, 4.0], [2.0, 0, 1.0], [2.0, -2, 0.25]]

    @mark.parametrize("x, n, expected", data_provider)
    def test_my_pow(self, x: float, n: int, expected: float, solutions):
        for solution in solutions:
            assert solution.my_pow(x, n) == expected


def complexity_analysis_pow():
    print("=> Time complexity: O(n)")


def complexity_analysis_math():
    print("=> Time complexity: O(log n)")


if __name__ == "__main__":
    complexity_analysis_pow()
    complexity_analysis_math()
