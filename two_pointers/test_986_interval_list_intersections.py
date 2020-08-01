from typing import List

from pytest import mark


class Solution:
    def interval_intersection(
        self, a: List[List[int]], b: List[List[int]]
    ) -> List[List[int]]:
        ap, bp = 0, 0
        res = []
        while ap < len(a) and bp < len(b):
            left = max(a[ap][0], b[bp][0])
            right = min(a[ap][1], b[bp][1])
            if left <= right:
                res.append([left, right])

            if a[ap][1] > b[bp][1]:
                bp += 1
            else:
                ap += 1

        return res


class TestSolution:
    data_provider = [
        [
            [[1, 3], [5, 8], [9, 12]],
            [[2, 4], [6, 7], [8, 9]],
            [[2, 3], [6, 7], [8, 8], [9, 9]],
        ],
        [
            [[1, 3], [5, 8], [9, 12]],
            [[2, 4], [6, 7], [8, 9], [10, 13]],
            [[2, 3], [6, 7], [8, 8], [9, 9], [10, 12]],
        ],
        [
            [[1, 100]],
            [[2, 4], [6, 7], [8, 9], [10, 13]],
            [[2, 4], [6, 7], [8, 9], [10, 13]],
        ],
        [[[1, 3], [5, 8], [9, 12]], [[1, 100]], [[1, 3], [5, 8], [9, 12]],],
        [[], [], [],],
        [[[1, 3]], [[4, 5]], [],],
    ]

    @mark.parametrize("a, b, expected", data_provider)
    def test_interval_intersection(
        self, a: List[List[int]], b: List[List[int]], expected: List[List[int]]
    ):
        solution = Solution()
        assert solution.interval_intersection(a, b) == expected
