#predict the winner 
from typing import List
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        l = len(nums)
        s1 = s2 = 0
        while l>0:
            s1+=max(nums[0],nums[l-1])
            print(s1)
            del nums[max(0,l-1)]
            l-=1
            if(l==0):
                break
            s2+=max(nums[0],nums[l-1])
            print(s2)
            del nums[max(0,l-1)]
            l-=1
        return s1>=s2
    
print(Solution().predictTheWinner([1,5,233,7]))