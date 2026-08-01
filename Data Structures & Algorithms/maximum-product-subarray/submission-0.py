class Solution:
    def maxProduct(self, nums):
        res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            temp_max = max(n, n * cur_max, n * cur_min)
            cur_min = min(n, n * cur_max, n * cur_min)
            cur_max = temp_max

            res = max(res, cur_max)

        return res