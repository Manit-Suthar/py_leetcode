from functools import cache
from math import gcd
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        @cache
        def dp(i: int, g1: int, g2: int) -> int:
            # Base case
            if i == n:
                return 1 if g1 == g2 and g1 != 0 else 0

            x = nums[i]

            # Choice 1: Put x in first subsequence
            take1 = dp(i + 1, gcd(g1, x), g2)

            # Choice 2: Put x in second subsequence
            take2 = dp(i + 1, g1, gcd(g2, x))

            # Choice 3: Skip x
            skip = dp(i + 1, g1, g2)

            return (take1 + take2 + skip) % MOD

        return dp(0, 0, 0)
    
print(Solution().subsequencePairCount([1,2,3,4]))