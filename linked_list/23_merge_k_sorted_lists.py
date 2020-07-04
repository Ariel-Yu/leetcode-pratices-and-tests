import unittest
from queue import PriorityQueue
from typing import List
from unittest import TestCase


class ListNode():
    def __init__(self, val: int = None, next = None):
        self.val = val
        self.next = next

    def _get_values(self, list_node) -> List:
        values = []
        while list_node:
            values.append(list_node.val)
            list_node = list_node.next

        return values

    def __eq__(self, other):
        return self._get_values(self) == self._get_values(other)


class Solution():
    def merge_k_sorted_lists(self, lists: List[ListNode]) -> ListNode:
        pq = PriorityQueue()
        for i in range(len(lists)):
            if lists[i]:
                # value, index as tie_breaker, next_node
                pq.put((lists[i].val, i, lists[i].next))

        first_list_node = ListNode()
        current_list_node = first_list_node
        while not pq.empty():
            item = pq.get()
            new_list_node = ListNode(item[0])
            if item[2]:
                pq.put((item[2].val, item[1], item[2].next))

            current_list_node.next = new_list_node
            current_list_node = new_list_node

        return first_list_node.next


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge_k_linked_list(self):
        lists = [
            self._linked_list_with_n_nodes(1, 1, 2),
            self._linked_list_with_n_nodes(1, 5),
            self._linked_list_with_n_nodes(6)
        ]

        self.assertTrue(self.solution.merge_k_sorted_lists(lists) == self._linked_list_with_n_nodes(1, 1, 1, 2, 5, 6))

    def test_merge_0_linked_list(self):
        lists = []

        self.assertEqual(self.solution.merge_k_sorted_lists(lists), None)

    def test_merge_k_linked_list_with_empty_linked_list(self):
        lists = [
            self._linked_list_with_n_nodes(1, 1, 2),
            self._linked_list_with_n_nodes(),
            self._linked_list_with_n_nodes(6)
        ]

        self.assertTrue(self.solution.merge_k_sorted_lists(lists) == self._linked_list_with_n_nodes(1, 1, 2, 6))

    def _linked_list_with_n_nodes(self, *args) -> ListNode:
        values = list(args)
        first_node = ListNode()
        current_node = first_node
        for value in values:
            new_node = ListNode(value)
            current_node.next = new_node
            current_node = new_node

        return first_node.next


def complexity_analysis():
    print("\nk linked lists, n total nodes")
    print("=> Time complexity: O(kn)")
    print("* Initialized PriorityQueue: O(k)")
    print("* Fetch the smallest item from PriorityQueue for n times: O(k*n)")
    print("=> Space complexity: O(k)")
    print("* PriorityQueue: O(k)")
    print("\nRunning unit tests ...")


if __name__ == "__main__":
    complexity_analysis()
    unittest.main()
