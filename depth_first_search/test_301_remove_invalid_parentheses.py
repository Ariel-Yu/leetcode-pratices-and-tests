from typing import List

from pytest import mark


class Solution:
    def remove_invalid_parentheses(self, s: str) -> List[str]:
        l = r = stack = 0
        for value in s:
            if value == "(":
                stack += 1
            elif value == ")":
                if not stack:
                    r += 1
                else:
                    stack -= 1
        l = stack

        def dfs(i: int, current: str, l: int, r: int, balance: int):
            if l < 0 or r < 0 or balance < 0:
                return
            if i == len(s):
                if l == r == balance == 0:
                    res.add(current)
                return
            if s[i] == "(":
                dfs(i + 1, current, l - 1, r, balance)  # discard this left
                dfs(i + 1, current + s[i], l, r, balance + 1)  # keep this left
            elif s[i] == ")":
                dfs(i + 1, current, l, r - 1, balance)  # discard this right
                dfs(i + 1, current + s[i], l, r, balance - 1)  # keep this right
            else:
                dfs(i + 1, current + s[i], l, r, balance)  # add the value

        res = set()
        dfs(0, "", l, r, 0)

        return list(res)


class TestSolution:
    data_provider = [
        ["()())()", ["()()()", "(())()"],],
        ["(a)())()", ["(a)()()", "(a())()"],],
        ["()))((()", ["()()"],],
        ["a)b(c", ["abc"],],
        ["", [""],],
    ]

    @mark.parametrize("s, expected", data_provider)
    def test_remove_invalid_parentheses(self, s: str, expected: List[str]):
        solution = Solution()
        assert sorted(solution.remove_invalid_parentheses(s)) == sorted(expected)
