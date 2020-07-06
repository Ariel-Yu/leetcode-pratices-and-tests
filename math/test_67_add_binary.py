from pytest import mark

# 1. Will the input strings be empty?
# 2. Do the input strings only consist of "0" and "1"?
# 3. Will the input strings have leading "0"s?
# 4. Is there limitation of the length of the input strings?


class Solution:
    def add_binary(self, a: str, b: str) -> str:
        binary_string = ""
        a = a[-1::-1]
        b = b[-1::-1]
        longer, shorter = a, b
        if len(a) < len(b):
            longer, shorter = b, a

        carry = 0
        for i in range(len(longer)):
            add = carry + int(longer[i])
            if len(shorter) > i:
                add += int(shorter[i])
            if add > 1:
                carry = 1
                add -= 2
            else:
                carry = 0
            binary_string = str(add) + binary_string

        if carry:
            binary_string = str(carry) + binary_string

        return binary_string


class TestSolution:
    data_provider = [
        [
            "1",
            "11",
            "100"
        ],
        [
            "100",
            "0",
            "100"
        ],[
            "11",
            "11",
            "110"
        ],
        [
            "100",
            "100",
            "1000"
        ]
    ]

    @mark.parametrize("a, b, expected", data_provider)
    def test_solution(self, a: str, b: str, expected: str):
        solution = Solution()
        assert solution.add_binary(a, b) == expected
