class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        start_sum = [nums[0]]
        for n in nums[1:]:
            start_sum.append(n * start_sum[-1])

        end_sum = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            n = nums[i]
            end_sum.append(n * end_sum[-1])

        res = []
        for i in range(len(nums)):
            ans = 1
            if i + 1 < len(nums):
                ans *= end_sum[len(end_sum) - 2 - i]
            if i > 0:
                ans *= start_sum[i - 1]

            res.append(ans)

        return res
