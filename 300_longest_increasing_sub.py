from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        if len(list(set(nums))) == 1:
            return 1

        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums1 = [0, 1, 0, 3, 2, 3]

    nums2 = [7, 7, 7, 7, 7, 7, 7]
    nums3 = [4, 10, 4, 3, 8, 9]
    s = Solution()
    print(s.lengthOfLIS(nums=nums))
    print(s.lengthOfLIS(nums=nums1))
    print(s.lengthOfLIS(nums=nums2))
    print(s.lengthOfLIS(nums=nums3))
