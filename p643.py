# max average sub array - sliding window 
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        prev = sum
        for i in range (k):
                sum+= nums[i]
        prev = sum

        for i in range(len(nums)-k):
                prev = prev-nums[i]+nums[i+k]
                temp = prev
                sum = max(temp, sum)
        return sum/k

l = [4,2,1,3,3]
print(Solution().findMaxAverage(l, 2))