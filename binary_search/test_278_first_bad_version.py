from pytest import mark

# 1. Is there always be a bad version within the given n?


class Solution:
    def __init__(self, bad_version: int):
        self.bad_version = bad_version

    def _is_bad_api(self, version: int) -> bool:
        if version >= self.bad_version:
            return True
        return False

    def first_bad_version(self, n: int) -> int:
        # Using floor division means that left edge will be hit but right edge will never be hit
        # ex: (1, 10) -> (5, 10) -> (7, 10) -> (8, 10) -> (9, 10) -> (9, 10) ...
        version = (n + 1) // 2
        left = 1
        right = n
        bad = None
        pre = None
        while pre != version:
            if self._is_bad_api(version):
                right = version
                bad = version
            else:
                left = version
            pre = version
            version = (left + right) // 2

        # If there might NOT be a bad version, the below check will be different
        if not bad:
            if left > 0:
                return n

        return bad


class TestSolution:
    data_provider = [
        [5, 1, 1],
        [5, 5, 5],
        [1, 1, 1],
        [2126753390, 1702766719, 1702766719],
    ]

    @mark.parametrize("latest_version, bad_version, expected", data_provider)
    def test_first_bad_version(
        self, latest_version: int, bad_version: int, expected: int
    ):
        solution = Solution(bad_version)
        assert solution.first_bad_version(latest_version) == expected
