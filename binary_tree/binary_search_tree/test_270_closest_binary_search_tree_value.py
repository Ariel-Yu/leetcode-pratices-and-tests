from abc import ABC, abstractmethod
from typing import Tuple, List

from pytest import fixture, mark


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution(ABC):
    @abstractmethod
    def closest_value(self, root: TreeNode, target: float) -> int:
        pass


class SolutionParseTreeAndCompare(Solution):
    def closest_value(self, root: TreeNode, target: float) -> int:
        sd = tuple((None, None)) # tuple (distance, value)

        def parse_tree_and_compare(node: TreeNode, target: float, sd: tuple) -> Tuple[float, int]:
            if node.left:
                sd = parse_tree_and_compare(node.left, target, sd)
                if sd[1] > target:
                    return sd

            value = node.val
            diff = abs(value - target)
            if sd[0] is None or diff < sd[0]:
                sd = tuple((diff, value))
                if value > target:
                    return sd

            if node.right:
                sd = parse_tree_and_compare(node.right, target, sd)

            return sd

        return parse_tree_and_compare(root, target, sd)[1]


class TestSolutions:
    @fixture
    def solutions(self) -> List[Solution]:
        return [
            SolutionParseTreeAndCompare()
        ]

    @staticmethod
    def get_tree() -> TreeNode:
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)

        node2.left = node1
        node2.right = node3

        node6.left = node5

        node4.left = node2
        node4.right = node6

        return node4

    func = get_tree.__func__
    data_provider = [
        [
            func(),
            3.75,
            4
        ],
        [
            func(),
            2.25,
            2
        ],
        [
            func(),
            6.05,
            6
        ],
    ]

    @mark.parametrize("root, target, expected", data_provider)
    def test_closest_value(self, root: TreeNode, target: int, expected: int, solutions):
        for solution in solutions:
            assert solution.closest_value(root, target) == expected

# Immutable objects: string, number, tuple => pass by value
# Mutable objects: list, dictionary => pass by reference
# https://stackoverflow.com/questions/534375/passing-values-in-python#:~:text=8%20Answers&text=Python%20passes%20references%2Dto%2Dobjects%20by%20value.&text=Some%20objects%2C%20like%20strings%2C%20tuples,function%2Fmethod%20is%20not%20changed.
