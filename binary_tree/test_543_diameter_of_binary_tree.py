from typing import List, Optional

from pytest import mark


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.right = None
        self.left = None


class Solution:
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        if not root:
            return 0

        def find_path(node: TreeNode, path: int, res: List[int]) -> int:
            left, right = 0, 0
            if node.left:
                left = find_path(node.left, path + 1, res)
            if node.right:
                right = find_path(node.right, path + 1, res)
            combine = left + right - 2 * path
            res[0] = max(combine, res[0])

            path = max(path, left, right)
            return path

        res = [0]
        path = find_path(root, 0, res)

        return max(path, res[0])


class TestSolution:
    @staticmethod
    def _deserialize(values: List[str]) -> Optional[TreeNode]:
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

    func = _deserialize.__func__
    data_provider = [
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
                    "3",
                    "null",
                    "null",
                ]
            ),
            3,
        ],
        [
            func(
                [
                    "1",
                    "2",
                    "4",
                    "6",
                    "8",
                    "null",
                    "null",
                    "null",
                    "null",
                    "5",
                    "null",
                    "7",
                    "null",
                    "9",
                    "null",
                    "null",
                    "3",
                    "null",
                    "null",
                ]
            ),
            6,
        ],
        [None, 0],
        [func(["1", "null", "null"]), 0],
    ]

    @mark.parametrize("root, expected", data_provider)
    def test_diameter_of_binary_tree(self, root: Optional[TreeNode], expected):
        solution = Solution()
        assert solution.diameter_of_binary_tree(root) == expected
