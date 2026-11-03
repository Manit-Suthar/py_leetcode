from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        maximum = max(nums)
        for i in nums:
            if i < maximum:
                count += maximum - i
        return count
    #         return max(nums) * len(nums) - sum(nums)
    
print(Solution().minMoves([4,4,5]))