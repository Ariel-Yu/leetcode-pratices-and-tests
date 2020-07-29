from typing import List

from pytest import mark


class Solution:
    def binary_search_exact(self, values: List[int], target: int) -> int:
        left, right = 0, len(values) - 1
        while left <= right:
            index = (left + right) // 2
            if values[index] < target:
                left = index + 1
            elif values[index] > target:
                right = index - 1
            else:
                return index

        return False

    def binary_search_approx(self, values: List[int], target: float) -> int:
        left, right = 0, len(values) - 1
        diff, res = None, None
        while left <= right:
            index = (left + right) // 2
            index_diff = abs(target - values[index])
            if diff is None or index_diff < diff:
                diff = index_diff
                res = index
            if values[index] < target:
                left = index + 1
            elif values[index] > target:
                right = index - 1

        return res


class TestSolution:
    exact_data_provider = [
        [[1, 2, 3, 4, 5], 5, 4],
        [[1, 2, 3, 4, 5], 1, 0],
        [[1, 2, 3, 4, 5], 3, 2],
        [[1, 2, 3, 4, 5], 3.5, False],
        [[1, 2, 3, 4, 5], 6, False],
    ]

    @mark.parametrize("values, target, expected", exact_data_provider)
    def test_binary_search_exact(self, values: List[int], target: int, expected: int):
        solution = Solution()
        assert solution.binary_search_exact(values, target) == expected

    approx_data_provider = [
        [[1, 2, 3, 4, 5], 5.8, 4],
        [[1, 2, 3, 4, 5], 0.2, 0],
        [[1, 2, 3, 4, 5], 3.2, 2],
        [[1, 2, 3, 4, 5], 3.8, 3],
    ]

    @mark.parametrize("values, target, expected", approx_data_provider)
    def test_binary_search_approx(self, values: List[int], target: int, expected: int):
        solution = Solution()
        assert solution.binary_search_approx(values, target) == expected
