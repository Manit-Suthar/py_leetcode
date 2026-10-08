#max products of 2 elements in array
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = m2 = float('-inf')
        for n in nums:
            if(n>=m1):
                m2 = m1
                m1 = n
            elif(n>=m2):
                m2 = n
        return (m1-1)*(m2-1)
print(Solution().maxProduct([1,4,2,5]))     