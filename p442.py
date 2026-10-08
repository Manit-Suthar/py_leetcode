#find all duplicates in array
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            index = abs(num) - 1

            if nums[index] < 0:
                ans.append(abs(num))
            else:
                nums[index] = -nums[index]

        return ans
    
print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))