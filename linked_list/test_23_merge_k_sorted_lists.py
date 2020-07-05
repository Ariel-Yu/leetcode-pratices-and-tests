from abc import ABC, abstractmethod
from heapq import heappop, heappush
from queue import PriorityQueue
from typing import List

from pytest import fixture

# Will the given list of ListNode be empty?
# Will any ListNode be emtpy?
# What is an empty ListNode? ListNode(0, None) or None
# Can the val of ListNode be only integer or possibly also float and character?
# Is there any time complexity and space complexity restriction?


class ListNode():
    def __init__(self, val: int = None, next = None):
        self.val = val
        self.next = next

    def _get_values(self) -> List:
        values = []
        list_node = self
        while list_node:
            values.append(list_node.val)
            list_node = list_node.next

        return values

    def __eq__(self, other):
        return self._get_values() == other._get_values()


class Solution(ABC):
    @abstractmethod
    def merge_k_sorted_lists(self, lists: List[ListNode]) -> ListNode:
        pass


class SolutionPriorityQueue(Solution):
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
            if item[2]:
                pq.put((item[2].val, item[1], item[2].next))

            new_list_node = ListNode(item[0])
            current_list_node.next = new_list_node
            current_list_node = new_list_node

        return first_list_node.next


class SolutionHeapQ(Solution):
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


class SolutionListSorting(Solution):
    def linked_list_to_list(self, linked_list: ListNode) -> List:
        values = []
        while linked_list:
            values.append(linked_list.val)
            linked_list = linked_list.next

        return values

    def list_to_linked_list(self, values: List) -> ListNode:
        first_list_node = ListNode()
        current_list_node = first_list_node
        for value in values:
            new_list_node = ListNode(value)
            current_list_node.next = new_list_node
            current_list_node = new_list_node

        return first_list_node.next

    def merge_k_sorted_lists(self, lists: List[ListNode]) -> ListNode:
        merged_list = []
        for linked_list in lists:
            merged_list.extend(self.linked_list_to_list(linked_list))
        merged_list.sort()

        return self.list_to_linked_list(merged_list)


class TestSolutions():
    @fixture
    def solutions(self) -> List[Solution]:
        return [
            SolutionPriorityQueue(),
            SolutionHeapQ(),
            SolutionListSorting()
        ]

    def test_merge_k_linked_list(self, solutions):
        lists = [
            self._get_linked_list_with_n_nodes(1, 1, 2),
            self._get_linked_list_with_n_nodes(1, 5),
            self._get_linked_list_with_n_nodes(6)
        ]

        for solution in solutions:
            assert solution.merge_k_sorted_lists(lists) == self._get_linked_list_with_n_nodes(1, 1, 1, 2, 5, 6)

    def test_merge_0_linked_list(self, solutions):
        for solution in solutions:
            assert solution.merge_k_sorted_lists([]) is None

    def test_merge_k_linked_list_with_empty_linked_list(self, solutions):
        lists = [
            self._get_linked_list_with_n_nodes(1, 1, 2),
            self._get_linked_list_with_n_nodes(),
            self._get_linked_list_with_n_nodes(6)
        ]

        for solution in solutions:
            assert solution.merge_k_sorted_lists(lists) == self._get_linked_list_with_n_nodes(1, 1, 2, 6)

    def _get_linked_list_with_n_nodes(self, *args) -> ListNode:
        values = list(args)
        first_node = ListNode()
        current_node = first_node
        for value in values:
            new_node = ListNode(value)
            current_node.next = new_node
            current_node = new_node

        return first_node.next


def complexity_analysis_priority_queues():
    print("\nPriorityQueue/HeadQ complexity analysis:")
    print("k linked lists, n total nodes")
    print("=> Time complexity: O(kn)")  # O(n(k + 1))
    print("* Initialized PriorityQueue/HeadQ: O(k)")
    print("* Fetch the smallest item from PriorityQueue/HeadQ for n times: O(k*n)")
    print("=> Space complexity: O(k)")
    print("* PriorityQueue/HeadQ: O(k)")


def complexity_analysis_list_sorting():
    print("\nList sorting complexity analysis:")
    print("k linked lists, n total nodes")
    print("=> Time complexity: O(n logn)")  # O(n(logn + 2))
    print("* All ListNodes to lists: O(n)")
    print("* Sort the merged list: O(n logn)")
    print("* Merged list to ListNode: O(n)")
    print("=> Space complexity: O(n)")
    print("* Merged list: O(n)")


if __name__ == "__main__":
    complexity_analysis_priority_queues()
    complexity_analysis_list_sorting()
