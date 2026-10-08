#smallest missing multiple of k
from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        hashSet = set(nums)
        mul = k
        i = 1
        while mul in hashSet:
            i += 1
            mul = k * i

        return mul
    
print(Solution().missingMultiple([8,2,3,4,6],2))