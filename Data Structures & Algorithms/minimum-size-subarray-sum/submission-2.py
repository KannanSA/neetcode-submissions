class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = float("inf")
        left = 0
        curSum = 0

        for right in range(n):
            curSum += nums[right]
            while curSum >= target:
                res = min(res, right - left + 1)
                curSum -= nums[left]
                left += 1

        return 0 if res == float("inf") else res