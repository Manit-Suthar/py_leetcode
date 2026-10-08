class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suff_min = [0] * n
        current_min = float('inf')
        for i in range(n - 1, -1, -1):
            if nums[i] < current_min:
                current_min = nums[i]
            suff_min[i] = current_min
            
        current_max = -float('inf')
        for i in range(n):
            if nums[i] > current_max:
                current_max = nums[i]
            
            if current_max - suff_min[i] <= k:
                return i
                
        return -1
