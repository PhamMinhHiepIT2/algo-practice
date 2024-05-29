
from typing import List
from itertools import combinations


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        for i in range(3, len(nums)+1):
            all_sub_arr = self.generate_sub_seq(nums, i)
            for sub_arr in all_sub_arr:
                if self.check_sub_seq(sub_arr):
                    count += 1
        return count

    def check_sub_seq(self, sub_seq: List[int]) -> bool:
        diff = []
        for i in range(len(sub_seq)-1):
            diff.append((sub_seq[i+1]-sub_seq[i]))
        return len(list(set(diff))) == 1

    def generate_sub_seq(self, nums: List[int], k: int):
        all_combinations = list(combinations(nums, k))
        res = []
        for c in all_combinations:
            res.append(list(c))
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [-2147483648, 0, -2147483648]
    print(s.numberOfArithmeticSlices(nums))
    # print(s.generate_sub_seq(nums, 4))
