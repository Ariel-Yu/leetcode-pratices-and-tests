from typing import List

from pytest import fixture, mark

# 1. Are the intervals sorted?
# 2. Will the first element of an interval larger than the second element of an interval?
# 3. Can the input list be empty?
# 4. Are the elements of the intervals number (integer/float) only?


class Solution:
    def merge_intervals(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()

        merged_intervals = []
        pre = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= pre[1]:
                pre[1] = max(pre[1], intervals[i][1])
            else:
                merged_intervals.append(pre)
                pre = intervals[i]
        merged_intervals.append(pre)

        return merged_intervals


class TestSolution:
    @fixture
    def solution(self) -> Solution:
        return Solution()

    data_provider = [
        [[[1, 2], [3, 8], [3, 6], [6, 10], [12, 15]], [[1, 2], [3, 10], [12, 15]]],
        [[], []],
        [[[5, 10], [-3, -1], [8, 12], [1, 1]], [[-3, -1], [1, 1], [5, 12]]],
        [[[1, 4], [4, 6], [6, 8]], [[1, 8]]],
    ]

    @mark.parametrize("intervals, merged_intervals", data_provider)
    def test_solution(
        self, intervals: List[List[int]], merged_intervals: List[List[int]], solution
    ):
        assert solution.merge_intervals(intervals) == merged_intervals


def complexity_analysis():
    print("=> Time complexity: O(n logn)")
    print("* Sort imported list of intervals: O(n logn)")
    print("* Loop throught the imported list: O(n)")
    print("=> Space complexity: O(n)")
    print("* Returned list of merged intervals: O(n)")


if __name__ == "__main__":
    complexity_analysis()
