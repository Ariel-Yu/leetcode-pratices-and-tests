from typing import List
from abc import ABC, abstractmethod

from pytest import mark, fixture


# Q1: Since the index will be <N, is the number N always False and won't be set True:
# Q2: Can the index be 0 which is not included in the array (1-based)?

class Solution(ABC):
    @abstractmethod
    def answer_queries(self, queries: List[List[int]], n: int) -> List[int]:
        pass


class Solution1(Solution):
    def answer_queries(self, queries: List[List[int]], n: int) -> List[int]:  # O(Q * N)
        array = [False] * n
        res = []
        for query in queries:  # O(Q)
            if query[0] == 1:  # SET
                array[query[1] - 1] = True
            else:  # GET
                index = -1
                for i in range(query[1] - 1, n):  # O(N)
                    if array[i]:
                        index = i + 1
                        break
                res.append(index)

        return res


class Solution2(Solution):
    def answer_queries(self, queries: List[List[int]], n: int) -> List[int]:  # O(Q * P)
        res, p = [], []
        for query in queries:  # O(Q)
            if query[0] == 1:  # SET
                p.append(query[1] - 1)
            else:  # GET
                index = -1
                c = [x for x in p if x >= query[1] - 1]  # O(P)
                if c:
                    index = min(c) + 1  # O(P)
                res.append(index)

        return res


class TestSolution:
    @fixture
    def solutions(self) -> List[Solution]:
        return [
            Solution1()
        ]

    data_provider = [
        [
            [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]],
            5,
            [-1, 2, -1, 2],
            # [False, True, False, False, False]
        ],
        [
            [[2, 1], [1, 1], [2, 1], [2, 2], [1, 3], [2, 2], [2, 3]],
            4,
            [-1, 1, -1, 3, 3],
            # [True, False, True, False]
        ],
    ]

    @mark.parametrize("queries, n, expected", data_provider)
    def test_answer_queries(self, queries: List[List[int]], n: int, expected: List[int]):
        solution = Solution1()
        assert solution.answer_queries(queries, n) == expected
