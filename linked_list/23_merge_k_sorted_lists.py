import unittest
from heapq import heappush, heappop
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


class SolutionPriorityQueue():
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


class SolutionHeapQ():
    def merge_k_sorted_lists(self, lists: List[ListNode]) -> ListNode:
        hq = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(hq, (lists[i].val, i, lists[i].next))

        first_list_node = ListNode()
        current_list_node = first_list_node
        while len(hq):
            item = heappop(hq)
            if item[2]:
                heappush(hq, (item[2].val, item[1], item[2].next))

            new_list_node = ListNode(item[0])
            current_list_node.next = new_list_node
            current_list_node = new_list_node

        return first_list_node.next


def get_linked_list_with_n_nodes(*args) -> ListNode:
    values = list(args)
    first_node = ListNode()
    current_node = first_node
    for value in values:
        new_node = ListNode(value)
        current_node.next = new_node
        current_node = new_node

    return first_node.next


class TestSolutionPriorityQueue(TestCase):
    def setUp(self):
        self.solution = SolutionPriorityQueue()

    def test_merge_k_linked_list(self):
        lists = [
            get_linked_list_with_n_nodes(1, 1, 2),
            get_linked_list_with_n_nodes(1, 5),
            get_linked_list_with_n_nodes(6)
        ]

        self.assertTrue(self.solution.merge_k_sorted_lists(lists) == get_linked_list_with_n_nodes(1, 1, 1, 2, 5, 6))

    def test_merge_0_linked_list(self):
        self.assertIsNone(self.solution.merge_k_sorted_lists([]))

    def test_merge_k_linked_list_with_empty_linked_list(self):
        lists = [
            get_linked_list_with_n_nodes(1, 1, 2),
            get_linked_list_with_n_nodes(),
            get_linked_list_with_n_nodes(6)
        ]

        self.assertTrue(self.solution.merge_k_sorted_lists(lists) == get_linked_list_with_n_nodes(1, 1, 2, 6))


class TestSolutionHeapQ(TestCase):
    def setUp(self):
        self.solution = SolutionHeapQ()

    def test_merge_k_sorted_lists(self):
        lists = [
            get_linked_list_with_n_nodes(1, 1, 2),
            get_linked_list_with_n_nodes(1, 5),
            get_linked_list_with_n_nodes(6)
        ]

        self.assertEqual(self.solution.merge_k_sorted_lists(lists), get_linked_list_with_n_nodes(1, 1, 1, 2, 5, 6))

    def test_merge_0_sorted_lists(self):
        self.assertIsNone(self.solution.merge_k_sorted_lists([]))

    def test_merge_k_sorted_lists_with_empty_linked_list(self):
        lists = [
            get_linked_list_with_n_nodes(1, 1, 2),
            get_linked_list_with_n_nodes(),
            get_linked_list_with_n_nodes(1, 6)
        ]

        self.assertEqual(self.solution.merge_k_sorted_lists(lists), get_linked_list_with_n_nodes(1, 1, 1, 2, 6))


def complexity_analysis():
    print("\nk linked lists, n total nodes")
    print("=> Time complexity: O(kn)")  # O(n(k + 1))
    print("* Initialized PriorityQueue/HeadQ: O(k)")
    print("* Fetch the smallest item from PriorityQueue/HeadQ for n times: O(k*n)")
    print("=> Space complexity: O(k)")
    print("* PriorityQueue/HeadQ: O(k)")


if __name__ == "__main__":
    complexity_analysis()
    print("\nRunning unit tests ...")
    unittest.main()
