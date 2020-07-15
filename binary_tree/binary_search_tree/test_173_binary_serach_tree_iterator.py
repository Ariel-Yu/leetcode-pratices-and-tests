from abc import ABC, abstractmethod
from typing import List

from pytest import fixture

# 1. Is the tree finite?
# 2. Is there any restriction of time and space complexity? O(1), O(h)


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution(ABC):
    @abstractmethod
    def next(self) -> int:
        pass

    @abstractmethod
    def has_next(self) -> bool:
        pass


class SolutionDFS(Solution):
    def __init__(self, root: TreeNode):
        self.values = []
        self._parse_tree(root)

    def _parse_tree(self, node: TreeNode):
        if not node:
            return

        if node.left:
            self._parse_tree(node.left)
        self.values.append(node.val)
        if node.right:
            self._parse_tree(node.right)

    def next(self) -> int:
        return self.values.pop(0)

    def has_next(self) -> bool:
        return len(self.values) != 0


class SolutionControlledRecursion(Solution):
    def __init__(self, root: TreeNode):
        self.nodes = []
        self._traverse_left(root)

    def _traverse_left(self, node: TreeNode):
        if not node:
            return

        self.nodes.append(node)
        if node.left:
            self._traverse_left(node.left)

    def next(self) -> int:
        node = self.nodes.pop()
        if node.right:
            self._traverse_left(node.right)
        return node.val

    def has_next(self) -> bool:
        return len(self.nodes) != 0


class TestSolutions:
    @fixture
    def solutions(self) -> List[Solution]:
        return [
            SolutionDFS(self._get_tree()),
            SolutionControlledRecursion(self._get_tree()),
        ]

    def _get_tree(self) -> TreeNode:
        node5 = TreeNode(5)
        node4 = TreeNode(4)
        node3 = TreeNode(3)
        node2 = TreeNode(2)
        node1 = TreeNode(1)

        node1.left = node2
        node1.right = node3
        node3.left = node4
        node3.right = node5

        return node1

    def test_solutions(self, solutions):
        for solution in solutions:
            assert solution.next() == 2
            assert solution.has_next()

            assert solution.next() == 1
            assert solution.has_next()

            assert solution.next() == 4
            assert solution.has_next()

            assert solution.next() == 3
            assert solution.has_next()

            assert solution.next() == 5
            assert not solution.has_next()
