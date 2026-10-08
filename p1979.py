# Find greatest divisor of an array's smallest and largest number
from math import gcd
from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(min(nums),max(nums))
l = [2,4,8,20] 
Sol = Solution()
print(Sol.findGCD(l))