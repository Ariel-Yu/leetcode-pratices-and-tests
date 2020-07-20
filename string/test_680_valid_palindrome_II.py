from pytest import mark


class Solution:
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

    def valid_palindrome(self, s: str) -> bool:
        if self.is_palindrome(s):
            return True

        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                new_s = s[:i] + s[i + 1 :]
                if self.is_palindrome(new_s):
                    return True
                else:
                    new_s = s[:j] + s[j + 1 :]
                    if self.is_palindrome(new_s):
                        return True
                    else:
                        return False
            i += 1
            j -= 1


class TestSolution:
    data_provider = [
        ["aba", True],
        ["abca", True],
        ["abcb", True],
        ["bcba", True],
        ["abcddcbab", True],
        ["abc", False],
        ["acdba", False],
    ]

    @mark.parametrize("s, expected", data_provider)
    def test_valid_palindrome(self, s: str, expected: bool):
        solution = Solution()
        assert solution.valid_palindrome(s) == expected
