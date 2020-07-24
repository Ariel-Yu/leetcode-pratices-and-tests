from typing import Optional


class TreeNode:
    def __init__(self, val: str):
        self.val = val
        self.children = {}
        self.terminated = False


class Solution:
    def __init__(self):
        self.root = TreeNode("")

    def insert(self, word: str) -> None:
        root = self.root
        for i in range(len(word)):
            if word[i] not in root.children:
                root.children[word[i]] = TreeNode(word[i])
            root = root.children[word[i]]
        root.terminated = True

    def search(self, word: str) -> bool:
        node = self._get_word(word)
        if not node:
            return False
        return node.terminated

    def starts_with(self, prefix: str) -> bool:
        return self._get_word(prefix) is not None

    def _get_word(self, word: str) -> Optional[TreeNode]:
        root = self.root
        for i in range(len(word)):
            if word[i] in root.children:
                root = root.children[word[i]]
            else:
                return None
        return root


class TestSolution:
    def test_solution(self):
        solution = Solution()
        solution.insert("apple")
        assert solution.search("apple")
        assert not solution.search("app")
        assert solution.starts_with("apple")
        assert solution.starts_with("app")
        assert not solution.search("apples")
        assert not solution.starts_with("apples")

        solution.insert("app")
        assert solution.search("app")
        assert solution.starts_with("app")
        assert not solution.search("apps")
        assert not solution.starts_with("apps")

        solution.insert("apt")
        assert solution.search("apt")
        assert solution.starts_with("apt")
        assert not solution.search("ap")
        assert solution.starts_with("ap")
