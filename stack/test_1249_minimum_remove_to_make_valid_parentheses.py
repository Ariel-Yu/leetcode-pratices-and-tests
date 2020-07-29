from pytest import mark


class Solution:
    def min_remove_to_make_valid_parentheses(self, s: str) -> str:
        remove = []
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if not stack:
                    remove.append(i)
                else:
                    stack.pop()
        remove.extend(stack)

        for j in range(len(remove)):
            s = s[:remove[j] - j] + s[remove[j] - j + 1:]

        return s


class TestSolution:
    data_provider = [
        [
            "((a)))",
            "((a))"
        ],
        [
            "))((",
            ""
        ],
        [
            "(()a(()",
            "()a()"
        ],
    ]

    @mark.parametrize("s, expected", data_provider)
    def test_min_remove_to_make_valid_parentheses(self, s: str, expected: str):
        solution = Solution()
        assert solution.min_remove_to_make_valid_parentheses(s) == expected
