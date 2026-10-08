class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Step 1: Find the minimum odd number in the array
        min_odd = min((x for x in nums1 if x % 2 != 0), default=None)
        
        # If there are no odd numbers, the array is already all even (True)
        if min_odd is None:
            return True
            
        # Step 2: Ensure no even number is smaller than the minimum odd number
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False
                
        return True
