from abc import ABC, abstractmethod
from typing import List

from pytest import fixture, mark

# 1. The input string can contain all kinds of character?
# 2. But only digit and alpha characters count?
# 3. Will the input string contain empty space?


class Solution(ABC):
    @abstractmethod
    def is_palindrome(self, s: str) -> bool:
        pass


class Solution1(Solution):
    def is_palindrome(self, s: str) -> bool:
        s = list(s)
        s = [x.lower() for x in s if x.isdigit() or x.isalpha()]
        s = "".join(s)

        return s == s[::-1]


class Solution2(Solution):
    def is_palindrome(self, s: str) -> bool:
        sc1 = "`~!@#$%^&*()-_=+[]{}|;:',.<>/?\\"
        sc2 = '"'
        for x in sc1:
            s = s.replace(x, "")
        for y in sc2:
            s = s.replace(y, "")
        s = s.replace(" ", "")
        s = s.lower()

        return s == s[::-1]


class TestSolutions:
    @fixture
    def solutions(self) -> List[Solution]:
        return [Solution1(), Solution2()]

    data_provider = [
        ["A man, a plan, a canal: Panama", True],
        [" a ", True],
        ["#aba*", True],
        ["race a car", False],
        ["", True],
        [" ", True],
    ]

    @mark.parametrize("s, expected", data_provider)
    def test_is_palindrome(self, s: str, expected: bool, solutions):
        for solution in solutions:
            assert solution.is_palindrome(s) == expected
