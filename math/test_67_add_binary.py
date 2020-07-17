from abc import ABC, abstractmethod
from typing import List

from pytest import fixture, mark

# 1. Will the input strings be empty?
# 2. Do the input strings only consist of "0" and "1"?
# 3. Will the input strings have leading "0"s?
# 4. Is there limitation of the length of the input strings?


class Solution(ABC):
    @abstractmethod
    def add_binary(self, a: str, b: str) -> str:
        pass


class SolutionStringLooping(Solution):
    def add_binary(self, a: str, b: str) -> str:
        carry, res = 0, ""
        i, j = len(a) - 1, len(b) - 1
        while i > -1 or j > -1 or carry:
            if i > -1:
                carry += int(a[i])
            if j > -1:
                carry += int(b[j])
            res = str(carry % 2) + res
            carry //= 2
            i -= 1
            j -= 1

        return res


class SolutionBinaryInteger(Solution):
    def add_binary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


class TestSolution:
    @fixture
    def solutions(self) -> List[Solution]:
        return [SolutionStringLooping(), SolutionBinaryInteger()]

    data_provider = [
        ["1", "11", "100"],
        ["100", "0", "100"],
        ["11", "11", "110"],
        ["100", "100", "1000"],
    ]

    @mark.parametrize("a, b, expected", data_provider)
    def test_solution(self, a: str, b: str, expected: str, solutions):
        for solution in solutions:
            assert solution.add_binary(a, b) == expected
