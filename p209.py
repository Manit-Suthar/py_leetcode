# maximum subarray sum
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        window_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0
print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))