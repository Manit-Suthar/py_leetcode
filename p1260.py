from typing import List

class Solution:
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        total = m * n
        k %= total

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                old = i * n + j
                new = (old + k) % total

                r = new // n
                c = new % n

                ans[r][c] = grid[i][j]

        return ans
print(Solution().shiftGrid([[1,2,3,5],[4,5,6,5]],1))