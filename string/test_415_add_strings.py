from pytest import mark


class Solution:
    def add_strings(self, a: str, b: str) -> str:
        carry, res = 0, ""
        i, j = len(a) - 1, len(b) - 1
        while i > -1 or j > -1 or carry:
            if i > -1:
                carry += int(a[i])
            if j > -1:
                carry += int(b[j])
            res = str(carry % 10) + res
            carry //= 10
            i -= 1
            j -= 1

        return res


class TestSolution:
    data_provider = [["99", "11", "110"], ["999", "11", "1010"], ["0", "0", "0"]]

    @mark.parametrize("a, b, expected", data_provider)
    def test_add_strings(self, a: str, b: str, expected: str):
        solution = Solution()
        assert solution.add_strings(a, b) == expected
