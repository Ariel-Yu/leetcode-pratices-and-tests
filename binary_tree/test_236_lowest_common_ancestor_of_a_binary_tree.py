from abc import ABC, abstractmethod
from typing import List, Optional

from pytest import fixture, mark
from testfixtures import compare


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution(ABC):
    @abstractmethod
    def lowest_common_ancestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        pass


class SolutionAllCommonAncestors(Solution):
    def lowest_common_ancestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        common_ancestors = []

        def parse_tree(
            node: TreeNode, p: TreeNode, q: TreeNode, common_ancestors: List[TreeNode]
        ) -> int:
            if not node:
                return 0

            value = 0
            if node.val == p.val or node.val == q.val:
                value += 1
            if node.left:
                value += parse_tree(node.left, p, q, common_ancestors)
            if node.right:
                value += parse_tree(node.right, p, q, common_ancestors)

            if value == 2:
                common_ancestors.append(node)

            return value

        parse_tree(root, p, q, common_ancestors)
        return common_ancestors[0]


class SolutionLowestCommonAncestor(Solution):
    def lowest_common_ancestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        common_ancestor = []

        def parse_tree(
            node: TreeNode, p: TreeNode, q: TreeNode, common_ancestor: List[TreeNode]
        ) -> int:
            if not node:
                return 0

            mid = int(node.val == p.val or node.val == q.val)
            left = parse_tree(node.left, p, q, common_ancestor)
            right = parse_tree(node.right, p, q, common_ancestor)

            if mid + left + right == 2:
                common_ancestor.append(node)

            return max(mid, left, right)

        parse_tree(root, p, q, common_ancestor)
        return common_ancestor[0]


class TestSolutions:
    @fixture
    def solutions(self) -> List[Solution]:
        return [SolutionAllCommonAncestors(), SolutionLowestCommonAncestor()]

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

    func = deserialize_tree.__func__
    data_provider = [
        [
            func(
                [
                    3,
                    5,
                    6,
                    "null",
                    "null",
                    2,
                    7,
                    "null",
                    "null",
                    4,
                    "null",
                    "null",
                    1,
                    0,
                    "null",
                    "null",
                    8,
                    "null",
                    "null",
                ]
            ),
            func(
                [
                    5,
                    6,
                    "null",
                    "null",
                    2,
                    7,
                    "null",
                    "null",
                    4,
                    "null",
                    "null",
                    1,
                    0,
                    "null",
                    "null",
                    8,
                    "null",
                    "null",
                ]
            ),
            func([1, 0, "null", "null", 8, "null", "null"]),
            func(
                [
                    3,
                    5,
                    6,
                    "null",
                    "null",
                    2,
                    7,
                    "null",
                    "null",
                    4,
                    "null",
                    "null",
                    1,
                    0,
                    "null",
                    "null",
                    8,
                    "null",
                    "null",
                ]
            ),
        ],
        [
            func(
                [
                    3,
                    5,
                    6,
                    "null",
                    "null",
                    2,
                    7,
                    "null",
                    "null",
                    4,
                    "null",
                    "null",
                    1,
                    0,
                    "null",
                    "null",
                    8,
                    "null",
                    "null",
                ]
            ),
            func(
                [
                    5,
                    6,
                    "null",
                    "null",
                    2,
                    7,
                    "null",
                    "null",
                    4,
                    "null",
                    "null",
                    1,
                    0,
                    "null",
                    "null",
                    8,
                    "null",
                    "null",
                ]
            ),
            func([7, "null", "null"]),
            func(
                [
                    5,
                    6,
                    "null",
                    "null",
                    2,
                    7,
                    "null",
                    "null",
                    4,
                    "null",
                    "null",
                    1,
                    0,
                    "null",
                    "null",
                    8,
                    "null",
                    "null",
                ]
            ),
        ],
        [
            func(
                [
                    3,
                    5,
                    6,
                    "null",
                    "null",
                    2,
                    7,
                    "null",
                    "null",
                    4,
                    "null",
                    "null",
                    1,
                    0,
                    "null",
                    "null",
                    8,
                    "null",
                    "null",
                ]
            ),
            func(
                [
                    5,
                    6,
                    "null",
                    "null",
                    2,
                    7,
                    "null",
                    "null",
                    4,
                    "null",
                    "null",
                    1,
                    0,
                    "null",
                    "null",
                    8,
                    "null",
                    "null",
                ]
            ),
            func([0, "null", "null"]),
            func(
                [
                    3,
                    5,
                    6,
                    "null",
                    "null",
                    2,
                    7,
                    "null",
                    "null",
                    4,
                    "null",
                    "null",
                    1,
                    0,
                    "null",
                    "null",
                    8,
                    "null",
                    "null",
                ]
            ),
        ],
    ]

    @mark.parametrize("root, p, q, expected", data_provider)
    def test_solutions(
        self, root: TreeNode, p: TreeNode, q: TreeNode, expected: TreeNode, solutions
    ):
        for solution in solutions:
            compare(solution.lowest_common_ancestor(root, p, q), expected)
