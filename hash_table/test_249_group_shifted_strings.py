from collections import defaultdict
from typing import List

from pytest import mark


class Solution:
    def get_grouping(self, s: str) -> tuple:
        scores = []
        for i in range(1, len(s)):
            tmp = ord(s[i]) - ord(s[i - 1])
            if tmp < 0:
                tmp += 26
            scores.append(tmp)
        return tuple(scores)

    def group_strings(self, strings: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for string in strings:
            group = self.get_grouping(string)
            results[group].append(string)

        return results.values()


class TestSolution:
    data_provider = [
        [
            [
                "abc",
                "bcd",
                "acef",
                "xyz",
                "az",
                "ba",
                "a",
                "z",
                "yza",
                "zbce",
                "zbde",
                "abd",
                "acd",
            ],
            [
                ["a", "z"],
                ["abd"],
                ["acef", "zbde"],
                ["acd"],
                ["zbce"],
                ["abc", "bcd", "xyz", "yza"],
                ["az", "ba"],
            ],
        ]
    ]

    @mark.parametrize("strings, expected", data_provider)
    def test_group_strings(self, strings: List[str], expected: List[List[str]]):
        solution = Solution()
        assert self._results_to_expected(solution.group_strings(strings)) == sorted(
            expected
        )

    def _results_to_expected(self, values):
        return sorted([value for value in values])
