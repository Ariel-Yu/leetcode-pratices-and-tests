from typing import List

from pytest import fixture


class NestedInteger:
    def __init__(self, value: int = None):
        if value is None:
            self.value = []
        else:
            self.value = value

    def is_integer(self) -> bool:
        return isinstance(self.value, int)

    def add(self, element):
        if isinstance(self.value, list):
            self.value.append(element)
        else:
            self.value = [self.value, element]

    def set_integer(self, value: int):
        self.value = value

    def get_integer(self):
        if isinstance(self.value, list):
            return None
        else:
            return self.value

    def get_list(self):
        if isinstance(self.value, list):
            return self.value
        else:
            return None


class Solution:
    def depth_sum(self, nested_list: List[NestedInteger]) -> int:
        def parse_nested_integer(
            nested_integer: NestedInteger, depth: int, total: List[int]
        ):
            if nested_integer.is_integer():
                total[0] += nested_integer.get_integer() * depth
            else:
                for value in nested_integer.get_list():
                    if value.is_integer():
                        total[0] += value.get_integer() * (depth + 1)
                    else:
                        parse_nested_integer(value, depth + 1, total)

        total = [0]
        for nested_integer in nested_list:
            parse_nested_integer(nested_integer, 1, total)

        return total[0]


class TestSolution:
    @fixture
    def solution(self) -> Solution:
        return Solution()

    def test_nested_integer_with_depth_one(self, solution):
        assert solution.depth_sum(self._get_nested_integer_with_depth_one()) == 6

    def test_nested_integer_with_depth_two(self, solution):
        assert solution.depth_sum(self._get_nested_integer_with_depth_two()) == 10

    def test_nested_integer_with_depth_three(self, solution):
        assert solution.depth_sum(self._get_nested_integer_with_depth_three()) == 11

    @staticmethod
    def _get_nested_integer_with_depth_one() -> List[NestedInteger]:
        # [1, 2, 3]
        nested_integer1 = NestedInteger(1)
        nested_integer2 = NestedInteger(2)
        nested_integer3 = NestedInteger(3)

        return [nested_integer1, nested_integer2, nested_integer3]

    @staticmethod
    def _get_nested_integer_with_depth_two() -> List[NestedInteger]:
        # [[1, 1], 2, [1, 1]]
        nested_integer = NestedInteger()
        nested_integer1 = NestedInteger(1)
        nested_integer.add(nested_integer1)
        nested_integer.add(nested_integer1)
        nested_integer2 = NestedInteger(2)

        return [nested_integer, nested_integer2, nested_integer]

    @staticmethod
    def _get_nested_integer_with_depth_three() -> List[NestedInteger]:
        # [[1, [2]], 3]
        nested_integer = NestedInteger()
        nested_integer1 = NestedInteger(1)
        nested_integer.add(nested_integer1)

        nested_integer2 = NestedInteger()
        nested_integer2_2 = NestedInteger(2)
        nested_integer2.add(nested_integer2_2)
        nested_integer.add(nested_integer2)

        nested_integer3 = NestedInteger(3)

        return [nested_integer, nested_integer3]
