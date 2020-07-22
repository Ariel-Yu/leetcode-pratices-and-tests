from typing import List

from pytest import mark


class Solution:
    def is_alien_sorted(self, words: List[str], order: str) -> bool:
        map_order = {x: i for i, x in enumerate(list(order))}

        for i in range(1, len(words)):
            if words[i - 1][: len(words[i])] == words[i] and len(words[i - 1]) > len(
                words[i]
            ):
                return False
            for k in range(len(words[i])):
                if k < len(words[i - 1]):
                    if map_order[words[i - 1][k]] < map_order[words[i][k]]:
                        break
                    elif map_order[words[i - 1][k]] > map_order[words[i][k]]:
                        return False

        return True


class TestSolution:
    data_provider = [
        [["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True],
        [["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False],
        [["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False],
        [["apap", "app"], "abcdefghijklmnopqrstuvwxyz", True],
    ]

    @mark.parametrize("words, order, expected", data_provider)
    def test_is_alien_sorted(self, words: List[str], order: str, expected: bool):
        solution = Solution()
        assert solution.is_alien_sorted(words, order) == expected
