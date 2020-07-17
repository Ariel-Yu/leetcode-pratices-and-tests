from collections import defaultdict
from typing import Dict, List

from pytest import mark


class Solution:
    def find_all_anagrams(self, s: str, p: str) -> List[int]:
        def get_ht(s: str) -> Dict:
            ht = defaultdict(int)
            for i in range(len(s)):
                ht[s[i]] += 1
            return ht

        def is_equal(a: Dict, b: Dict) -> bool:
            """
            defaultdict will not remove the key with value 0, thus, in this method, the following
            scenario will be evaluated as is_equal.
            It suits for this problem but maybe not for other problems.

            a = {'a': 1, 'b': 1}
            b = {'a': 1, 'b': 1, 'c': 0}

            :param a: should be p in this use case
            :param b: should be the comparing subset of s
            :return: bool
            """
            for key, value in a.items():
                if key not in b:
                    return False
                if b[key] != value:
                    return False
            return True

        p_len = len(p)
        p = get_ht(p)
        ht = get_ht(s[:p_len])
        res = []
        if is_equal(p, ht):
            res.append(0)
        for i in range(1, len(s) - p_len + 1):
            ht[s[i - 1]] -= 1
            ht[s[i + p_len - 1]] += 1
            if is_equal(p, ht):
                res.append(i)

        return res


class TestSolution:
    data_provider = [
        ["abbaababbaba", "abab", [0, 1, 2, 4, 6, 8]],
        ["aaa", "aa", [0, 1]],
        ["ad", "bc", []],
        ["dabc", "abc", [1]],
    ]

    @mark.parametrize("s, p, expected", data_provider)
    def test_find_all_anagrams(self, s: str, p: str, expected: List[int]):
        solution = Solution()
        assert solution.find_all_anagrams(s, p) == expected
