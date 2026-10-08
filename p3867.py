# Sum of GCD of formed pairs
from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        mx = 0

        # Step 1: Build prefixGcd
        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(gcd(num, mx))

        # Step 2: Sort
        prefixGcd.sort()

        # Step 3: Pair smallest with largest
        ans = 0
        left = 0
        right = len(prefixGcd) - 1

        while left < right:
            ans += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return ans