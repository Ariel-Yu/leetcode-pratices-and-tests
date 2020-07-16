from abc import ABC, abstractmethod
from typing import List

from pytest import fixture, mark

# 1. Will the given matrices be empty? No
# 2. Should the validations listed be implemented in the solutions?


# a: n * m
# b: m * o
class Solution(ABC):
    @abstractmethod
    def matrix_multiplication(
        self, a: List[List[int]], b: List[List[int]]
    ) -> List[List[int]]:
        pass


# Time complexity: O(n * o * m)
# Auxiliary space complexity: O(1)
class SolutionFullMatrix(Solution):
    def matrix_multiplication(
        self, a: List[List[int]], b: List[List[int]]
    ) -> List[List[int]]:
        results = []
        for i in range(len(a)):
            results.append([])
            for j in range(len(b[0])):
                value = 0
                for k in range(len(b)):
                    value += a[i][k] * b[k][j]
                results[-1].append(value)

        return results


# Time complexity: O(n * m + m * o) = O(m * (n + o))
# Auxiliary space complexity: O(m * (n + o))
class SolutionHashTable(Solution):
    def matrix_multiplication(
        self, a: List[List[int]], b: List[List[int]]
    ) -> List[List[int]]:
        results = [[0 for y in range(len(b[0]))] for x in range(len(a))]
        map_a = {}
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] != 0:
                    map_a[tuple((i, j))] = a[i][j]
        map_b = {}
        for i in range(len(b)):
            for j in range(len(b[0])):
                if a[i][j] != 0:
                    map_b[tuple((i, j))] = b[i][j]

        for key_a in map_a.keys():
            for key_b in map_b.keys():
                if key_a[1] == key_b[0]:
                    results[key_a[0]][key_b[1]] += map_a[key_a] * map_b[key_b]
        return results


class TestSolutions:
    @fixture
    def solutions(self) -> List[Solution]:
        return [SolutionFullMatrix()]

    data_provider = [
        [
            [[1, 0, 0], [-1, 0, 3]],
            [[7, 0, 0], [0, 0, 0], [0, 0, 1]],
            [[7, 0, 0], [-7, 0, 3]],
        ],
        [[[1, 0, 0]], [[7], [0], [0]], [[7]]],
        [[], [], []],
        [[[1, -5]], [[12], [-1]], [[17]]],
    ]

    @mark.parametrize("a, b, expected", data_provider)
    def test_matrix_multiplication(
        self,
        a: List[List[int]],
        b: List[List[int]],
        expected: List[List[int]],
        solutions,
    ):
        for solution in solutions:
            assert solution.matrix_multiplication(a, b) == expected
