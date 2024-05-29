from typing import List
from time import time


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        def find_2ndmax(nums: List[int], max_num: int):
            for i in range(len(nums)):
                if nums[i] < max_num:
                    return i
            return 0

        if len(set(list(nums))) == 1:
            return 0

        res = 0
        while len(set(list(nums))) != 1:
            nums.sort(reverse=True)
            second_max_num_idx = find_2ndmax(nums, nums[0])
            nums[0] = nums[second_max_num_idx]
            res += 1
        return res

    def reductionOperations01(self, nums):
        n = len(nums)
        freq = [0] * (n+1)
        for num in nums:
            freq[num] += 1
        print(freq)
        res, operations = 0, 0
        for i in range(n, 0, -1):
            if freq[i] > 0:
                operations += freq[i]
                res += operations - freq[i]
                print(operations, res)
        return res


if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3]
    sol = Solution()
    print(sol.reductionOperations01(nums))
