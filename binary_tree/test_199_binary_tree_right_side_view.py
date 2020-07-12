from abc import ABC, abstractmethod
from typing import List, Optional

from pytest import fixture, mark


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution(ABC):
    @abstractmethod
    def right_side_view(self, root: TreeNode) -> List[int]:
        pass


class SolutionBFS(Solution):
    def right_side_view(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        values = []
        queue = [root]

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            values.append(level)

        return [value[-1] for value in values]


class SolutionDFS(Solution):
    def right_side_view(self, root: TreeNode) -> List[int]:
        values = []

        def parse_tree(node: TreeNode, index: int):
            if not node:
                return

            if len(values) == index:
                values.append([])

            values[index].append(node.val)
            if node.left:
                parse_tree(node.left, index + 1)
            if node.right:
                parse_tree(node.right, index + 1)

        parse_tree(root, 0)
        return [value[-1] for value in values]


class TestSolutions:
    @fixture
    def solutions(self) -> List[Solution]:
        return [SolutionBFS(), SolutionDFS()]

    @staticmethod
    def deserialize_tree(values: List[int]) -> TreeNode:
        def create_tree(values: List[int], index: List[int]) -> Optional[TreeNode]:
            if values[index[0]] == "null":
                index[0] += 1
                return None

            node = TreeNode(values[index[0]])
            index[0] += 1
            node.left = create_tree(values, index)
            node.right = create_tree(values, index)

            return node

        return create_tree(values, [0])

    # This is the trick to get the static function in a class ...
    # https://stackoverflow.com/questions/41921255/staticmethod-object-is-not-callable
    func = deserialize_tree.__func__
    data_provider = [
        [
            func([1, 2, 4, "null", "null", "null", 3, 5, "null", "null", "null"]),
            [1, 3, 5],
        ],
        [func([1, 2, 4, "null", "null", "null", 3, "null", "null"]), [1, 3, 4]],
        [func([1, 2, 4, "null", "null", "null", "null"]), [1, 2, 4]],
        [None, []],
    ]

    @mark.parametrize("root, expected", data_provider)
    def test_right_side_view(self, root: TreeNode, expected: List[int], solutions):
        for solution in solutions:
            assert solution.right_side_view(root) == expected
