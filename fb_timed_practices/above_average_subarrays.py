from typing import List

from pytest import mark


class Solution:
    def above_average_subarrays(self, a: List[int]) -> List[List[int]]:  # O(N ** 3)
        res = []
        for i in range(len(a)):  # O(N)
            for j in range(i, len(a)):  # O(N)
                sub = a[i : j + 1]  # O(N)
                sub_avg = sum(sub) / len(sub)
                r = a[:i] + a[j + 1 :]  # O(N)
                if not r:
                    r_avg = 0
                else:
                    r_avg = sum(r) / len(r)
                if sub_avg > r_avg:
                    res.append([i + 1, j + 1])

        return res


class TestSolution:
    data_provider = [
        [
            [3, 4, 2],
            [[1, 2], [1, 3], [2, 2]],
            # i, j sub, r
            # 0, 0, 3, 3
            # 0, 1, 3.5, 2 v 1,2
            # 0, 2, 3, 0 v 1,3
            # 1, 1, 4, 2.5 v 2,2
            # 1, 2, 3, 3
            # 2, 2, 2, 3.5
        ],
        [
            [4, 2, 1, 3],
            [[1, 1], [1, 2], [1, 4], [4, 4]],
            # i, j sub, r
            # 0, 0, 4, 1 v 1,1
            # 0, 1, 3, 2 v 1,2
            # 0, 2, 2.33, 3
            # 0, 3, x, 0 v 1, 4
            # 1, 1, 2, 2.67
            # 1, 2, 2.5, 3,5
            # 1, 3, 2, 4
            # 2, 2, 1, 3,
            # 2, 3, 2, 3
            # 3, 3, 3, 2,33 v 4,4
        ],
    ]

    @mark.parametrize("a, expected", data_provider)
    def test_above_average_subarrays(self, a: List[int], expected: List[List[int]]):
        solution = Solution()
        assert solution.above_average_subarrays(a) == expected
