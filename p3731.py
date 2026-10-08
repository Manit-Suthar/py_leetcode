# find missing elements
from typing import List
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        minimum = min(nums)
        maximum = max(nums)
        # for i in range(len(nums)):
        #     if nums[i]<min:
        #         min = nums[i]
        #     if nums[i]>max:
        #         max = nums[i]
        for j in range(minimum+1,maximum):
            if j not in nums:
                ans.append(j)
        return ans
print(Solution().findMissingElements([1,5,2]))