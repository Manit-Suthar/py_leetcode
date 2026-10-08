from typing import List
# hard 
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        ans = []

        for l, r in queries:
            t = s[l:r + 1]
            ones = t.count('1')
            best = ones

            n = len(t)

            for i in range(n):
                if t[i] != '1':
                    continue

                j = i
                while j + 1 < n and t[j + 1] == '1':
                    j += 1

                if i == 0 or j == n - 1:
                    i = j + 1
                    continue

                if t[i - 1] != '0' or t[j + 1] != '0':
                    i = j + 1
                    continue

                left = 0
                p = i - 1
                while p >= 0 and t[p] == '0':
                    left += 1
                    p -= 1

                right = 0
                p = j + 1
                while p < n and t[p] == '0':
                    right += 1
                    p += 1

                best = max(best, ones + left + right)

                i = j + 1

            ans.append(best)

        return ans