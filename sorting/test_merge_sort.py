from typing import List

from pytest import mark


class MergeSort:
    """
    5, 8, 1, 3
    center: 2
    left: 5, 8
        center: 1
        left: 5
        right: 8
        l r k
        0 0 0
        1 0 1
        res: 5 8
    right: 1 3
        center: 1
        left: 1
        right: 3
        l r k
        1 0 1
        res: 1 3
    l r k
    0 2 2
    res: 1 3 5 8
    """

    def merge_sort(self, arr: List[int]) -> List[int]:
        if len(arr) < 2:
            return arr

        center = len(arr) // 2
        left = arr[:center]
        right = arr[center:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        res, l, r = [], 0, 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1

        if l < len(left):
            res = res + left[l:]
        if r < len(right):
            res = res + right[r:]

        return res


class TestQuickSort:
    data_provider = [
        [[5, 8, 1, 3, 7, 9, 2], [1, 2, 3, 5, 7, 8, 9],],
        [[-5, 0, 5, 10, 15], [-5, 0, 5, 10, 15],],
        [[15, 10, 5, 0, -5], [-5, 0, 5, 10, 15],],
        [[5, 5, 5, 5, 5, 3, 3, 3], [3, 3, 3, 5, 5, 5, 5, 5],],
        [
            [
                406,
                157,
                415,
                318,
                472,
                46,
                252,
                187,
                364,
                481,
                450,
                90,
                390,
                35,
                452,
                74,
                196,
                312,
                142,
                160,
                143,
                220,
                483,
                392,
                443,
                488,
                79,
                234,
                68,
                150,
                356,
                496,
                69,
                88,
                177,
                12,
                288,
                120,
                222,
                270,
                441,
                422,
                103,
                321,
                65,
                316,
                448,
                331,
                117,
                183,
                184,
                128,
                323,
                141,
                467,
                31,
                172,
                48,
                95,
                359,
                239,
                209,
                398,
                99,
                440,
                171,
                86,
                233,
                293,
                162,
                121,
                61,
                317,
                52,
                54,
                273,
                30,
                226,
                421,
                64,
                204,
                444,
                418,
                275,
                263,
                108,
                10,
                149,
                497,
                20,
                97,
                136,
                139,
                200,
                266,
                238,
                493,
                22,
                17,
                39,
            ],
            [
                10,
                12,
                17,
                20,
                22,
                30,
                31,
                35,
                39,
                46,
                48,
                52,
                54,
                61,
                64,
                65,
                68,
                69,
                74,
                79,
                86,
                88,
                90,
                95,
                97,
                99,
                103,
                108,
                117,
                120,
                121,
                128,
                136,
                139,
                141,
                142,
                143,
                149,
                150,
                157,
                160,
                162,
                171,
                172,
                177,
                183,
                184,
                187,
                196,
                200,
                204,
                209,
                220,
                222,
                226,
                233,
                234,
                238,
                239,
                252,
                263,
                266,
                270,
                273,
                275,
                288,
                293,
                312,
                316,
                317,
                318,
                321,
                323,
                331,
                356,
                359,
                364,
                390,
                392,
                398,
                406,
                415,
                418,
                421,
                422,
                440,
                441,
                443,
                444,
                448,
                450,
                452,
                467,
                472,
                481,
                483,
                488,
                493,
                496,
                497,
            ],
        ],
    ]

    @mark.parametrize("array, expected", data_provider)
    def test_quick_sort(self, array: List[int], expected: List[int]):
        solution = MergeSort()
        assert solution.merge_sort(array) == expected
