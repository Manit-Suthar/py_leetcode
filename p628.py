#max product of three nums
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n1 = n2 = n3 = float('-inf')
        m1 = m2 = float('inf')

        for n in nums:

            # Three largest
            if n >= n1:
                n3 = n2
                n2 = n1
                n1 = n
            elif n >= n2:
                n3 = n2
                n2 = n
            elif n > n3:
                n3 = n

            # Two smallest
            if n <= m1:
                m2 = m1
                m1 = n
            elif n < m2:
                m2 = n

        return max(n1 * n2 * n3,
                   n1 * m1 * m2)

print(Solution().maximumProduct([3, 1, 2]))
print(Solution().maximumProduct([3,1,2]))
    