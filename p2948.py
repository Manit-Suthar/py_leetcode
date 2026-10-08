from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        pairs = sorted((x, i) for i, x in enumerate(nums))
        ans = [0] * n

        start = 0

        while start < n:
            end = start

            while end + 1 < n and pairs[end + 1][0] - pairs[end][0] <= limit:
                end += 1

            values = sorted(x for x, _ in pairs[start:end + 1])
            indices = sorted(i for _, i in pairs[start:end + 1])

            for i in range(len(values)):
                ans[indices[i]] = values[i]

            start = end + 1

        return ans