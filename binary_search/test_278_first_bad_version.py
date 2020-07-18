from pytest import mark

# 1. Is there always be a bad version within the given n?
#    Which means that, can the bad version be 0 or > n


class Solution:
    def __init__(self, bad_version: int):
        self.bad_version = bad_version

    def _is_bad_api(self, version: int) -> bool:
        if version >= self.bad_version:
            return True
        return False

    def first_bad_version(self, n: int) -> int:
        left = 1
        right = n + 1
        res = None
        while left < right:
            mid = (left + right) // 2
            if self._is_bad_api(mid):
                right = mid
                res = mid
            else:
                left = mid + 1

        if res is None:
            return n
        return res


class TestSolution:
    data_provider = [
        [5, 1, 1],
        [5, 5, 5],
        [5, 0, 1],
        [5, 6, 5],
        [1, 1, 1],
        [2126753390, 1702766719, 1702766719],
    ]

    @mark.parametrize("latest_version, bad_version, expected", data_provider)
    def test_first_bad_version(
        self, latest_version: int, bad_version: int, expected: int
    ):
        solution = Solution(bad_version)
        assert solution.first_bad_version(latest_version) == expected
