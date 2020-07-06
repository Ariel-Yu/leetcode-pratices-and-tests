from typing import List

from pytest import fixture, mark

# 1. Will nums be empty?
# 2. Will the number be only integer?
# 3. Except for in-place modification, is there any time or space complexity restriction?


class Solution:
    def next_permutation(self, nums: List[int]):
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                next_big = None
                next_big_index = None
                for j in range(i, len(nums)):
                    if next_big is None or nums[i - 1] < nums[j] < next_big:
                        next_big = nums[j]
                        next_big_index = j
                tmp = nums[i - 1]
                nums[i - 1] = nums[next_big_index]
                nums[next_big_index] = tmp
                nums[i:] = sorted(nums[i:])
                return

        nums.sort()


class TestSolution:
    @fixture
    def solution(self) -> Solution:
        return Solution()

    _find_next_permutation_data_provider = [
        [[1, 2, 3], [1, 3, 2]],
        [[1, 4, 6, 5, 2], [1, 5, 2, 4, 6]],
        [[4, 3, 2, 1], [1, 2, 3, 4]],
        [[], []],
        [[5, -1, 0], [5, 0, -1]],
    ]

    @mark.parametrize("nums, expected", _find_next_permutation_data_provider)
    def test_find_next_permutation(self, nums: List[int], expected: List[int], solution):
        solution.next_permutation(nums)

        assert nums == expected


def complexity_analysis():
    print("=> Time complexity: O(n logn)")
    print("* Find the first descending number from the right: O(n)")
    print("* Sort the list from the next number of the first descending number until the end: O(n logn)")
    print("=> Space complexity: O(1)")
    print("* All the modification should be done in-place")


if __name__ == "__main__":
    complexity_analysis()
