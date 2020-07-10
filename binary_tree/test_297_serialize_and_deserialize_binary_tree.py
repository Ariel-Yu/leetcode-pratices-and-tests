from typing import List, Optional

from pytest import fixture


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

    def __eq__(self, other):
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right
        )


class Solution:
    def serialize(self, root: TreeNode) -> str:
        returned_str = ""

        def parse_tree(node: TreeNode, values: str) -> str:
            if not node:
                values += ",null"
                return values

            values += f",{node.val}"
            values = parse_tree(node.left, values)
            values = parse_tree(node.right, values)

            return values

        return parse_tree(root, returned_str)[1:]

    def deserialize(self, data: str) -> TreeNode:
        values = data.split(",")

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


class TestSolution:
    @fixture
    def solution(self) -> Solution:
        return Solution()

    def test_serialize(self, solution):
        assert solution.serialize(self._get_tree()) == self._get_string()

    def test_deserialize(self, solution):
        assert solution.deserialize(self._get_string()) == self._get_tree()

    def test_serialize_deserialize(self, solution):
        assert (
            solution.deserialize(solution.serialize(self._get_tree()))
            == self._get_tree()
        )

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

    def _get_string(self) -> str:
        return "1,2,null,null,3,4,null,null,5,null,null"
