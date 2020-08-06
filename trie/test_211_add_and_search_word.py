from typing import List, Optional

from pytest import mark

# Q1: Can the input search string be empty?


class TreeNode:
    def __init__(self, data: str):
        self.data = data
        self.children = {}
        self.terminated = False


class WordDictionary:
    def __init__(self):
        self.root = TreeNode("")

    def add(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                node.children[word[i]] = TreeNode(word[i])
            node = node.children[word[i]]
            if i == len(word) - 1:
                node.terminated = True

    def search(self, word: str) -> bool:
        def is_found(node: TreeNode, index: int) -> bool:
            found = False
            if word[index] == ".":
                if index == len(word) - 1:
                    return sum([x.terminated for x in node.children.values()]) != 0
                for child in node.children.values():
                    found = is_found(child, index + 1)
                    if found:
                        return True
            elif word[index] in node.children:
                if index == len(word) - 1:
                    return node.children[word[index]].terminated
                found = is_found(node.children[word[index]], index + 1)

            return found

        return is_found(self.root, 0)


class TestSolution:
    data_provider = [
        [
            [
                ["add", "bad"],
                ["add", "dad"],
                ["add", "mad"],
                ["search", "bad"],
                ["search", "pad"],
                ["search", ".ad"],
                ["search", "..d"],
                ["search", ".a."],
                ["search", "..."],
                ["search", "."],
                ["search", "...."],
            ],
            [None, None, None, True, False, True, True, True, True, False, False],
        ],
        [
            [
                ["add", "at"],
                ["add", "an"],
                ["add", "and"],
                ["add", "add"],
                ["search", "bat"],
                ["search", "an"],
                ["search", "and"],
                ["search", "an."],
                ["search", "..d"],
                ["search", "at."],
                ["add", "bat"],
                ["search", "bat"],
            ],
            [None, None, None, None, False, True, True, True, True, False, None, True],
        ],
    ]

    @mark.parametrize("actions, expected", data_provider)
    def test_add_and_search_word(
        self, actions: List[List[str]], expected: List[Optional[bool]]
    ):
        solution = WordDictionary()
        for i in range(len(actions)):
            method = getattr(solution, actions[i][0])
            assert method(actions[i][1]) == expected[i]
