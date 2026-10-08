from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # A rectangle is represented as [x1, y1, x2, y2]
        
        # Check if either rectangle is a line (has no area)
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:
            return False
            
        # Check if rec2 is completely to the left, right, below, or above rec1
        if (rec2[2] <= rec1[0] or  # Left
            rec2[0] >= rec1[2] or  # Right
            rec2[3] <= rec1[1] or  # Below
            rec2[1] >= rec1[3]):   # Above
            return False
            
        return True
    
print(Solution().isRectangleOverlap([0,0,2,2],[1,1,3,3]))  # Output: True
