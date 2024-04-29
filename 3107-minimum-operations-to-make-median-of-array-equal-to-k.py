from typing import List
import math


def solve(nums: List[int], k: int):
    sorted_nums = sorted(nums)
    n = len(nums)
    med_idx = math.floor(n/2)
    med_num = sorted_nums[med_idx]
    count = 0
    # print(f"Sorted nums = {sorted_nums}")
    # print(f"Med index={med_idx}, Med num={med_num}")
    if k == med_num:
        return 0
    if k < med_num:
        if k <= sorted_nums[0]:
            count = sum(sorted_nums[:med_idx+1]) - (med_idx+1)*k
            return count
        else:
            for i in range(0, med_idx+1):
                # print(
                #     f"Checking i={i}, nums[i]={sorted_nums[i]}, nums[i+1]={sorted_nums[i+1]}")
                if sorted_nums[i] <= k and k <= sorted_nums[i+1]:
                    count = sum(sorted_nums[i+1:med_idx+1]) - k*(med_idx-i)
                    return count
    if k > med_num:
        for i in range(med_idx, n):
            if i+1 < n:
                if sorted_nums[i] <= k and k <= sorted_nums[i+1]:
                    # print(
                    #     f"Checking i={i}, nums[i]={sorted_nums[i]}, nums[i+1]={sorted_nums[i+1]}")
                    count = k*(i-med_idx+1) - sum(sorted_nums[med_idx:i+1])
                    return count
            else:
                count = k*(i-med_idx+1) - sum(sorted_nums[med_idx:i+1])
                return count
    return count


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        res = solve(nums=nums, k=k)
        # print(res)
        return res


if __name__ == "__main__":

    sol = Solution()
    nums = [2, 5, 6, 8, 5]
    k = 7
    sol.minOperationsToMakeMedianK(nums, k)

    nums = [1]
    k = 10000
    sol.minOperationsToMakeMedianK(nums, k)
