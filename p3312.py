# hard one 

from collections import Counter
from itertools import accumulate
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums, queries):
        mx = max(nums)

        cnt = Counter(nums)

        cntG = [0] * (mx + 1)

        for i in range(mx, 0, -1):
            v = 0

            for j in range(i, mx + 1, i):
                v += cnt[j]
                cntG[i] -= cntG[j]

            cntG[i] += v * (v - 1) // 2

        prefix = list(accumulate(cntG))

        return [bisect_right(prefix, q) for q in queries]