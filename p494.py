class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)
       
        if (target + total_sum) % 2 != 0 or abs(target) > total_sum:
            return 0
            
        new_target = (target + total_sum) // 2
     
        dp = [0] * (new_target + 1)
        dp[0] = 1 
        for num in nums:
            for i in range(new_target, num - 1, -1):
                dp[i] = dp[i] + dp[i - num]
                
        return dp[new_target]
