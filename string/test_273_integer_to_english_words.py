from pytest import mark


class Solution:
    def number_to_words(self, num: int) -> str:
        if not num:
            return "zero"

        mapping = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
        }

        ten_mapping = {
            2: "twenty",
            3: "thirty",
            4: "forty",
            5: "fifty",
            6: "sixty",
            7: "seventy",
            8: "eighty",
            9: "ninety",
        }

        units = {3: "hundred", 4: "thousand", 7: "million", 10: "billion"}

        res = ""
        index = 0
        pre = None
        agg = 0
        pre_unit = None
        while num > 0:
            index += 1
            sub_index = index % 3
            digit = num % 10
            num //= 10

            if index > 3 and sub_index == 1:
                res = units[index] + " " + res
                pre_unit = units[index]

            if sub_index == 1:
                pre = digit
                agg += digit
            elif sub_index == 2:
                if digit != 0:
                    if digit < 2:
                        res = mapping[digit * 10 + pre] + " " + res
                    else:
                        if pre:
                            res = ten_mapping[digit] + " " + mapping[pre] + " " + res
                        else:
                            res = ten_mapping[digit] + " " + res
                else:
                    if pre:
                        res = mapping[pre] + " " + res
                pre = None
                agg += digit
            else:
                agg += digit
                if digit != 0:
                    res = mapping[digit] + " " + units[3] + " " + res

                if pre_unit and not agg:
                    res = res.replace(pre_unit, "")
                    res = res.lstrip()
                    pre_unit = None

        if pre:
            res = mapping[pre] + " " + res

        return res.rstrip()


class TestSolution:
    data_provider = [
        [
            1234567891,
            "one billion two hundred thirty four million five hundred sixty seven thousand eight hundred ninety one",
        ],
        [1012, "one thousand twelve"],
        [1010, "one thousand ten"],
        [1050, "one thousand fifty"],
        [2301, "two thousand three hundred one"],
        [1000000, "one million"],
        [1000000000, "one billion"],
        [100, "one hundred"],
        [100000, "one hundred thousand"],
        [100000000, "one hundred million"],
        [0, "zero"],
    ]

    @mark.parametrize("num, expected", data_provider)
    def test_number_to_words(self, num: int, expected: str):
        solution = Solution()
        assert solution.number_to_words(num) == expected
