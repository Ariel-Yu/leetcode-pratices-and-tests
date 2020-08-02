from typing import List, Optional

from pytest import mark


class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def max_path_sum(self, root: TreeNode) -> int:
        def parse_tree(node: TreeNode, total: List[Optional[int]]) -> int:
            path = node.data
            left, right = 0, 0
            if node.left:
                left = parse_tree(node.left, total)
            if node.right:
                right = parse_tree(node.right, total)

            longest = max(path, path + left, path + right, path + left + right)
            if total[0] is None or longest > total[0]:
                total[0] = longest

            return max(path, path + left, path + right)

        total = [None]
        parse_tree(root, total)

        return total[0]


class TestSolution:
    @staticmethod
    def _deserialize_tree(values: List[str]) -> Optional[TreeNode]:
        def create_tree(values: List[str], index: List[int]) -> Optional[TreeNode]:
            if values[index[0]] == "null":
                index[0] += 1
                return None

            node = TreeNode(int(values[index[0]]))
            index[0] += 1
            node.left = create_tree(values, index)
            node.right = create_tree(values, index)

            return node

        return create_tree(values, [0])

    func = _deserialize_tree.__func__
    data_provider = [
        # All positive, Going through root
        [
            func(
                [
                    "1",
                    "2",
                    "4",
                    "null",
                    "null",
                    "5",
                    "null",
                    "null",
                    "6",
                    "null",
                    "null",
                ]
            ),
            14,
        ],
        # All positive, Not going through root
        [
            func(
                [
                    "1",
                    "2",
                    "4",
                    "null",
                    "null",
                    "5",
                    "null",
                    "null",
                    "1",
                    "null",
                    "null",
                ]
            ),
            11,
        ],
        # With negative, path
        [func(["0", "-2", "null", "null", "-3", "null", "null"]), 0],
        # With negative, path + left
        [func(["0", "2", "null", "null", "-3", "null", "null"]), 2],
        # With negative, path + right
        [func(["0", "-2", "null", "null", "3", "null", "null"]), 3],
        # With negative, path only
        [func(["-1", "null", "null"]), -1],
        # With negative, path + left only
        [func(["-1", "2", "null", "null", "null"]), 2],
        # With negative, path + right only
        [func(["-1", "null", "3", "null", "null"]), 3],
        # All negative, path
        [func(["-1", "-2", "null", "null", "-3", "null", "null"]), -1],
    ]

    @mark.parametrize("root, expected", data_provider)
    def test_max_path_sum(self, root: TreeNode, expected: int):
        solution = Solution()
        assert solution.max_path_sum(root) == expected
